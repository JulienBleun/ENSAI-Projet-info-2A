# TODO Rajouter une fonction permettant la connexion

import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection
from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.business_object.utilisateur import Utilisateur
from src.dao.collection_physique_dao import CollectionPhysiqueDAO

from src.utils.mdp_utils import hasher_mot_de_passe
from src.utils.mdp_utils import verifier_mot_de_passe






class UtilisateurDao(metaclass=Singleton):
    """Classe DAO pour ............... dans la base de données"""

#    @log
    @log
    def add_utilisateur(self, utilisateur: Utilisateur):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    mot_de_passe_hashe, sel = hasher_mot_de_passe(utilisateur.mdp)
                    cursor.execute(
                    "INSERT INTO tp.utilisateur (nom, prenom, pseudo, email, mdp, sel)"
                    "VALUES (%(nom)s, %(prenom)s, %(pseudo)s, %(email)s, %(mdp)s, %(sel)s)"
                    "RETURNING id_utilisateur;",
                    {
                        "nom": utilisateur.nom,
                        "prenom": utilisateur.prenom,
                        "pseudo": utilisateur.pseudo,
                        "email": utilisateur.email,
                        "mdp": mot_de_passe_hashe,
                        "sel": sel.hex(),  # Stockez le sel en hexadécimal pour compatibilité SQL
                    },
                )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        if res:
            utilisateur.id_utilisateur = res["id_utilisateur"]
            created = True

        return created

    def read_profil(self, id: int) -> dict:
        """
        Lire le profil d'un utilisateur à partir de la base de données.

        Paramètres :
        ------------
        id : int
            Identifiant de l'utilisateur.

        Retourne :
        ----------
        dict : Un dictionnaire contenant les informations du profil utilisateur si trouvé, sinon None.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT id, nom, mdp
                        FROM utilisateurs
                        WHERE id = %s;
                        """,
                        (id,)
                        )
                    res = cursor.fetchone()  # Récupérer la première ligne de la requête

            if res:

                # Retourne un dictionnaire représentant le profil de
                # utilisateur

                return {
                    "id": res["id"],
                    "nom": res["nom"],
                    "mdp": res["mdp"]
                }
            else:
                print(f"Utilisateur avec l'ID {id} introuvable.")
                return None

        except Exception as e:
            print(f"Erreur lors de la lecture du profil : {e}")
            return None

        except Exception as e:
            print(f"Erreur lors de la lecture du profil : {e}")
            return None

    def delete_utilisateur(self, id: int) -> bool:
        """
        Supprime un utilisateur de la base de données en fonction de
        l'identifiant.

        Paramètres :
        ------------
        id : int
            L'identifiant unique de l'utilisateur à supprimer.

        Retourne :
        ----------
        bool : Indique si la suppression a été effectuée avec succès.
        """
        deleted = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                # 1. On supprime ses avis
                cursor.execute(
                    "DELETE FROM tp.avis_collection WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )
                cursor.execute(
                    "DELETE FROM tp.avis_manga WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )

                # 2. On supprime ses collections en utilisant les fonctionnalités des classes DAO appropriées

                cursor.execute(
                    "SELECT id_collection FROM tp.collection WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )
                res1 = cursor.fetchall()
                for id_collection in res1:
                    collection_coherente = CollectionCoherenteDAO().read_coherente(id_collection)
                    suppression = CollectionCoherenteDAO().delete_coherente(collection_coherente)
                    if not (suppression):
                        collection_physique = CollectionCoherenteDAO().read_physique(id_collection)
                        suppression = CollectionCoherenteDAO().delete_physique(collection_physique)

                # 3. On supprime finalement le compte

                cursor.execute(
                    "DELETE FROM utilisateurs WHERE id = %(id)s RETURNING id;",
                    {"id": id}
                )
                res = cursor.fetchone()

        if res:
            deleted = True

        return deleted

    @log
    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter grâce à son pseudo et son mot de passe.

        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur.
        mdp : str
            Mot de passe de l'utilisateur.

        Returns
        -------
        Utilisateur : L'utilisateur connecté ou None si échoue.
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM tp.utilisateur WHERE pseudo = %(pseudo)s AND mdp = %(mdp)s;",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        utilisateur = None

        if res:
            mdp_hashe = res["mdp"]
            sel = bytes.fromhex(res["sel"])  # Convertir le sel en bytes
            if verifier_mot_de_passe(mdp, mdp_hashe, sel):
                utilisateur = Utilisateur(
                    id_utilisateur=res["id_utilisateur"],  # Assuming you have an ID field in the DB
                    nom=res["nom"],
                    prenom=res["prenom"],
                    pseudo=res["pseudo"],
                    email=res["email"],
                    mdp=res["mdp"]
                )

        return utilisateur

    @log
    def update_utilisateur(self, utilisateur: Utilisateur) -> bool:
        """
        Met à jour les informations d'un utilisateur dans la base de données.

        Paramètres :
        ------------
        utilisateur : Utilisateur
            L'objet utilisateur contenant les informations mises à jour.

        Retourne :
        ----------
        bool : Indique si la mise à jour a été effectuée avec succès.
        """
        updated = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE tp.utilisateur
                        SET nom = %(nom)s,
                            prenom = %(prenom)s,
                            pseudo = %(pseudo)s,
                            email = %(email)s,
                            mdp = %(mdp)s
                        WHERE id_utilisateur = %(id_utilisateur)s
                        RETURNING id_utilisateur;
                        """,
                        {
                            "nom": utilisateur.nom,
                            "prenom": utilisateur.prenom,
                            "pseudo": utilisateur.pseudo,
                            "email": utilisateur.email,
                            "mdp": utilisateur.mdp,
                            "id_utilisateur": utilisateur.id_utilisateur,
                        }
                    )
                    res = cursor.fetchone()

            if res:
                updated = True

        except Exception as e:
            logging.info(f"Erreur lors de la mise à jour de l'utilisateur : {e}")
            raise

        return updated

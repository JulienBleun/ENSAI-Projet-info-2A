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

    @log
    def add_utilisateur(self, utilisateur: Utilisateur):
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    mot_de_passe_hashe, sel = hasher_mot_de_passe(utilisateur.mdp)
                    print(mot_de_passe_hashe, sel)
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

    def read_profil(self, pseudo: str):
        """
        Permet d'obtenir l'id d'un utilisateur à partir de son pseudo.

        Paramètres :
        ------------
        pseudo : str
            pseudo de l'utilisateur dont on souhaite obtenir l'id.

        Retourne :
        ----------
        dict : Un dictionnaire contenant les informations du profil utilisateur si trouvé, sinon None.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT tp.utilisateur.id_utilisateur
                        FROM tp.utilisateur
                        WHERE pseudo = %(pseudo)s;
                        """,
                        {
                            "pseudo": pseudo
                        }
                    )
                    res = cursor.fetchone()

            if res:

                return {
                    "id_utilisateur": res["id_utilisateur"]
                }
            else:
                print(f"Utilisateur avec le pseudo {pseudo} introuvable.")
                return None

        except Exception as e:
            print(f"Erreur lors de la lecture du profil : {e}")
            return None

    def delete_utilisateur(self, id_utilisateur: int) -> bool:
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
                cursor.execute(
                    "DELETE FROM tp.utilisateur WHERE id_utilisateur = %(id_utilisateur)s RETURNING id_utilisateur;",
                    {"id_utilisateur": id_utilisateur}
                )
                res = cursor.fetchone()

        if res:
            deleted = True

        return deleted

    def se_connecter(self, pseudo: str, mdp: str) -> Utilisateur:
        """Se connecter grâce à son pseudo et son mot de passe.
        Parameters
        ----------
        pseudo : str
            Pseudo de l'utilisateur.
        mdp : str
            Mot de passe de l'utilisateur.
        Returns
        -------
        Utilisateur : L'utilisateur connecté ou None si échec.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM tp.utilisateur WHERE pseudo = %(pseudo)s;",
                        {"pseudo": pseudo},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(f"Erreur lors de la connexion : {e}")
            return None
        if res:
            mdp_hashe1 = res["mdp"]
            sel1 = bytes.fromhex(res["sel"])  # Convertir le sel hexadécimal en bytes
            mdp_hashe, sel = hasher_mot_de_passe(mdp)
            if verifier_mot_de_passe(mdp, mdp_hashe, sel):
                return Utilisateur(
                    id_utilisateur=res["id_utilisateur"],
                    nom=res["nom"],
                    prenom=res["prenom"],
                    pseudo=res["pseudo"],
                    email=res["email"],
                    mdp=mdp_hashe1,
                    sel=sel1
                )
        return None

    @log
    def update_utilisateur(self, id_utilisateur, nouveau_pseudo,
                           nouveau_mdp) -> bool:
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
            mot_de_passe_hashe = hasher_mot_de_passe(nouveau_mdp)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        UPDATE tp.utilisateur
                        SET pseudo = %(pseudo)s,
                            mdp = %(mdp)s
                        WHERE id_utilisateur = %(id_utilisateur)s
                        RETURNING id_utilisateur;
                        """,
                        {
                            "pseudo": nouveau_pseudo,
                            "mdp": mot_de_passe_hashe,
                            "id_utilisateur": id_utilisateur,
                        }
                    )
                    res = cursor.fetchone()

            if res:
                updated = True

        except Exception as e:
            logging.info(f"Erreur lors de la mise à jour de l'utilisateur : {e}")
            raise

        return updated

# TODO Rajouter une fonction permettant la connexion

import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection
from collection_coherente_dao import CollectionCoherenteDAO57
from collection_physique_dao import CollectionPhysiqueDAO

from src.business_object.manga import Manga
from src.business_object.utilisateur import Utilisateur



class UtilisateurDao(metaclass=Singleton):
    """Classe DAO pour ............... dans la base de données"""

#    @log
    @log
    def add_utilisateur(self, nom, prenom, nom_utilisateur, email, mot_de_passe):
        # Vérifier si le schéma et la table existent, sinon les créer
        create_schema_query = """
            CREATE SCHEMA IF NOT EXISTS tp;
        """
        create_table_query = """
            CREATE TABLE IF NOT EXISTS tp.utilisateur (
                id_utilisateur SERIAL PRIMARY KEY,
                nom VARCHAR(100),
                prenom VARCHAR(100),
                nom_utilisateur VARCHAR(1000) UNIQUE,
                email VARCHAR(400),
                mot_de_passe VARCHAR(10)
            );
        """

        insert_query = """
            INSERT INTO tp.utilisateur
                (nom, prenom, nom_utilisateur, email, mot_de_passe)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING id_utilisateur;
        """
        values = (nom, prenom, nom_utilisateur, email, mot_de_passe)

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Créer le schéma et la table si nécessaire
                    cursor.execute(create_schema_query)
                    cursor.execute(create_table_query)
                    # Insérer l'utilisateur
                    cursor.execute(insert_query, values)
                    id_utilisateur = cursor.fetchone()[0]
                    connection.commit()
                    return id_utilisateur
        except Exception as e:
            logging.error(f"Erreur lors de l'ajout de l'utilisateur: {e}")
            logging.error(f"Détails de l'erreur: {str(e._class_._name_)}")
            logging.error(f"Message d'erreur complet: {str(e)}")
            logging.error(f"Valeurs tentées: nom={nom}, prenom={prenom}, nom_utilisateur={nom_utilisateur}, email={email}")
            raise e

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
                    "DELETE FROM avis_collection WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )
                cursor.execute(
                    "DELETE FROM avis_manga WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )

                # 2. On supprime ses collections en utilisant les fonctionnalités des classes DAO appropriées

                cursor.execute(
                    "SELECT id_collection FROM collection WHERE id_utilisateur = %(id_utilisateur)s;",
                    {"id_utilisateur": id}
                )
                res1 = cursor.fetchall()
                for id_collection in res1 :
                    collection_coherente = readCoherent (id_collection)
                    suppression = deleteCoherent(collection_coherente)
                    if not(suppression):
                        collection_physique = readPhysique(id_collection)
                        suppression = detePhysique(collection_physique)

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
                        "SELECT * FROM utilisateurs WHERE pseudo = %(pseudo)s AND mot_de_passe = %(mdp)s;",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        utilisateur = None

        if res:
            utilisateur = Utilisateur(
                id_utilisateur=res["id_utilisateur"],  # Assuming you have an ID field in the DB
                nom=res["nom"],
                prenom=res["prenom"],
                pseudo=res["pseudo"],
                email=res["email"],
                mot_de_passe=res["mot_de_passe"]
            )

        return utilisateur

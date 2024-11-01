# TODO Rajouter une fonction permettant la connexion

import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.manga import Manga
from src.business_object.utilisateur import Utilisateur


class UtilisateurDao(metaclass=Singleton):
    """Classe DAO pour ............... dans la base de données"""

#    @log
    @log
    def add_utilisateur(self, nom, prenom, pseudo, email, mot_de_passe) -> bool:
        """
        Ajouter un utilisateur à la base de données.

        Paramètres :
        ------------
        nom : str
            Nom de l'utilisateur.
        prenom : str
            Prénom de l'utilisateur.
        pseudo : str
            Pseudo de l'utilisateur.
        email : str
            Email de l'utilisateur.
        mot_de_passe : str
            Mot de passe de l'utilisateur.

        Retourne :
        ----------
        bool : Indique si l'utilisateur a été ajouté avec succès.
        """
        created = False
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO utilisateur (nom, prenom, pseudo, email, mot_de_passe)
                        VALUES (%(nom)s, %(prenom)s, %(pseudo)s, %(email)s, %(mot_de_passe)s)
                        RETURNING id_utilisateur;
                        """,
                        {
                            "nom": nom,
                            "prenom": prenom,
                            "pseudo": pseudo,
                            "email": email,
                            "mot_de_passe": mot_de_passe,
                        },
                    )
                    res = cursor.fetchone()

            if res:
                created = True

        except Exception as e:
            logging.info(e)
            raise

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

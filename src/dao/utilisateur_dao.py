# A voir si ça marche .

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga import Manga


class UtilisateurDao(metaclass=Singleton):
    """Classe DAO pour ............... dans la base de données"""

#    @log
    def add_Utilisateur(self,utilisateur) -> bool:
        """
        Ajouter un utilisateur à la base de données.

        Paramètres :
        ------------
        utilisateur : Utilisateur
            Instance d'utilisateur.

        Retourne :
        ----------
        bool : Indique si l'utilisateur a été ajouté avec succès.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                   cursor.execute(
                    """
                    INSERT INTO utilisateurs (id, nom, mdp)
                    VALUES (%(id)s, %(nom)s, %(mdp)s)
                    RETURNING id;
                    """,
                    {
                        "id": utilisateur["id"],
                        "nom": utilisateur["nom"],
                        "mdp": utilisateur["mdp"],
                    },
                )
                res = cursor.fetchone()

        if res:
            utilisateur["id"] = res["id"]
            created = True

        return created

    def delete_utilisateur(self, id: int) -> bool:
        """
        Supprime un utilisateur de la base de données en fonction de l'identifiant.

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
            # Retourne un dictionnaire représentant le profil de l'utilisateur
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


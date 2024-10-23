# A voir si ça marche .

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga import Manga


class utilisateur_dao(metaclass=Singleton):
    """Classe DAO pour ............... dans la base de données"""

#    @log
    def Add_Utilisateur(self,utilisateur) -> bool:
        """
        Ajouter un utilisateur à la base de données.

        Paramètres :
        ------------
        utilisateur : dict
            Dictionnaire représentant un utilisateur avec 'id', 'nom', et 'mdp' (mot de passe).

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
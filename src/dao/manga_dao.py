### A voir si ça marche c'est un copié collé de la template ...

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga import Manga


class MangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de données"""

    @log
    def trouver_par_id(self, id_manga) -> Manga:
        """trouver un manga grace à son id

        Parameters
        ----------
        id_manga : int
            numéro id du manga que l'on souhaite trouver

        Returns
        -------
        manga : Manga
            renvoie le manga que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM manga                      "
                        " WHERE id_manga = %(id_manga)s;  ",
                        {"id_manga": id_manga},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        manga = None
        if res:
            manga = Manga(
                titre=res["pseudo"],
                auteur=res["age"],
                id_manga=res["id_manga"],
            )

        return manga

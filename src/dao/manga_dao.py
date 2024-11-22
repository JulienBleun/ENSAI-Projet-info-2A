import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.manga import Manga


class MangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Mangas de la base de """
    """données"""

    @log
    def rechercher_manga_par_id(self, id_manga) -> Manga:
        """Trouver un manga grace à son id

        Parameters
        ----------
        id_manga : int
            Numéro id du manga que l'on souhaite trouver

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
                        "  FROM tp.manga                      "
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
                id_manga=res["id_manga"],
                titre=res["titre"],
                descript=res["descript"],
                auteur=res["auteur"],
                )

        return manga

    @log
    def rechercher_manga_par_titre(self, titre) -> Manga:
        """Trouver un manga grace à son titre

        Parameters
        ----------
        titre : str
            Titre du manga que l'on souhaite trouver

        Returns
        -------
        manga : Manga
            Renvoie le manga que l'on cherche par titre
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM tp.manga                      "
                        " WHERE titre = %(titre)s;  ",
                        {"titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        manga = None
        if res:
            manga = Manga(
                id_manga=res["id_manga"],
                titre=res["titre"],
                descript=res["descript"],
                auteur=res["auteur"],
                )

        return manga

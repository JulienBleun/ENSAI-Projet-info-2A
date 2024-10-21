### TODO commandes sql et autres méthodes (la première marche théoriquement)

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.avis import Avis


class AvisMangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de """
    """données"""

    @log
    def create_avis(self, id_avis, id_utilisateur, id_manga,
                    contenu, note) -> Avis:
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
                        "INSERT INTO avis_manga(id_avis, id_utilisateur,"
                        "id_manga, contenu, note) VALUES                "
                        "(%(id_avis)s, %(id_utilisateur)s, %(id_manga)s, "
                        "%(contenu)s, %(note)s)             "
                        "  RETURNING id_joueur;                                                ",
                        {
                            "id_avis": avis_manga.id_avis,
                            "id_utilisateur": avis_manga.id_utilisateur,
                            "id_manga": avis_manga.id_manga,
                            "contenu": avis_manga.contenu,
                            "note": avis_manga.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

       created = False
        if res:
            avis_manga.id_avis = res["id_avis"]
            created = True

        return created

    @log
    def UpdateAvis(self,id_avis, nouveau_contenu,
        nouvelle_note) -> Avis:
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
                        "INSERT INTO avis_manga(id_avis, id_utilisateur,"
                        "id_manga, contenu, note) VALUES                "
                        "(%(id_avis)s, %(id_utilisateur)s, %(id_manga)s, "
                        "%(contenu)s, %(note)s)             "
                        "  RETURNING id_joueur;                                                ",
                        {
                            "id_avis": avis_manga.id_avis,
                            "id_utilisateur": avis_manga.id_utilisateur,
                            "id_manga": avis_manga.id_manga,
                            "contenu": avis_manga.contenu,
                            "note": avis_manga.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

       created = False
        if res:
            avis_manga.id_avis = res["id_avis"]
            created = True

        return created UpdateAvis(id_avis, nouveau_contenu,
nouvelle_note)

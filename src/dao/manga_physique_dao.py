import requests
import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.manga_physique import MangaPhysique


class MangaPhysiqueDAO(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de """
    """données"""

    #@log
    def create_manga_physique(self, manga: MangaPhysique) -> bool:
        """Créer un manga sous la forme physique dans la base de données

        Parameters
        ----------
        manga : MangaPhysique
            numéro id du manga que l'on souhaite trouver

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO manga_physique(id_manga_physique, id_collection, "
                        "id_manga, dernier_tome_acquis, tomes_manquants, statut) VALUES                 "
                        "(%(id_manga_physique)s, %(id_collection)s, %(id_manga)s"
                        " %(dernier_tome_acquis)s, %(tomes_manquants)s, "
                        "%(statut)s)                         "
                        "  RETURNING id_manga_physique;                          ",
                        {
                            "id_manga_physique": manga.id_manga_physique,
                            "id_collection": manga.id_collection,
                            "id_manga": manga.id_manga,
                            "dernier_tome_acquis": manga.dernier_tome_acquis,
                            "tomes_manquants": manga.tomes_manquants,
                            "statut": manga.statut
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        if res:
            manga.id_manga_physique = res["id_manga_physique"]
            created = True

        return created

     #@log
    def update_manga_physique(self, manga: MangaPhysique) -> bool:
        """Modifier un manga sous la forme physique dans la base de données

        Parameters
        ----------
        manga : MangaPhysique
            numéro id du manga que l'on souhaite trouver

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        res = None

        #try:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE manga_physique                                     "
                    "   SET id_manga_physique        = %(id_manga_physique)s,  "
                    "       id_collection            = %(id_collection)s,      "
                    "       id_manga                 = %(id_manga)s,           "
                    "       dernier_tome_acquis      = %(dernier_tome_acquis)s,"
                    "       tomes_manquants          = %(tomes_manquants)s     "
                    "       statut                   = %(statut)s              "
                    " WHERE id_manga_physique        = %(id_manga_physique)s;  ",
                    {
                            "id_manga_physique": manga.id_manga_physique,
                            "id_collection": manga.id_collection,
                            "id_manga": manga.id_manga,
                            "dernier_tome_acquis": manga.dernier_tome_acquis,
                            "tomes_manquants": manga.tomes_manquants,
                            "statut": manga.statut
                    },
                )
                res = cursor.rowcount
        #except Exception as e:
            #logging.info(e)

        return res == 1



    #@log

    def read_manga_physique(self, id_manga) -> MangaPhysique:
        """Trouver un manga physique grâce à son id

        Parameters
        ----------
        id_manga : int
            numéro id du manga physique que l'on souhaite trouver

        Returns
        -------
        avis : MangaPhysique
            renvoie le manga physique que l'on cherche par id
        """
        #try:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM manga_physique                      "
                        " WHERE id_manga_physique = %(id_manga_physique)s;  ",
                        {"id_manga_physique": id_manga},
                )
        res = cursor.fetchone()
        #except Exception as e:
        #logging.info(e)
            #raise

        manga = None
        if res:
            manga = MangaPhysique(
                id_manga_physique=res["id_manga_physique"],
                id_collection=res["id_collection"],
                id_manga=res["id_manga"],
                dernier_tome_acquis=res["dernier_tome_acquis"],
                tomes_manquants=res["tomes_manquants"],
                statut=res["statut"]
            )
        return manga

import requests
import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.manga_physique import MangaPhysique


class MangaPhysiqueDAO(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de """
    """données"""

    @log
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
                        "SELECT 1 FROM tp.manga WHERE tp.manga.titre = %(titre_manga)s;",
                        {"titre_manga": manga.titre_manga},
                    )
                    exists = cursor.fetchone()

                    if not exists:
                        logging.info(f"Le manga '{manga.titre_manga}' n'est"
                                     " pas recensé dans la base de données.")

                        return False
                    cursor.execute(
                        "INSERT INTO tp.manga_physique(titre_manga, tomes_acquis,"
                        " statut, id_utilisateur) VALUES                 "
                        "(%(titre_manga)s, %(tomes_acquis)s, %(statut)s, "
                        "%(id_utilisateur)s)                         "
                        "  RETURNING id_manga_physique;                          ",
                        {
                            "titre_manga": manga.titre_manga,
                            "tomes_acquis": manga.tomes_acquis,
                            "id_utilisateur": manga.id_utilisateur,
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

    @log
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

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                    UPDATE tp.manga_physique
                    SET id_utilisateur = %(id_utilisateur)s, titre_manga = %(titre_manga)s,
                    tomes_acquis = %(tomes_acquis)s, statut = %(statut)s
                    WHERE id_manga_physique = %(id_manga_physique)s;
                    """,
                    {
                        "id_manga_physique": manga.id_manga_physique,
                        "id_utilisateur": manga.id_utilisateur,
                        "titre_manga": manga.titre_manga,
                        "tomes_acquis": manga.tomes_acquis,
                        "statut": manga.statut,
                    },
                    )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)

        return res == 1

    def delete_manga_physique(self, id_supprime: int) -> bool:
        """
        Suppression d'un manga physique dans la base de données

        Parameters
        ----------
        manga_physique : MangaPhysique
            manga physique à supprimer de la base de données

        Returns
        -------
            True si le manga physique a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tp.manga_physique                   "
                        " WHERE tp.manga_physique.id_manga_physique=%(id_manga_physique)s      ",
                        {"id_manga_physique": id_supprime},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def recup_manga_physique_from_id(self, id_utilisateur):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM tp.manga_physique"
                        " WHERE id_utilisateur='%(id_utilisateur)s'",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

# A voir si ça marche c'est un copié collé de la template ...
import requests
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
        """Trouver un manga grace à son id

        Parameters
        ----------
        id_manga : int
            numéro id du manga que l'on souhaite trouver

        Returns
        -------
        manga : Manga
            renvoie le manga que l'on cherche par titre
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

    """@log
    def rechercher_manga_par_titre(self, titre):
        url = f"https://api.jikan.moe/v4/manga?q={titre}"
        response = requests.get(url)

        if response.status_code == 200:
            resultats = response.json()['data']
            print(resultats)
            if not resultats:
                print("Aucun manga trouvé.")
                return None  # Pas de mangas trouvés

            # Affichage des mangas trouvés
            for index, manga in enumerate(resultats):
                print(f"{index + 1}. Titre: {manga['title']}, ID: {manga['mal_id']}")

            return resultats  # Retourner les résultats pour un usage ultérieur
        else:
            print("Erreur lors de la recherche.")
            return None

# Créer une instance de MangaDao pour être utilisée ailleurs
manga_dao = MangaDao()"""

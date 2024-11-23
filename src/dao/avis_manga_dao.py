import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.avis_manga import AvisManga


class AvisMangaDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux avis des mangas de la """
    """base de données"""

    @log
    def create_avis_manga(self, avis: AvisManga) -> bool:
        """Création d'un avis sur un manga dans la base de données

        Parameters
        ----------
        avis : AvisManga
            Instance AvisManga à écrire en base de données.

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # On vérifie si l'utilisateur a déjà un avis sur cette
                    # collection
                    cursor.execute(
                        """
                        SELECT 1
                        FROM tp.avis_manga
                        WHERE id_utilisateur = %(id_utilisateur)s
                        AND id_manga = %(id_manga)s;
                        """,
                        {"id_utilisateur": avis.id_utilisateur, "id_manga": avis.id_manga},
                    )
                    result = cursor.fetchone()
                    if result:
                        return False  # Pas besoin de continuer si un avis existe déjà
                    cursor.execute(
                        "INSERT INTO tp.avis_manga (id_utilisateur, id_manga, commentaire, note)"
                        "VALUES (%(id_utilisateur)s, %(id_manga)s, %(commentaire)s, %(note)s)                         "
                        "  RETURNING id_avis;                          ",
                        {
                            "id_utilisateur": avis.id_utilisateur,
                            "id_manga": avis.id_manga,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        created = False
        if res:
            avis.id_avis = res["id_avis"]
            created = True

        return created

    @log
    def update_avis_manga(self, avis: AvisManga) -> bool:
        """Modifier un avis de manga dans la base de données

        Parameters
        ----------
        avis : AvisManga
            Avis à modifier.

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE tp.avis_manga                                "
                        "   SET id_utilisateur = %(id_utilisateur)s,      "
                        "       id_manga       = %(id_manga)s,            "
                        "       commentaire    = %(commentaire)s,             "
                        "       note           = %(note)s                 "
                        " WHERE id_avis      = %(id_avis)s;           ",
                        {
                            "id_utilisateur": avis.id_utilisateur,
                            "id_manga": avis.id_manga,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                            "id_avis": avis.id_avis
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    @log
    def delete_avis_manga(self, avis: AvisManga) -> bool:
        """Supprimer un avis de manga dans la base de données

        Parameters
        ----------
        avis : AvisManga
            Avis à supprimer de la base de données

        Returns
        -------
        created : bool
            True si la suppression a bien été effectuée
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tp.avis_manga                  "
                        " WHERE id_avis=%(id_avis)s        ",
                        {"id_avis": avis.id_avis},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def read_avis_manga(self, id_avis) -> AvisManga:
        """Trouver un avis de manga grâce à son id

        Parameters
        ----------
        id_avis : int
            Numéro id de l'avis que l'on souhaite trouver

        Returns
        -------
        avis : AvisManga
            Renvoie l'avis que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM tp.avis_manga                      "
                        " WHERE id_avis = %(id_avis)s;  ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        avis = None
        if res:
            avis = AvisManga(
                id_avis=res["id_avis"],
                id_manga=res["id_manga"],
                id_utilisateur=res["id_utilisateur"],
                commentaire=res["commentaire"],
                note=res["note"],
                )
        return avis

    def recup_avis_from_id(self, id_utilisateur):
        """Récupérer tous les avis de manga associés à l'id de l'utilisateur.

        Parameters
        ----------
        id_utilisateur : int
            Numéro id de l'utilisateur dont on souhaite voir les avis de manga

        Returns
        -------
        res : List
            Renvoie une liste de dictionnaires contenant les informations sur
            les avis de mangas de l'utilisateur.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT avis_manga.*, titre FROM tp.avis_manga"
                        " JOIN tp.manga ON tp.avis_manga.id_manga=tp.manga.id_manga"
                        " WHERE id_utilisateur='%(id_utilisateur)s'",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def recup_avis_from_titre(self, titre):
        """Récupérer tous les avis de manga en cherchant directement le titre
        du manga.

        Parameters
        ----------
        titre : str
            Titre du manga dont on souhaite voir les avis.

        Returns
        -------
        res : List
            Renvoie une liste de dictionnaires contenant les informations sur
            les avis de mangas correspondant au titre en paramètre.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT avis_manga.*, utilisateur.pseudo FROM tp.avis_manga"
                        " JOIN tp.manga ON tp.avis_manga.id_manga = tp.manga.id_manga"
                        " JOIN tp.utilisateur ON tp.avis_manga.id_utilisateur = tp.utilisateur.id_utilisateur"
                        " WHERE titre=%(titre)s",
                        {"titre": titre},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

### TODO rien normalement c'est bon insh
import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.avis_manga import AvisManga


class AvisCollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux avis des collections """
    """de la base de données"""

    #log
    def create_avis(self, avis: AvisManga) -> bool:
        """trouver un manga grace à son id

        Parameters
        ----------
        avis : AvisManga

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        #try:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO avis_manga(id_avis, id_utilisateur, "
                        "id_manga, contenu, note) VALUES                 "
                        "(%(id_avis)s, %(id_utilisateur)s, %(id_manga)s, "
                        " %(contenu)s, %(note)s)                         "
                        "  RETURNING id_joueur;                          ",
                        {
                            "id_avis": avis.id_avis,
                            "id_utilisateur": avis.id_utilisateur,
                            "id_manga": avis.id_manga,
                            "contenu": avis.contenu,
                            "note": avis.note,
                        },
                    )
                    res = cursor.fetchone()
        # Exception as e:
            #logging.info(e)

        created = False
        if res:
            avis.id_avis = res["id_avis"]
            created = True

        return created

    #@log
    def UpdateAvis(self, avis: AvisManga) -> bool:
        """Modifier un avis dans la bas de données

        Parameters
        ----------
        avis : AvisManga

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """
        res = None

        #try:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE avis                                      "
                        "   SET id_avis        = %(id_avis)s,             "
                        "       id_utilisateur = %(id_utilisateur)s,      "
                        "       id_manga       = %(id_manga)s,            "
                        "       contenu        = %(contenu)s,             "
                        "       note           = %(note)s                 "
                        " WHERE id_joueur      = %(id_joueur)s;           ",
                        {
                            "id_avis": avis.id_avis,
                            "id_utilisateur": avis.id_utilisateur,
                            "id_manga": avis.id_manga,
                            "contenu": avis.contenu,
                            "note": avis.note
                        },
                    )
                    res = cursor.rowcount
        #except Exception as e:
            #logging.info(e)

        return res == 1

    @log
    def DeleteAvis(self, avis: AvisManga) -> bool:
        """Supprimer un avis dans la bas de données

        Parameters
        ----------
        avis : AvisManga
            avis à supprimer de la base de données

        Returns
        -------
        created : bool
            True si la suppression a bien été effectuée
        """

        #try:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM avis                  "
                        " WHERE id_avis=%(id_avis)s        ",
                        {"id_avis": avis.id_avis},
                    )
                    res = cursor.rowcount
        #except Exception as e:
            #logging.info(e)
            #raise

        return res > 0

    @log
    def ReadAvis(self, id_avis) -> AvisManga:
        """Trouver un avis grâce à son id

        Parameters
        ----------
        id_avis : int
            numéro id de l'avis que l'on souhaite trouver

        Returns
        -------
        avis : AvisManga
            renvoie l'avis que l'on cherche par id
        """
        #try:
        with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM avis                      "
                        " WHERE id_avis = %(id_avis)s;  ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()
        #except Exception as e:
        #logging.info(e)
            #raise

        avis = None
        if res:
            avis = AvisManga(
                id_manga=res["id_manga"],
                id_utilisateur=res["id_utilisateur"],
                commentaire=res["commentaire"],
                note=res["note"],
                id_avis=res["id_avis"],
            )
        return avis

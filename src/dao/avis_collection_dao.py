### TODO rien normalement c'est bon insh
import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.avis_collection import AvisCollection


class AvisCollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux avis des collections """
    """de la base de données"""

    #log
    def create_avis_collection(self, avis: AvisCollection) -> bool:
        """Création d'un avis sur une collection dans la base de données

        Parameters
        ----------
        avis : AvisCollection

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
                        "INSERT INTO avis_collection(id_avis, id_utilisateur, "
                        "commentaire, note, id_collection) VALUES                 "
                        "(%(id_avis)s, %(id_utilisateur)s, %(id_collection)s, "
                        " %(contenu)s, %(note)s)                         "
                        "  RETURNING id_avis;                          ",
                        {
                            "id_avis": avis.id_avis,
                            "id_utilisateur": avis.id_utilisateur,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                            "id_collection": avis.id_collection,
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
    def update_avis_collection(self, avis: AvisCollection) -> bool:
        """Modifier un avis de collection dans la base de données

        Parameters
        ----------
        avis : AvisCollection

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
                        "UPDATE avis_collection                            "
                        "   SET id_avis        = %(id_avis)s,             "
                        "       id_utilisateur = %(id_utilisateur)s,      "
                        "       id_manga       = %(id_manga)s,            "
                        "       commentaire    = %(commentaire)s,             "
                        "       note           = %(note)s                 "
                        " WHERE id_joueur      = %(id_joueur)s;           ",
                        {
                            "id_avis": avis.id_avis,
                            "id_utilisateur": avis.id_utilisateur,
                            "id_collection": avis.id_collection,
                            "commentaire": avis.commentaire,
                            "note": avis.note
                        },
                    )
                    res = cursor.rowcount
        #except Exception as e:
            #logging.info(e)

        return res == 1

    #@log
    def delete_avis_collection(self, avis: AvisCollection) -> bool:
        """Supprimer un avis de collection dans la base de données

        Parameters
        ----------
        avis : AvisCollection
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
                        "DELETE FROM avis_collection                  "
                        " WHERE id_avis=%(id_avis)s        ",
                        {"id_avis": avis.id_avis},
                    )
                    res = cursor.rowcount
        #except Exception as e:
            #logging.info(e)
            #raise

        return res > 0

    #@log
    def read_avis(self, id_avis) -> AvisCollection:
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
                        "  FROM avis_collection                     "
                        " WHERE id_avis = %(id_avis)s;  ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()
        #except Exception as e:
        #logging.info(e)
            #raise

        avis = None
        if res:
            avis = AvisCollection(
                id_manga=res["id_manga"],
                id_utilisateur=res["id_utilisateur"],
                commentaire=res["commentaire"],
                note=res["note"],
                id_avis=res["id_avis"],
            )
        return avis

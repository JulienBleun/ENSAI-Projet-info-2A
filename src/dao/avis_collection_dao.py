### TODO rien normalement c'est bon insh
import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.avis_collection import AvisCollection


class AvisCollectionDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux avis des collections """
    """de la base de données"""

    @log
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
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Vérifier si l'utilisateur a déjà un avis sur cette collection
                    cursor.execute(
                        """
                        SELECT 1
                        FROM tp.avis_collection
                        WHERE id_utilisateur = %(id_utilisateur)s
                        AND id_collection = %(id_collection)s;
                        """,
                        {"id_utilisateur": avis.id_utilisateur, "id_collection": avis.id_collection},
                    )

                    result = cursor.fetchone()
                    if result:
                        logging.error(
                            "Vous avez déjà un avis sur cette collection. "
                            "Réessayez avec un autre titre."
                        )
                        return False  # Pas besoin de continuer si un avis existe déjà

                    # Insérer un nouvel avis et récupérer son ID

                    cursor.execute(
                        "INSERT INTO tp.avis_collection(id_utilisateur, "
                        "id_collection, commentaire, note) VALUES                 "
                        "(%(id_utilisateur)s, %(id_collection)s, "
                        " %(commentaire)s, %(note)s)                         "
                        " RETURNING id_avis;                  ",
                        {
                            "id_utilisateur": avis.id_utilisateur,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                            "id_collection": avis.id_collection,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

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

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE tp.avis_collection                           "
                        "   SET id_utilisateur = %(id_utilisateur)s,      "
                        "       commentaire    = %(commentaire)s,             "
                        "       note           = %(note)s                 "
                        " WHERE id_avis      = %(id_avis)s;           ",
                        {
                            "id_utilisateur": avis.id_utilisateur,
                            "commentaire": avis.commentaire,
                            "note": avis.note,
                            "id_avis": avis.id_avis,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    #@log
    def delete_avis_collection(self, id_avis: AvisCollection) -> bool:
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

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM tp.avis_collection                  "
                        " WHERE id_avis=%(id_avis)s        ",
                        {"id_avis": id_avis},
                        )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

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
                id_avis=res["id_avis"],
                id_manga=res["id_manga"],
                id_utilisateur=res["id_utilisateur"],
                commentaire=res["commentaire"],
                note=res["note"],
                )
        return avis

    def recup_avis_collec_from_id(self, id_utilisateur):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_avis, id_utilisateur, tp.avis_collection.id_collection, tp.collection_coherente.titre, commentaire, note FROM tp.avis_collection"
                        " JOIN tp.collection_coherente ON tp.collection_coherente.id_collection=tp.avis_collection.id_collection"
                        " WHERE id_utilisateur='%(id_utilisateur)s'",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def recup_avis_collec_from_id_collec(self, id_collection):

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT tp.utilisateur.pseudo, tp.avis_collection.commentaire, tp.avis_collection.note FROM tp.avis_collection"
                        " JOIN tp.utilisateur ON tp.utilisateur.id_utilisateur=tp.avis_collection.id_utilisateur "
                        " WHERE id_collection='%(id_collection)s'",
                        {"id_collection": id_collection},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

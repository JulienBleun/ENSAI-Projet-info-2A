import logging

from src.utils.singleton import Singleton
#from utils.log_decorator import log

from src.dao.db_connection import DBConnection


from src.business_object.collection_physique import CollectionPhysique
from src.business_object.manga_physique import MangaPhysique




class CollectionPhysiqueDAO(metaclass=Singleton):
    """Classe DAO pour gérer les collections physiques dans la base de données"""

#    @log
    def CreatePhysique(self, collection: CollectionPhysique) -> bool:
        """Création d'une nouvelle collection physique dans la base de données

        Parameters
        ----------
        collection : CollectionPhysique
            Nouvelle collection physique à inserer.

        Returns
        -------
        created : bool
            True si la création a réussi, False sinon.
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO collection (id_collection, id_utilisateur) VALUES "
                        "(%(id_collection)s, %(id_utilisateur)s)",
                        {
                            "id_collection": collection.id_collection,
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    for c in collection.contenu:
                        cursor.execute(
                            "INSERT INTO manga_physique (id_manga_physique, id_collection, id_manga, dernier_tome_acquis, tomes_manquants, statut) VALUES "
                            "(%(id_manga_physique)s, %(id_collection)s, %(id_manga)s, %(dernier_tome_acquis)s, %(tomes_manquants)s, %(statut)s)",
                            {
                                "id_manga_physique": c.id_manga_physique, # Problème résolu
                                "id_collection": c.id_collection_physique,
                                "id_manga": c.id_manga,
                                "dernier_tome_acquis": c.dernier_tome_acquis,
                                "tomes_manquants": c.tomes_manquant,
                                "statut": c.statut
                            }
                        )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)

        created = False
        if res:
            created = True

        return created

    #    @log
    def DeletePhysique(self, collection : CollectionPhysique) -> bool:
        """Suppression d'une collection physique de la base de données

        Parameters
        ----------
        collection : CollectionPhysique
            La collection à supprimer

        Returns
        -------
        deleted : bool
            True si la suppression a réussi, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # 1. Supprimer d'abord les mangas physiques associés à la collection physique que l'on souhaite supprimer
                    cursor.execute(
                        """
                        DELETE FROM manga_physique
                        WHERE id_collection = %(id_collection)s;
                        """,
                        {"id_collection": collection.id_collection},
                    )
                    # 2. Supprimer ensuite la collection physique

                    cursor.execute(
                        "DELETE FROM collection WHERE id_collection = %(id_collection)s;",
                        {"id_collection": collection.id_collection},
                    )
                    deleted = cursor.rowcount > 0  # rowcount > 0 indique si la suppression a affecté des lignes
        except Exception as e:
            logging.info(e)
            deleted = False

        return deleted

#    @log
    def ReadPhysique(self, id : int) -> CollectionPhysique:
        """Lecture d'une collection physique à partir de son ID

        Parameters
        ----------
        id : int
            ID de la collection à lire

        Returns
        -------
        collection : CollectionCoherente
            L'objet CollectionCoherente correspondant
        """
        collection = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM collection WHERE id_collection = %(id_collection)s;",
                        {"id_collection": id},
                    )
                    res1 = cursor.fetone()

                    # 2. Récupérer l'id de l'utilisateur
                    cursor.execute(
                        "SELECT * FROM collection WHERE id_collection = %(id)s;",
                        {"id": id},
                    )
                    res2 = cursor.fetchone()

                    cursor.execute(
                        "SELECT * ",
                        "FROM manga_physique",
                        "WHERE id_collection = %(id_collection)s;",
                        {"id_collection": id},
                    )
                    res3 = cursor.fetchall()

                    if res1:
                        collection = CollectionPhysique(
                            id_collection=res1["id_collection"],
                            id_utilisateur=res2["id_utilisateur"],
                            contenu=[MangaPhysique(
                                id_manga_physique=manga["id_manga_physique"],
                                id_manga=manga["id_manga"],
                                id_collection_physique=manga["id_collection"],
                                dernier_tome_acquis=manga["dernier_tome_acquis"],
                                tomes_manquants=manga["tomes_manquants"],
                                statut=manga["statut"]
                            ) for manga in res3]  # Liste d'objets MangaPhysique
                        )
        except Exception as e:
            logging.info(e)

        return collection

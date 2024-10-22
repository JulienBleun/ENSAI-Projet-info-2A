import logging

from utils.singleton import Singleton
#from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.collection_coherente import Collection_coherente


class CollectionPhysiqueDAO(metaclass=Singleton):
    """Classe DAO pour gérer les collections physiques dans la base de données"""

#    @log
    def CreatePhysique(self, collection : CollectionPhysique) -> bool:
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
                            "id_collection": collection.id_collection,  # Utilisation des attributs de l'objet collection
                            "id_utilisateur": collection.id_utilisateur,
                            },
                    )
                    for c in collection.contenu :
                        cursor.execute(
                            "INSERT INTO manga_physique (id_manga_physique, id_collection, id_manga, dernier_tome_acquis, tomes_manquants, statut) VALUES"
                            "(%(id_maga_physique)s, %(id_collection)s, %(id_manga)s, %(dernier_tome_acquis)s, %(tomes_manquants)s, %(statut)s)"
                            {
                                "id_manga_physique": c.id_manga_physique,
                                "id_collection": c.id_collection_physique,
                                "id_manga": c.id_manga
                                "dernier_tome_acquis": c.dernier_tome_acquis
                                "tomes_manquants": c.tomes_manquants
                                "statut": c.statut
                            
                                }
                        )
                    res = cursor.fetchone()
#        except Exception as e:
#            logging.info(e)

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
                    cursor.execute(
                        "DELETE FROM collection WHERE id_collection = %(id_collection)s;",
                        {"id_collection": collection.id_collection},
                    )
                    deleted = cursor.rowcount > 0  # rowcount > 0 indique si la suppression a affecté des lignes
#        except Exception as e:
#            logging.info(e)
#            deleted = False

        return deleted

#    @log
    def ReadPhysique(self, id : int) -> CollectionCoherente:
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
                        "SELECT * FROM collection_physique WHERE id = %(id)s;",
                        {"id": id},
                    )
                    res = cursor.fetchone()

                    cursor.execute(
                        "SELECT * ",
                        "FROM collection_physique as c ",
                        "JOIN manga_physique as m",
                        "ON c.id_collection = m.id_collection",
                        "WHERE id = %(id)s;",
                        {"id": id},
                    )
                    res2 = cursor.fetchone()

                    if res:
                        collection = CollectionPhysique(
                            id_collection=res["id_collection"],
                            id_utilisateur=res["id_utilisateur"],
                            contenu=res[""],
                        )
#        except Exception as e:
#            logging.info(e)

        return collection

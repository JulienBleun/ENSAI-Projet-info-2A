import logging

from utils.singleton import Singleton
#from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.collection_coherente import Collection_coherente


class Collection_coherenteDAO(metaclass=Singleton):
    """Classe DAO pour gérer les collections cohérentes dans la base de données"""

#    @log
    def CreateCoherente(self, collection: CollectionCoherente) -> bool:
        """Création d'une nouvelle collection cohérente dans la base de données

        Parameters
        ----------
        collection : Collection_coherente
            Objet représentant la collection cohérente

        Returns
        -------
        created : bool
            True si la création a réussi, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO collection_coherente (id, titre, description) VALUES "
                        "(%(id)s, %(titre)s, %(description)s, %(mangas)s) RETURNING id_collection;",
                        {
                            "id": collection.id,  # Utilisation des attributs de l'objet collection
                            "titre": collection.titre,
                            "description": collection.description,
                        },
                        "INSERT INTO"
                    )
                    res = cursor.fetchone()
#        except Exception as e:
#            logging.info(e)

        created = False
        if res:
            created = True

        return created

#    @log
    def UpdateCoherent(self, collection: CollectionCoherente) -> bool:
        """Mise à jour d'une collection cohérente existante

        Parameters
        ----------
        collection : Collection_coherente
            Objet représentant la collection cohérente avec les nouvelles valeurs

        Returns
        -------
        updated : bool
            True si la mise à jour a réussi, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE collection_coherente SET titre = %(titre)s, "
                        "description = %(description)s, mangas = %(mangas)s "
                        "WHERE id = %(id)s;",
                        {
                            "titre": collection.titre,
                            "description": collection.description,
                            "mangas": collection.mangas,
                            "id": collection.id,
                        },
                    )
                    updated = cursor.rowcount > 0  # rowcount > 0 indique si la mise à jour a affecté des lignes
#        except Exception as e:
#            logging.info(e)
#            updated = False

        return updated

#    @log
    def DeleteCoherent(self, id: int) -> bool:
        """Suppression d'une collection cohérente de la base de données

        Parameters
        ----------
        id : int
            ID de la collection à supprimer

        Returns
        -------
        deleted : bool
            True si la suppression a réussi, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM collection_coherente WHERE id = %(id)s;",
                        {"id": id},
                    )
                    deleted = cursor.rowcount > 0  # rowcount > 0 indique si la suppression a affecté des lignes
#        except Exception as e:
#            logging.info(e)
#            deleted = False

        return deleted

#    @log
    def ReadCoherent(self, id: int) -> CollectionCoherente:
        """Lecture d'une collection cohérente à partir de son ID

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
                        "SELECT * FROM collection_coherente WHERE id = %(id)s;",
                        {"id": id},
                    )
                    res = cursor.fetchone()
                    if res:
                        collection = Collection_coherente(
                            id=res["id"],
                            titre=res["titre"],
                            description=res["description"],
                            mangas=res["mangas"],
                        )
#        except Exception as e:
#            logging.info(e)

        return collection

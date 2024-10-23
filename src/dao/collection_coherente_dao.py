import logging

from utils.singleton import Singleton
#from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.collection_coherente import CollectionCoherente



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
                            "id": collection.id_collection,  # Utilisation des attributs de l'objet collection
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
                    """
                    UPDATE collection_coherente
                    SET titre = %(titre)s, description = %(description)s
                    WHERE id_collection = %(id_collection)s;
                    """,
                    {
                        "titre": collection.titre,
                        "description": collection.description,
                        "id_collection": collection.id,
                    },
                    )
                
                # Suppression des mangas existants pour cette collection dans la table d'association
                    cursor.execute(
                    """
                    DELETE FROM Association_manga_collection_coherente
                    WHERE id_collection_coherente = %(id_collection)s;
                    """,
                    {"id_collection": collection.id},
                )

                # Réinsertion des mangas mis à jour dans la table d'association
                    for manga in collection.mangas:
                    cursor.execute(
                        """
                        INSERT INTO Association_manga_collection_coherente (id_manga, id_collection_coherente)
                        VALUES (%(id_manga)s, %(id_collection_coherente)s);
                        """,
                        {
                            "id_manga": manga.id_manga,
                            "id_collection_coherente": collection.id,
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
                # 1. Supprimer d'abord les associations avec les mangas dans la table d'association
                cursor.execute(
                    """
                    DELETE FROM Association_manga_collection_coherente
                    WHERE id_collection_coherente = %(id)s;
                    """,
                    {"id": id},
                )

                # 2. Supprimer ensuite la collection cohérente
                cursor.execute(
                    """
                    DELETE FROM collection_coherente
                    WHERE id_collection = %(id)s;
                    """,
                    {"id": id},
                )
                
                # Vérifier si la suppression de la collection a bien eu lieu
                deleted = cursor.rowcount > 0  # rowcount > 0 indique si une ligne a été supprimée

#    except Exception as e:
 #       logging.error(f"Erreur lors de la suppression de la collection cohérente : {e}")
  #      deleted = False

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
                # 1. Récupérer les informations de la collection cohérente
                cursor.execute(
                    "SELECT * FROM collection_coherente WHERE id_collection = %(id)s;",
                    {"id": id},
                )
                res = cursor.fetchone()

                # 2. Récupérer les mangas associés via la table d'association
                cursor.execute(
                    """
                    SELECT m.id_manga, m.titre, m.description
                    FROM Association_manga_collection_coherente AS amcc
                    JOIN Manga AS m ON amcc.id_manga = m.id_manga
                    WHERE amcc.id_collection_coherente = %(id)s;
                    """,
                    {"id": id},
                )
                mangas_res = cursor.fetchall()

                # 3. Si la collection est trouvée, construire l'objet CollectionCoherente
                if res:
                    mangas = [
                        Manga(
                            id_manga=manga["id_manga"],
                            titre=manga["titre"],
                            description=manga["description"]
                        ) for manga in mangas_res
                    ]
                    
                    collection = CollectionCoherente(
                        id=res["id_collection"],
                        titre=res["titre"],
                        description=res["description"],
                        mangas=mangas  # Liste d'objets Manga associés à la collection
                    )
                    
#    except Exception as e:
 #       logging.error(f"Erreur lors de la lecture de la collection cohérente : {e}")
  #      collection = None

    return collection

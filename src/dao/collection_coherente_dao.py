import logging

from src.utils.singleton import Singleton
#from utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.collection_coherente import CollectionCoherente



class Collection_coherenteDAO(metaclass=Singleton):
    """Classe DAO pour gérer les collections cohérentes dans la base de données"""

#    @log
    def CreateCoherente(self, collection: CollectionCoherente) -> bool:
        """Création d'une nouvelle collection cohérente dans la base de données

    Parameters
    ----------
    collection : CollectionCoherente
        Objet représentant la collection cohérente

    Returns
    -------
    created : bool
        True si la création a réussi, False sinon
        """
        created = False

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                # 1. Insertion de la collection cohérente et récupération de son ID
                    cursor.execute(
                        "INSERT INTO collection_coherente (titre, description) VALUES "
                        "(%(titre)s, %(description)s) RETURNING id_collection;",
                        {
                            "titre": collection.titre,
                            "description": collection.description,
                        },
                    )
                    res = cursor.fetchone()  # Récupération de l'ID de la collection nouvellement créée

                    if res:
                        id_collection = res["id_collection"]  # ID de la collection créée

                    # 2. Insertion des mangas dans la table d'association
                        for manga in collection.mangas:
                            cursor.execute(
                            """
                                INSERT INTO Association_manga_collection_coherente (id_manga, id_collection_coherente)
                                VALUES (%(id_manga)s, %(id_collection_coherente)s);
                            """,
                                {
                                    "id_manga": manga.id_manga,
                                    "id_collection_coherente": id_collection,  # Utilisation de l'ID récupéré
                                },
                            )
                        created = True  # Si tout s'est bien passé

        except Exception as e:
            logging.error(f"Erreur lors de la création de la collection cohérente : {e}")
            created = False
        
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
                        "id_collection": collection.id_collection,
                        "titre": collection.titre,
                        "description": collection.description,
                    },
                    )

                # Suppression des mangas existants pour cette collection dans la table d'association
                    cursor.execute(
                    """
                    DELETE FROM Association_manga_collection_coherente
                    WHERE id_collection_coherente = %(id_collection)s;
                    """,
                    {"id_collection": collection.id_collection},
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
                            "id_collection_coherente": collection.id_collection,
                        },
                        )
                    updated = cursor.rowcount > 0  # rowcount > 0 indique si la mise à jour a affecté des lignes
        except Exception as e:
            logging.info(e)
            updated = False

        return updated

#    @log
def DeleteCoherent(self, collection: CollectionCoherente) -> bool:
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
                    {"id": collection.id_collection},
                )

                # 2. Supprimer ensuite la collection cohérente
                cursor.execute(
                    """
                    DELETE FROM collection_coherente
                    WHERE id_collection = %(id)s;
                    """,
                    {"id": collection.id_collection},
                )

                # Vérifier si la suppression de la collection a bien eu lieu
                deleted = cursor.rowcount > 0  # rowcount > 0 indique si une ligne a été supprimée

    except Exception as e:
        logging.error(f"Erreur lors de la suppression de la collection cohérente : {e}")
        deleted = False

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

    except Exception as e:
        logging.error(f"Erreur lors de la lecture de la collection cohérente : {e}")
        collection = None

    return collection

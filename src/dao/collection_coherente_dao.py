import logging

from src.utils.singleton import Singleton
from src.utils.log_decorator import log

from src.dao.db_connection import DBConnection

from src.business_object.collection_coherente import CollectionCoherente
from src.business_object.manga import Manga



class CollectionCoherenteDAO(metaclass=Singleton):
    """Classe DAO pour gérer les collections cohérentes dans la base de données"""

    @log
    def create_coherente(self, collection: CollectionCoherente) -> bool: #Assigner utilisateur_id à collection.id_utilisateur
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
                # Vérifier si le titre existe déjà
                    cursor.execute(
                        "SELECT 1 FROM tp.collection_coherente WHERE titre = %(titre)s;",
                        {"titre": collection.titre},
                    )

                    if cursor.fetchall():
                        logging.error(f"Une collection avec le titre '{collection.titre}' existe déjà."
                                      " Réessayez avec un autre titre.")
                        return False  # Empêche la création

                    cursor.execute(
                        "INSERT INTO tp.collection (id_utilisateur) VALUES "
                        "(%(id_utilisateur)s) RETURNING id_collection;",
                        {
                            "id_utilisateur": collection.id_utilisateur,
                        },
                    )
                    res = cursor.fetchone()  # Récupération de l'ID de la collection nouvellement créée

                    if res:
                        collection.id_collection = res["id_collection"]
                        created = True  # Si tout s'est bien passé

                    cursor.execute(
                        "INSERT INTO tp.collection_coherente (id_collection, titre, description) VALUES "
                        "(%(id_collection)s ,%(titre)s, %(description)s);",
                        {
                            "id_collection": collection.id_collection,
                            "titre": collection.titre,
                            "description": collection.description,
                        },
                    )
                    for manga in collection.contenu:
                        cursor.execute(

                        "INSERT INTO tp.Association_manga_collection_coherente (id_manga, id_collection)"
                        "VALUES (%(id_manga)s, %(id_collection)s);",

                            {
                            "id_manga": manga.id_manga,
                            "id_collection": collection.id_collection,  # Utilisation de l'ID récupéré
                            },
                        )
        except Exception as e:
            logging.error(f"Erreur lors de la création de la collection cohérente : {e}")
            created = False

        return created

    @log
    def update_coherente(self, collection: CollectionCoherente) -> bool:
        """Mise à jour d'une collection cohérente existante

        Parameters
        ----------
        collection : Collection_coherente
            Objet représentant la collection cohérente avec les nouvelles
            valeurs à mettre à jour.

        Returns
        -------
        updated : bool
            True si la mise à jour a réussi, False sinon
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT 1
                        FROM tp.collection_coherente
                        WHERE titre = %(titre)s AND id_collection != %(id_collection)s;
                        """,
                        {"titre": collection.titre, "id_collection": collection.id_collection},
                    )
                    if cursor.fetchall():
                        logging.error(
                            f"Une collection avec le titre '{collection.titre}' existe déjà. "
                            "Réessayez avec un autre titre."
                        )
                        return False
                    cursor.execute(
                    """
                    UPDATE tp.collection_coherente
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
                    DELETE FROM tp.association_manga_collection_coherente
                    WHERE id_collection = %(id_collection)s;
                    """,
                    {"id_collection": collection.id_collection},
                )

                # Réinsertion des mangas mis à jour dans la table d'association
                    for manga in collection.contenu:
                        cursor.execute(
                        """
                        INSERT INTO tp.association_manga_collection_coherente (id_manga, id_collection)
                        VALUES (%(id_manga)s, %(id_collection)s);
                        """,
                        {
                            "id_manga": manga.id_manga,
                            "id_collection": collection.id_collection,
                        },
                        )
                    res = cursor.rowcount

        except Exception as e:
            logging.info(e)

        return res == 1

    @log
    def delete_coherente(self, id_collection) -> bool:
        """Suppression d'une collection cohérente de la base de données

        Parameters
        ----------
        id_collection : int
            id de la collection cohérente à supprimer

        Returns
        -------
        deleted : bool
            True si la suppression a réussi, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                    """
                    DELETE FROM tp.avis_collection
                    WHERE id_collection = %(id_collection)s;
                    """,
                    {"id_collection": id_collection},
                )

                # 1. Supprimer d'abord les associations avec les mangas dans la table d'association
                    cursor.execute(
                    """
                    DELETE FROM tp.association_manga_collection_coherente
                    WHERE id_collection = %(id_collection)s;
                    """,
                    {"id_collection": id_collection},
                )

                    # 2. Supprimer ensuite la collection cohérente
                    cursor.execute(
                        """
                        DELETE FROM tp.collection_coherente
                        WHERE id_collection = %(id_collection)s;
                        """,
                        {"id_collection": id_collection},
                    )
                    # 3. Supprimer la collection associée
                    cursor.execute(
                        """
                        DELETE FROM tp.collection
                        WHERE id_collection = %(id_collection)s;
                        """,
                        {"id_collection": id_collection},
                    )
                    deleted = cursor.rowcount > 0
                    # Vérifier si la suppression de la collection a bien eu lieu
              # rowcount > 0 indique si une ligne a été supprimée

        except Exception as e:
            logging.error(f"Erreur lors de la suppression de la collection cohérente : {e}")
            deleted = False

        return deleted

    @log
    def read_coherente(self, titre: int) -> CollectionCoherente:
        """Lecture d'une collection cohérente à partir de son titre

        Parameters
        ----------
        titre : str
            Titre de la collection à lire

        Returns
        -------
        collection : CollectionCoherente
            L'objet CollectionCoherente correspondant au titre en paramètre
        """
        collection = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # 1. Récupérer les informations de la collection cohérente
                    cursor.execute(
                        "SELECT * FROM tp.collection_coherente WHERE titre = %(titre)s;",
                        {"titre": titre},
                    )
                    res1 = cursor.fetchone()

                    # 2. Récupérer l'id de l'utilisateur
                    cursor.execute(
                        "SELECT * FROM tp.collection"
                        " JOIN tp.collection_coherente ON tp.collection.id_collection=tp.collection_coherente.id_collection"
                        " WHERE tp.collection_coherente.titre = %(titre)s;",
                        {"titre": titre},
                    )
                    res2 = cursor.fetchone()

                    # 3. Récupérer les mangas associés via la table d'association
                    cursor.execute(
                        """
                        SELECT tp.manga.titre, tp.manga.id_manga, tp.manga.descript, tp.manga.auteur
                        FROM tp.association_manga_collection_coherente
                        JOIN tp.manga ON tp.association_manga_collection_coherente.id_manga = tp.manga.id_manga
                        JOIN tp.collection_coherente ON tp.association_manga_collection_coherente.id_collection = tp.collection_coherente.id_collection
                        WHERE tp.collection_coherente.titre = %(titre)s;
                        """,
                        {"titre": titre},
                    )
                    mangas_res = cursor.fetchall()

                    # 4. Si la collection est trouvée, construire l'objet CollectionCoherente
                    if mangas_res:
                        contenu = []
                        for manga in mangas_res:
                            new_manga = Manga(
                                id_manga=manga["id_manga"],
                                titre=manga["titre"],
                                descript=manga["descript"],
                                auteur=manga["auteur"]
                                )
                            contenu.append(new_manga)

                        collection = CollectionCoherente(
                            id_collection=res1["id_collection"],
                            id_utilisateur=res2["id_utilisateur"],
                            titre=res1["titre"],
                            description=res1["description"],
                            contenu=contenu  # Liste d'objets Manga associés à la collection
                        )

        except Exception as e:
            logging.error(f"Erreur lors de la lecture de la collection cohérente : {e}")
            collection = None

        return collection

    def recup_collec_coherente_from_id(self, id_utilisateur):
        """Récupérer les collections cohérentes à partir de l'id d'un
        utilisateur.

        Parameters
        ----------
        id_utilisateur : str
            id de l'utilisateur dont on veut voir les collections cohérentes.

        Returns
        -------
        res : List
           Liste de dictionnaires contenant les informations sur les collections
           cohérentes associées à l'utilisateur.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT titre, description, tp.collection.id_collection FROM tp.collection"
                        " JOIN tp.collection_coherente ON tp.collection.id_collection=tp.collection_coherente.id_collection"
                        " WHERE id_utilisateur='%(id_utilisateur)s'",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def recup_id_collec_from_manga_titre(self, titre):
        """
        Renvoie les id de collections parmi lesquels le titre d'un manga
        passé en paramètre est contenu.

        Parameters
        ----------
        titre : str
            Titre du manga dont on veut voir les collections cohérentes le
            contenant.

        Returns
        -------
        res : List
           Liste de dictionnaires contenant les informations sur les collections
           cohérentes contenant le titre de manga passé en paramètre.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT tp.collection_coherente.id_collection FROM tp.association_manga_collection_coherente
                        JOIN tp.collection_coherente ON tp.association_manga_collection_coherente.id_collection=tp.collection_coherente.id_collection
                        JOIN tp.manga ON tp.association_manga_collection_coherente.id_manga=tp.manga.id_manga
                        WHERE tp.manga.titre = %(titre)s;
                        """,
                        {"titre": titre},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        return res

    def recup_infos_from_collec_id(self, id_collection: int):
        """Lecture d'une collection cohérente à partir de son ID

        Parameters
        ----------
        id_collection : int
            ID de la collection à lire

        Returns
        -------
        res : List
           Liste de dictionnaires contenant les informations sur la collection
           cohérente correspondant à l'id passé en paramètre.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # 1. Récupérer les informations de la collection cohérente
                    cursor.execute(
                        """
                        SELECT tp.manga.titre AS titre_manga, tp.utilisateur.pseudo, tp.collection_coherente.titre AS titre_collec, tp.collection_coherente.description FROM tp.collection
                        JOIN tp.collection_coherente ON tp.collection.id_collection=tp.collection_coherente.id_collection
                        JOIN tp.utilisateur ON tp.collection.id_utilisateur=tp.utilisateur.id_utilisateur
                        JOIN tp.association_manga_collection_coherente ON tp.collection_coherente.id_collection=tp.association_manga_collection_coherente.id_collection
                        JOIN tp.manga ON tp.association_manga_collection_coherente.id_manga=tp.manga.id_manga
                        WHERE tp.collection_coherente.id_collection = %(id_collection)s;
                        """,
                        {"id_collection": id_collection},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise
        return res

    def recup_id_collec_from_titre(self, titre: str) -> CollectionCoherente:
        """
        Permet de récupérer l'id d'une collecton cohérente à partir de
        son titre.

        Parameters
        ----------
        titre : str
            Titre de la collection à lire

        Returns
        -------
        res : List
           Liste de dictionnaires contenant les informations sur la collection
           cohérente correspondant au titre passé en paramètre.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # 1. Récupérer les informations de la collection cohérente
                    cursor.execute(
                        """
                        SELECT * from tp.collection_coherente
                        WHERE tp.collection_coherente.titre = %(titre)s;
                        """,
                        {"titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        return res

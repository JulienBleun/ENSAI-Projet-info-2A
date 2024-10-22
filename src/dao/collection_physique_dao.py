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
                        "INSERT INTO manga_physique (id_maga_physique, id_collection, id_manga, dernier_tome_acquis, tomes_manquants, statut) VALUES"
                        "(%(id_maga_physique)s, %(id_collection)s, %(id_manga)s, %(dernier_tome_acquis)s, %(tomes_manquants)s, %(statut)s)"
                        {
                            
                        }
                    )
                    res = cursor.fetchone()
#        except Exception as e:
#            logging.info(e)

        created = False
        if res:
            created = True

        return created

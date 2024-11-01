#TODO Nothing, normally

from utils.log_decorator import log

from business_object.collection_physique import CollectionPhysique
from business_object.manga_physique import MangaPhysique
from dao.collection_physique_dao import CollectionPhysiqueDAO


class CollectionPhysiqueService:
    """Classe contenant les méthodes de service des collections physiques"""

    @log
    def creer_physique(self, id_utilisateur, id_collection, titre,
                       description, contenu: list[MangaPhysique]):

        nouvelle_collection = CollectionPhysique(
            id_utilisateur=id_utilisateur,
            id_collection=id_collection,
            titre=titre,
            description=description,
            contenu=contenu
        )

        return nouvelle_collection if CollectionPhysiqueDAO().CreatePhysique(
               nouvelle_collection) else None

    @log
    def mettre_a_jour_physique(self, collection_modifiée: CollectionPhysique
                               ) -> CollectionPhysique:

        # collection_modifiée doit être une instance de CollectionCoherente.
        # On accède aux informations de la collection associée à son id, puis
        # on les modifie avec les nouvelles infos

        return collection_modifiée if CollectionPhysiqueDAO().UpdatePhysique(
               collection_modifiée) else None

    @log
    def supprimer_physique(self, collection: CollectionPhysique) -> bool:

        return CollectionPhysiqueDAO().DeletePhysique(collection)

    @log
    def consulter_physique(self, id_collection) -> CollectionPhysique:

        return CollectionPhysiqueDAO().ReadPhysique(id_collection)

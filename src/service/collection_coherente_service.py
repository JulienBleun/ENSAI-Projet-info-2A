# TODO Normally nothing

from utils.log_decorator import log

from business_object.collection_coherente import CollectionCoherente
from business_object.manga import Manga
from dao.collection_coherente_dao import Collection_coherenteDAO


class CollectionCoherenteService:
    """Classe contenant les méthodes de service des collections cohérentes"""

    @log
    def creer_coherent(self, id_collection, id_utilisateur, titre, description,
                       contenu: list[Manga]):

        nouvelle_collection = CollectionCoherente(
            id_collection=id_collection,
            id_utilisateur=id_utilisateur,
            titre=titre,
            description=description,
            contenu=contenu
        )

        return nouvelle_collection if Collection_coherenteDAO().CreateCoherente(nouvelle_collection) else None

    @log
    def mettre_a_jour_coherent(self, collection_modifiée: CollectionCoherente
                               ) -> CollectionCoherente:

        # collection_modifiée doit être une instance de CollectionCoherente. On accède aux informations
        # de la collection associée à son id, puis on les modifie avec les nouvelles infos

        return collection_modifiée if Collection_coherenteDAO().UpdateCoherent(collection_modifiée) else None

    @log
    def supprimer_coherent(self, id_collection) -> bool:

        return Collection_coherenteDAO().DeleteCoherent(id_collection)

    @log
    def consulter_coherent(self, id_collection) -> CollectionCoherente:

        return Collection_coherenteDAO().ReadCoherent(id_collection)

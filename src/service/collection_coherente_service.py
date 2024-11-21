# TODO Normally nothing

from src.utils.log_decorator import log

from src.business_object.collection_coherente import CollectionCoherente
from src.business_object.manga import Manga
from src.dao.collection_coherente_dao import CollectionCoherenteDAO


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

        return nouvelle_collection if CollectionCoherenteDAO(
               ).create_coherente(nouvelle_collection) else None

    @log
    def mettre_a_jour_coherent(self, collection_modifiee: CollectionCoherente
                               ) -> CollectionCoherente:

        # collection_modifiée doit être une instance de CollectionCoherente.
        # On accède aux informations de la collection associée à son id, puis
        # on les modifie avec les nouvelles infos

        return collection_modifiee if CollectionCoherenteDAO(
               ).update_coherente(collection_modifiee) else None

    @log
    def supprimer_coherent(self, id_collection) -> bool:

        return CollectionCoherenteDAO().delete_coherente(id_collection)

    @log
    def consulter_coherent(self, titre_collection) -> CollectionCoherente:

        return CollectionCoherenteDAO().read_coherente(titre_collection)

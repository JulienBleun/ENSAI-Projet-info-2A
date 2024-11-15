#TODO Nothing normally

from src.utils.log_decorator import log

from src.business_object.avis_collection import AvisCollection

from src.dao.avis_collection_dao import AvisCollectionDao


class AvisCollectionService:
    """Classe contenant les méthodes de service des avis de collections"""

    @log
    def rediger_avis_collection(self, id_avis, id_utilisateur, commentaire,
                                note, id_collection) -> AvisCollection:

        nouvel_avis_collection = AvisCollection(
                id_avis=id_avis,
                id_utilisateur=id_utilisateur,
                commentaire=commentaire,
                note=note,
                id_collection=id_collection
            )

        return nouvel_avis_collection if AvisCollectionDao(
               ).create_avis_collection(nouvel_avis_collection) else None

    @log
    def mettre_a_jour(self, avis_modifié: AvisCollection) -> AvisCollection:

        # avis_modifié doit être une instance d'AvisCollection. On accède aux
        # informations de l'avis associé à son id, puis on les modifie
        # avec les nouvelles infos.

        return avis_modifié if AvisCollectionDao().update_avis_collection(
               avis_modifié) else None

    @log
    def supprimer(self, avis: AvisCollection) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisCollectionDao().delete_avis_collection(avis)

    @log
    def consulter(self, id_avis) -> AvisCollection:
        return AvisCollectionDao().read_avis(id_avis)

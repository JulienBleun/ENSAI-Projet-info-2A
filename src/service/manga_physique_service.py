#TODO Nothing normally

from src.utils.log_decorator import log

from src.business_object.manga_physique import MangaPhysique
from src.dao.manga_physique_dao import MangaPhysiqueDAO


class MangaPhysiqueService:
    """Classe contenant les méthodes de service des mangas physiques"""

    @log
    def creer_manga_physique(self, id_manga_physique, id_manga,
                             id_collection_physique, dernier_tome_acquis,
                             tomes_manquant, statut) -> MangaPhysique:

        nouveau_manga_physique = MangaPhysique(
                id_manga_physique=id_manga_physique,
                id_manga=id_manga,
                id_collection_physique=id_collection_physique,
                dernier_tome_acquis=dernier_tome_acquis,
                tomes_manquant=tomes_manquant,
                statut=statut,
            )

        return nouveau_manga_physique if MangaPhysiqueDAO().UpdateCoherent(
               nouveau_manga_physique) else None

    @log
    def mettre_a_jour(self, manga_modif: MangaPhysique) -> MangaPhysique:

        # manga_modifié doit être une instance de MangaPhysique. On accède aux
        # informations de l'avis associé à son id, puis on les modifie avec
        # les nouvelles infos

        return manga_modif if MangaPhysiqueDAO().update_manga_physique(
               manga_modif) else None

    @log
    def consulter_manga_physique(self, id_manga_physique) -> MangaPhysique:
        return MangaPhysiqueDAO().read_manga_physique(id_manga_physique)

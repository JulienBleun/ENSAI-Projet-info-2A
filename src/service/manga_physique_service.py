#TODO Nothing normally

from src.utils.log_decorator import log

from src.business_object.manga_physique import MangaPhysique
from src.dao.manga_physique_dao import MangaPhysiqueDAO


class MangaPhysiqueService:
    """Classe contenant les méthodes de service des mangas physiques"""

    @log
    def creer_manga_physique(self, titre_manga,
                             tomes_acquis, statut,
                             id_utilisateur) -> MangaPhysique:

        nouveau_manga_physique = MangaPhysique(
                id_manga_physique=None,
                titre_manga=titre_manga,
                tomes_acquis=tomes_acquis,
                statut=statut,
                id_utilisateur=id_utilisateur,
            )

        return nouveau_manga_physique if MangaPhysiqueDAO(
                                        ).create_manga_physique(
               nouveau_manga_physique) else None

    @log
    def mettre_a_jour(self, id_manga_physique, titre_manga,
                      tomes_acquis, statut, id_utilisateur) -> MangaPhysique:

        manga_physique_modif = MangaPhysique(
                id_manga_physique=id_manga_physique,
                titre_manga=titre_manga,
                tomes_acquis=tomes_acquis,
                statut=statut,
                id_utilisateur=id_utilisateur,
            )
        return manga_physique_modif if MangaPhysiqueDAO().update_manga_physique(
               manga_physique_modif) else None

    @log
    def consulter_manga_physique(self, titre) -> MangaPhysique:
        return MangaPhysiqueDAO().recup_manga_physique_from_titre(titre)

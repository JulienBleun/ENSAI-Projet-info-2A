#TODO Nothing normally

from tabulate import tabulate

from utils.log_decorator import log

from business_object.avis_manga import AvisManga
from dao.avis_manga_dao import AvisMangaDao


class AvisMangaService:
    """Classe contenant les méthodes de service des avis de mangas"""

    @log
    def rédiger_avis_manga(self, id_avis, id_utilisateur, id_manga, contenu,
                           note) -> AvisManga:

        nouvel_avis_manga = AvisManga(
                id_avis=id_avis,
                id_utilisateur=id_utilisateur,
                id_manga=id_manga,
                contenu=contenu,
                note=note,
            )

        return nouvel_avis_manga if AvisMangaDao().create_avis_manga(nouvel_avis_manga) else None

    @log
    def mettre_a_jour(self, avis_modifié: AvisManga) -> AvisManga:

        # avis_modifié doit être une instance d'AvisManga. On accède aux informations
        # de l'avis associé à son id, puis on les modifie avec les nouvelles infos

        return avis_modifié if AvisMangaDao().update_avis_manga(avis_modifié) else None

    @log
    def supprimer(self, avis : AvisManga) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisMangaDao().delete_avis_manga(avis)

    @log
    def consulter(self, id_avis) -> AvisManga:
        return AvisMangaDao().read_avis_manga(id_avis)

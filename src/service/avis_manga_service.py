#TODO Nothing normally

from tabulate import tabulate
from src.utils.singleton import Singleton
from src.utils.log_decorator import log
from src.business_object.avis_manga import AvisManga
from src.dao.avis_manga_dao import AvisMangaDao


class AvisMangaService(metaclass=Singleton):
    """Classe contenant les méthodes de service des avis de mangas"""

    @log
    def rédiger_avis_manga(self, id_manga, id_utilisateur, commentaire,
                           note) -> AvisManga:

        nouvel_avis_manga = AvisManga(
                id_avis=None,  # On ne rentre pas d'id avis comme PostGre s'en occupe
                id_manga=id_manga,
                id_utilisateur=id_utilisateur,
                commentaire=commentaire,
                note=note,
            )

        return nouvel_avis_manga if AvisMangaDao().create_avis_manga(
               nouvel_avis_manga) else None

    @log
    def mettre_a_jour(self, avis_modifié: AvisManga) -> AvisManga:

        return avis_modifié if AvisMangaDao().update_avis_manga(
               avis_modifié) else None

    @log
    def supprimer(self, avis: AvisManga) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisMangaDao().delete_avis_manga(avis)

    @log
    def consulter(self, id_avis) -> AvisManga:

        return AvisMangaDao().read_avis_manga(id_avis)

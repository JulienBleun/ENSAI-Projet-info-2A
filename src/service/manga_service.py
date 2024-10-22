from tabulate import tabulate

from utils.log_decorator import log

from business_object.manga import Manga
from dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service des Mangas"""

    @log
    def consulter_manga(self, id_manga) -> Manga:

        return MangaDao().trouver_par_id(id_manga)

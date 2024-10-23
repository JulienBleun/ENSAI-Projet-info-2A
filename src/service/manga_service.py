#TODO Nothing

from src.utils.log_decorator import log

from src.business_object.manga import Manga
from src.dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service des Mangas"""

    @log
    def consulter_manga(self, id_manga) -> Manga:

        return MangaDao().trouver_par_id(id_manga)

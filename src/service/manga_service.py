#TODO Nothing

<<<<<<< HEAD
from utils.log_decorator import log
=======
from tabulate import tabulate

from src.utils.log_decorator import log
>>>>>>> 60ec57f3723f72405a8845463e46e123ab8dee4f

from src.business_object.manga import Manga
from src.dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service des Mangas"""

    @log
    def consulter_manga(self, id_manga) -> Manga:

        return MangaDao().trouver_par_id(id_manga)
<<<<<<< HEAD
=======


>>>>>>> 60ec57f3723f72405a8845463e46e123ab8dee4f

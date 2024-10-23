#TODO Nothing

from tabulate import tabulate

from src.utils.log_decorator import log

from src.business_object.manga import Manga
from src.dao.manga_dao import MangaDao


class MangaService:
    """Classe contenant les méthodes de service des Mangas"""

    @log
    def consulter_manga(self, id_manga) -> Manga:

<<<<<<< HEAD
        return MangaDao().trouver_par_id(id_manga)


=======
        return MangaDao().read_avis(id_manga)
>>>>>>> 3db1a9481357d47a6a97b24d36a3af611e597f61

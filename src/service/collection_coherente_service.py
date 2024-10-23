from utils.log_decorator import log

from business_object.collection_coherente import CollectionCoherente
from business_object.manga import Manga
from dao.collection_coherente_dao import Collection_coherenteDAO


class CollectionCoherenteService:
    """Classe contenant les méthodes de service des collections cohérentes"""

    @log
    def creer_coherent(self, id, titre, description, liste_mangas: list[Manga])

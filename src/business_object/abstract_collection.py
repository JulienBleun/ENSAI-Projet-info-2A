from abc import ABC


class AbstractCollection(ABC):
    def __init__(self, id_utilisateur: int, id_collection : int):
        self.id_utilisateur = id_utilisateur
        self.id_collection = id_collection

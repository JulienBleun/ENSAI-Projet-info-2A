from abc import ABC, abstractmethod

class AbstractCollection(ABC):
    def __init__(self, id_utilisatuer: int, id_collection : int):
        self.id_utilisateur = id_utilisateur
        self.id_collection = id_collection


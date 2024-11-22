from abc import ABC


class AbstractCollection(ABC):
    """
    Classe abstraite représentant une collection.

    Parametres :
    ------------

    id_collection : int
        Identifiant unique associé à la collection?

    id_utilisateur : int
        Identifiant de l'utilisateur à qui appartient la collection.

    """

    def __init__(self, id_collection, id_utilisateur: int):

        self.id_collection = id_collection
        self.id_utilisateur = id_utilisateur

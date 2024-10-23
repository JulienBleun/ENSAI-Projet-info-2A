from abstract_avis import AbstractAvis
from src.business_object.abstract_avis import AbstractAvis  


class AvisManga(AbstractAvis):
    """
    Classe représentant un avis spécifique à une collection.

    Cette classe hérite de `AbstractAvis` et ajoute un attribut supplémentaire
    pour l'identifiant de la collection à laquelle l'avis est lié.

    Attributs supplémentaires :
    ---------------------------

    id_collection : int
        Identifiant de la collection associée à cet avis.
    """

    def __init__(self,
                 id_avis: int,
                 id_utilisateur: int,
                 commentaire: str,
                 note: int,
                 id_manga: int):

        super().__init__(id_avis, id_utilisateur, commentaire, note)
        self.id_collection = id_manga
        self.id_utilisateur = id_utilisateur


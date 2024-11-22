from src.business_object.abstract_avis import AbstractAvis


class AvisCollection(AbstractAvis):
    """
    Classe représentant un avis spécifique à une collection cohérente.

    Cette classe hérite de `AbstractAvis` et ajoute un attribut supplémentaire
    pour l'identifiant de la collection à laquelle l'avis est lié.

    Attributs supplémentaires :
    ---------------------------

    id_collection : int
        Identifiant unique de la collection associée à cet avis.
    """

    def __init__(self,
                 id_utilisateur: int,
                 commentaire: int,
                 note: int,
                 id_avis: int,
                 id_collection: int):

        if not isinstance(id_collection, int):
            raise TypeError("L'identifiant utilisateur doit être un entier")

        super().__init__(id_utilisateur, commentaire, note, id_avis)
        self.id_collection = id_collection

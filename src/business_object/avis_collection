from abstract_avis import AbstractAvis


class AvisCollection(AbstractAvis):
    """
    Classe représentant un avis spécifique à une collection.

    Cette classe hérite de `AbstractAvis` et ajoute un attribut supplémentaire
    pour l'identifiant de la collection à laquelle l'avis est lié.

    Attributs supplémentaires :
    ---------------------------
    id_collection : int
        Identifiant unique de la collection associée à cet avis.
    """

    def __init__(self,
                 id_avis: int,
                 id_utilisateur: int,
                 commentaire: str,
                 note: int,
                 id_collection: int):

        super().__init__(id_avis, id_utilisateur, commentaire, note)
        self.id_collection = id_collection

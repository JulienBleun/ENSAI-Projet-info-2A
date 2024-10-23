from abc import ABC


class AbstractAvis(ABC):
    """
    Classe abstraite représentant un avis .

    Parametres :
    -----------
    id_avis : int
        Identifiant de l'avis.
    id_utilisateur : int
        Identifiant de l'utilisateur qui a laissé l'avis.
    commentaire : str
        Le texte du commentaire laissé par l'utilisateur.
    note : int
        La note attribuée à l'avis

    """

    def __init__(self,
                 id_avis: int,
                 id_objet_avis: int,
                 commentaire: str,
                 note: int):

        self.id_avis = id_avis
        self.id_objet_avis = id_objet_avis
        self.commentaire = commentaire
        self.note = note

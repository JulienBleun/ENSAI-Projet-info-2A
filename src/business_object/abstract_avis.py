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
                 id_utilisateur: int,
                 commentaire: str,
                 note: int):

        if not isinstance(id_avis, int):
            raise TypeError(
                "L'identifiant de l'avis doit être un entier"
            )

        if not isinstance(id_utilisateur, int):
             raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier"
            )

        if not isinstance(commentaire, str):
            raise TypeError(
                "Le commentaire doit être une chaîne de caractères"
            )

        if not isinstance(note, int):
            raise TypeError(
                "La note doit être un entier "
            )


        self.id_avis = id_avis
        self.id_utilisateur = id_utilisateur
        self.commentaire = commentaire
        self.note = note

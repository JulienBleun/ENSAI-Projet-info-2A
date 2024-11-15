from src.business_object.abstract_avis import AbstractAvis


class AvisManga(AbstractAvis):
    """
    Classe représentant un avis spécifique à un manga.

    Cette classe hérite de `AbstractAvis` et ajoute un attribut supplémentaire
    pour l'identifiant du manga auquel l'avis est lié.

    Attributs supplémentaires :
    ---------------------------

    id_manga : int
        Identifiant de la collection associée à cet avis.
    """

    def __init__(self,
                 id_manga: int,
                 id_avis,
                 id_utilisateur: int,
                 commentaire: str,
                 note: int,
                 ):

        super().__init__(id_utilisateur=id_utilisateur, commentaire=commentaire, note=note, id_avis=id_avis) #Cet ordre précis est IMPORTANT pour écrire dans la base. NE PAS TOUCHER
        self.id_manga = id_manga

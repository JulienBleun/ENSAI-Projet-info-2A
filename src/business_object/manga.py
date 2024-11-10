class Manga():
    """
    Classe pour modéliser un manga.

    Parameters
    ----------

    id_manga : int
        identifiant unique associé au manga.

    titre : str
        Titre du manga.

    auteur : str
        Description du manga.
    """
    def __init__(
            self,
            id_manga: int,
            titre: str,
            auteur: str,
            descript: str):

        self.id_manga = id_manga
        self.titre = titre
        self.auteur = auteur
        self.descript = descript

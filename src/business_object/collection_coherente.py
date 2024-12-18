from src.business_object.manga import Manga


class CollectionCoherente():
    """
    Classe pour modéliser une collection cohérente.

    Parameters :
    ------------

    id_collection : int
        identifiant de la collection cohérente

    id_utilisateur : int
        identifiant de l'utilisateur à qui appartient la collection cohérente

    titre : str
        Titre de la collection.

    description : str
        Description de la collection.

    contenu : list[Manga]
        Contenu de la collection sous forme d'une liste d'instances de
        la classe Manga.

    """
    def __init__(self,
                 id_collection,
                 id_utilisateur,
                 titre,
                 description,
                 contenu: list[Manga]):

        if not isinstance(id_utilisateur, int):
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier"
            )

        if not isinstance(titre, str):
            raise TypeError(
                "Le titre doit être une chaîne de caractère"
            )

        if not isinstance(description, str):
            raise TypeError(
                "La description doit être une chaîne de caractère"
            )
        if not all(isinstance(manga, Manga) for manga in contenu):
            raise TypeError("Tous les éléments de la liste doivent être des instances de la classe Manga")


        self.id_collection = id_collection
        self.id_utilisateur = id_utilisateur
        self.titre = titre
        self.description = description
        self.contenu = contenu

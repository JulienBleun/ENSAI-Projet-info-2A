from src.business_object.abstract_collection import AbstractCollection

from src.business_object.manga_physique import MangaPhysique


class CollectionPhysique(AbstractCollection):
    """
    Classe pour modéliser une collection physique.

    Attributs supplémentaires :
    ---------------------------

    titre : str
        Titre de la collection.

    description : str
        Description de la collection.

    contenu : list[MangaPhysique]
        Contenu de la collection sous forme d'une liste d'instance de
        la classe MangaPhysique.

    """
    def __init__(self,
                 id_utilisateur,
                 id_collection,
                 titre,
                 description,
                 contenu: list[MangaPhysique]):

        if not isinstance(id_utilisateur, int):
            raise TypeError(
                "L'identifiant de l'utilisateur doit être un entier"
            )

        if not isinstance(id_collection, int):
            raise TypeError(
                "L'identifiant de la collection doit être un entier"
            )

        if not isinstance(titre, str):
            raise TypeError(
                "Le titre de la collection doit être une chaîne de caractère"
            )
        
        if not isinstance(description, str):
            raise TypeError(
                "Le description de la collection doit être une chaîne de caractère"
            )

        if not all(isinstance(manga, MangaPhysique) for manga in contenu):
            raise TypeError(
                "Le contenu doit être une liste d'instances de la classe MangaPhysique"
            )

        super().__init__(id_collection, id_utilisateur)
        self.titre = titre
        self.description = description
        self.contenu = contenu

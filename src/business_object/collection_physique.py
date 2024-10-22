from abstract_collection import AbstractCollection


class CollectionPhysique(AbstractCollection):
    """Classe pour modéliser une collection physique.

    Parameters
    ----------


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
                 contenu):

        if not isinstance(id_utilisateur, int):
            raise ValueError(
                "L'identifiant de l'utilisateur doit être un entier"
            )

        if not isinstance(id_collection, int):
            raise ValueError(
                "L'identifiant de la collection doit être un entier"
            )

        if not isinstance(contenu, str):
            raise TypeError(
                "Le contenu doit être une chaîne de caractère"
            )

        super().__init__(id_utilisateur, id_collection)

        self.contenu = contenu
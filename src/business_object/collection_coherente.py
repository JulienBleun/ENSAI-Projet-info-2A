from src.business_object.abstract_collection import AbstractCollection
from src.business_object.abstract_collection import AbstractCollection
from src.business_object.manga import Manga
from src.business_object.abstract_collection import AbstractCollection  


class CollectionCoherente(AbstractCollection):
    """
    Classe pour modéliser une collection cohérente.

    Attributs supllémentaires :
    ---------------------------

    titre : str
        Titre de la collection.

    description : str
        Description de la collection.

    contenu : list[Manga]
        Contenu de la collection sous forme d'une liste d'instance de
        la classe Manga

    """
    def __init__(self,
                 id_collection,
                 id_utilisateur,
                 titre,
                 description,
                 contenu: list[Manga]):

        if not isinstance(id_collection, int):
            raise TypeError(
                "L'identifiant de la collection doit être un entier"
            )

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



        super().__init__(id_collection, id_utilisateur)

        self.titre = titre
        self.description = description
        self.contenu = contenu

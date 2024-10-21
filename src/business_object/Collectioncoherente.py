class Collectioncoherente:
    """Classe pour modéliser une collection cohérente.

    Parameters
    ----------
    id_utilisateur : int
        Identifiant de l'utilisateur.

    titre : str
        Titre de la collection.

    description : str
        Description de la collection.

    contenu : str
        Contenu de la collection

    """
    def __init__(self, id_utilisateur, titre, description, contenu):

       if not isinstance(id_utilisateur, int):
            raise ValueError(
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

        if not isinstance(contenu, str):
            raise TypeError(
                "Le contenu doit être une chaîne de caractère"
            )

        self.id_utilisateur = id_utilisatuer
        self.titre = titre
        self.description = description
        self.contenu = contenu

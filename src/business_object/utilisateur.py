

class utilisateur():
    """
    Classe représentant l' utilisateur.

    Parametres :
    ------------

    id : int
        L'identifiant unique associé à l'utilisateur.

    nom : str

    prenom : str

    pseudo : str

    email : str

    mot_de_passe : str
    """

    def __init__(self, id: int, nom: str, prenom: str,
                 pseudo: str,
                 email: str, mot_de_passe: str
                 ):

        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mot_de_passe = mot_de_passe

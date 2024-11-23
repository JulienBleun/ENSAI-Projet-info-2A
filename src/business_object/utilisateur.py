

class Utilisateur:
    """
    Classe représentant un utilisateur de l'application

    Parameters :
    ------------
    id_utilisateur : int
        L'identifiant unique associé à l'utilisateur.
    nom : str
        Le nom de l'utilisateur.
    prenom : str
        Le prénom de l'utilisateur.
    pseudo : str
        Le pseudo de l'utilisateur.
    email : str
        L'email de l'utilisateur.
    mdp : str
        Le mot de passe de l'utilisateur.
    """
    def __init__(self, nom: str, prenom: str, pseudo: str, email: str, mdp: str, id_utilisateur=None):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mdp = mdp

class Utilisateur:
    """
    Classe représentant l'utilisateur.

    Paramètres :
    ------------

    id_utilisateur : int
        L'identifiant unique associé à l'utilisateur.

    nom : str
        Nom de l'utilisateur.

    prenom : str
        Prénom de l'utilisateur.

    pseudo : str
        Pseudo de l'utilisateur.

    email : str
        Adresse email de l'utilisateur.

    mdp : str
        Mot de passe haché de l'utilisateur.

    sel : bytes
        Sel utilisé pour hacher le mot de passe.
    """

    def __init__(self, nom: str, prenom: str,
                 pseudo: str, email: str, 
                 mdp: str, sel: bytes = None, 
                 id_utilisateur: int = None):
        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mdp = mdp
        self.sel = sel  # Ajout du sel

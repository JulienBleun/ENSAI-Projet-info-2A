

class Utilisateur():
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

    def __init__(self, nom: str, prenom: str,
                 pseudo: str,
                 email: str, mdp: str, id_utilisateur=None
                 ):

        self.id_utilisateur = id_utilisateur
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.mdp = mdp

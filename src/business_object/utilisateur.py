

class utilisateur():
    """Classe représentant l' utilisateur.

    Attributs :
    -----------
    id_avis : int
        L'identifiant unique de l'avis.
        """

    def __init__(self, id: int, prenom: str,
                 nom_utilisateur: str,
                 email: str, mot_de_passe: str
                 ):

        self.id = id
        self.nom_utisateur = nom_utilisateur
        self.email = email
        self.mot_de_passe = mot_de_passe
        
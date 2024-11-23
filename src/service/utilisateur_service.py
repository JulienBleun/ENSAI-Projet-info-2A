import re
from src.utils.log_decorator import log
from src.utils.singleton import Singleton
from src.utils.mdp_utils import hasher_mot_de_passe  # Assurez-vous que cette fonction génère aussi le sel
from src.business_object.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao


class UtilisateurService(metaclass=Singleton):
    """Classe contenant les méthodes de service de l'utilisateur."""
    @log
    def inscription(self, nom, prenom, pseudo, email, mdp):
        """
        Inscrit un nouvel utilisateur en vérifiant les conditions d'inscription.

        Parameters :
        ------------
        nom : str
            Nom de l'utilisateur

        prenom : str
           Prénom de l'utilisateur

        pseudo : str
            Pseudo de l'utilisateur

        email : str
           Email de l'utilisateur

        mdp : str
            Mot de passe de l'utilisateur

        Returns :
        ----------
        utilisateur : Utilisateur
            Instance d'utilisateur créée si l'inscription a réussi sinon None
        """
        # Vérification des conditions
        valide, message = self.verifier_conditions_inscription(nom, prenom, pseudo, email, mdp)
        if not valide:
            raise ValueError(f"Inscription échouée : {message}")
         # Hachage du mot de passe et génération du sel
        mot_de_passe_hashe, sel = hasher_mot_de_passe(mdp)
        # Conversion du sel en hexadécimal pour stockage dans la base de données
        sel_hex = sel.hex()
        # Création de l'utilisateur
        nouveau_utilisateur = Utilisateur(
            nom=nom,
            prenom=prenom,
            pseudo=pseudo,
            email=email,
            mdp=mot_de_passe_hashe,  # Mot de passe haché
            sel=sel_hex  # Sel en format hexadécimal
        )
        # Ajout de l'utilisateur dans la base de données
        if UtilisateurDao().add_utilisateur(nouveau_utilisateur):
            return nouveau_utilisateur
        else:
            return None

    @staticmethod
    def verifier_conditions_inscription(nom, prenom, pseudo, email, mdp):
        """
        Vérifie les conditions pour les informations d'inscription.

        Returns :
        ----------
        tuple : (bool, str)
            - bool : True si toutes les conditions sont respectées, sinon False.
            - str : Message d'erreur ou "OK".
        """
        if len(nom) < 2:
            return False, "Le nom doit comporter au moins 2 caractères."
        if len(prenom) < 2:
            return False, "Le prénom doit comporter au moins 2 caractères."
        if len(pseudo) < 3:
            return False, "Le pseudo doit comporter au moins 3 caractères."
        if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
            return False, "L'adresse email n'est pas valide."
        if len(mdp) < 8:
            return False, "Le mot de passe doit comporter au moins 8 caractères."
        return True, "OK"

    @log
    def suppression(self, id_utilisateur):
        if UtilisateurDao().delete_utilisateur(id_utilisateur):
            return True
        else:
            return False

    @log
    def se_connecter(self, pseudo: str, mdp: str):
        utilisateur = UtilisateurDao().se_connecter(pseudo, mdp)
        if utilisateur:
            return utilisateur
        else:
            return None

    @log
    def mettre_a_jour_utilisateur(self, id_utilisateur, nouveau_pseudo,
                                  nouveau_mdp) -> bool:
        if UtilisateurDao().update_utilisateur(id_utilisateur, nouveau_pseudo,
                                               nouveau_mdp):
            return True
        else:
            return False

    @log
    def consulter_profil(self, pseudo: str):
        return UtilisateurDao().read_profil(pseudo)

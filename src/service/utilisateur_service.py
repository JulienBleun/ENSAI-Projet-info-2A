import re
from src.utils.log_decorator import log
from src.utils.singleton import Singleton

from src.business_object.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao

class UtilisateurService(metaclass=Singleton):
    """Classe contenant les méthodes de service de l'utilisateur."""

    @log
    def inscription(self, nom, prenom, pseudo, email, mdp):
        """
        Inscrit un nouvel utilisateur en vérifiant les conditions d'inscription.

        Retourne :
        ----------
        Utilisateur : l'utilisateur créé si l'inscription réussit, sinon None.
        """
        # Vérification des conditions
        valide, message = self.verifier_conditions_inscription(nom, prenom, pseudo, email, mdp)
        if not valide:
            raise ValueError(f"Inscription échouée : {message}")

        nouveau_utilisateur = Utilisateur(
            nom=nom,
            prenom=prenom,
            pseudo=pseudo,
            email=email,
            mdp=mdp
        )
        return nouveau_utilisateur if UtilisateurDao().add_utilisateur(nouveau_utilisateur) else None

    @staticmethod
    def verifier_conditions_inscription(nom, prenom, pseudo, email, mdp):
        """
        Vérifie les conditions pour les informations d'inscription.

        Retourne :
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

        def desinscription(self, utilisateur):

        def connexion(self, pseudo, md):

        def deconnexion(self, pseudo):

        def consulter_profil(self, id):

        def mettre_a_jour(self, utilisateur):

import getpass

from src.dao.utilisateur_dao import UtilisateurDao
from src.business_object.utilisateur import Utilisateur
import src.utils.mdp_utils as mdp_utils

def inscription_view():
    """Fonction pour gérer l'inscription d'un utilisateur."""
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    pseudo = input("Entrez votre pseudo : ")
    email = input("Entrez votre email : ")
    mdp = mdp_utils.hasher_mot_de_passe(getpass.getpass("Entrez votre mot de passe : "))

    utilisateur = Utilisateur(nom, prenom, pseudo, email, mdp)

    try:
        if UtilisateurDao().add_utilisateur(utilisateur):
            print("Inscription réussie !")
        else:
            print("L'inscription a échoué. Veuillez réessayer.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'inscription : {e}")

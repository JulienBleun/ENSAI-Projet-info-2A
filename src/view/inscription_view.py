import getpass

from src.service.utilisateur_service import UtilisateurService

def inscription_view():
    """Fonction pour gérer l'inscription d'un utilisateur."""
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    pseudo = input("Entrez votre pseudo : ")
    email = input("Entrez votre email : ")
    mdp = getpass.getpass("Entrez votre mot de passe : ")

    utilisateur = UtilisateurService().inscription(nom, prenom, pseudo, email, mdp)
    if utilisateur:
        print(f"Inscription réussie ! Bienvenue sur la meilleure Mangathèque {pseudo}")
    else:
        print("L'inscription a échoué. Veuillez réessayer.")

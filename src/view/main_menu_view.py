# Importer les fonctions 

# from  xxx import deconnexion

from src.view.inscription_view import inscription_view
from src.view.connexion_view import connexion_view


def afficher_menu_principal():
    """Affiche le menu principal et gère le choix de l'utilisateur."""
    while True:
        print("\n--- Menu Principal ---")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Quitter l'application")

        choix = input("Entrez votre choix (1, 2 ou 3) : ")

        if choix == '1':
            utilisateur = inscription_view()  # Fonction d'inscription
            if utilisateur:
                return utilisateur  # Retourne l'utilisateur inscrit pour le menu utilisateur
        elif choix == '2':
            utilisateur = connexion_view()  # Fonction de connexion
            if utilisateur:
                return utilisateur  # Retourne l'utilisateur connecté pour le menu utilisateur
        elif choix == '3':
            print("Merci d'avoir utilisé l'application. Au revoir!")
            exit()  # Quitte l'application
        else:
            print("Choix invalide. Veuillez réessayer.")

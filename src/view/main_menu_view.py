# Importer les fonctions

# from  xxx import deconnexion
import sys
from src.view.inscription_view import inscription_view
from src.view.connexion_view import connexion_view


def afficher_menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Quitter l'application")

        choix = input("Entrez votre choix (1, 2 ou 3) : ")

        if choix == '1':
            inscription_view()  # Fonction de création de compte
        elif choix == '2':
            utilisateur = connexion_view()  # Fonction de connexion
            if utilisateur:
                return utilisateur
        elif choix == '3':
            print("Merci d'avoir utilisé l'application. Au revoir!")
            sys.exit()
        else:
            print("Choix invalide. Veuillez réessayer.")

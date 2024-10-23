# Importer fonctions 
from src.dao.utilisateur_dao import UtilisateurDao
from src.dao.utilisateur_dao import se_connecter


def afficher_menu_principal():
    while True:
        print("\nBienvenue sur MangaLover, l'application de gestion de collection de mangas !")
        print("1. Créer un compte")
        print("2. Se connecter")
        print("3. Quitter")
        choix = input("Veuillez choisir une option : ")

        if choix == '1':
            creer_compte()
        elif choix == '2':
            connexion()
        elif choix == '3':
            print("Au revoir !")
            break
        else:
            print("Option invalide, veuillez réessayer.")

def creer_compte():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    nom_utilisateur = input("Nom d'utilisateur : ")
    email = input("Email : ")
    mot_de_passe = input("Mot de passe : ")

    UtilisateurDao().add_Utilisateur(nom, prenom, nom_utilisateur, email, mot_de_passe)

def connexion():
    nom_utilisateur = input("Nom d'utilisateur : ")
    mot_de_passe = input("Mot de passe : ")
    
    UtilisateurDao().se_connecter(nom_utilisateur, mot_de_passe)

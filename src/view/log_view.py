# Importer fonctions 


def afficher_menu_principal():
    while True:
        print("\nBienvenue dans l'application de gestion de collection de mangas !")
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
    username = input("Nom d'utilisateur : ")
    email = input("Email : ")
    mot_de_passe = input("Mot de passe : ")

    creer_compte_controller(nom, prenom, username, email, mot_de_passe)

def connexion():
    username = input("Nom d'utilisateur : ")
    mot_de_passe = input("Mot de passe : ")
    connexion_controller(username, mot_de_passe)

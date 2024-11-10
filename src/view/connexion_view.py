import getpass

from src.dao.utilisateur_dao import UtilisateurDao

def connexion_view():
    """Fonction pour gérer la connexion d'un utilisateur."""
    pseudo = input("Entrez votre pseudo : ")
    mdp = getpass.getpass("Entrez votre mot de passe : ")

    try:
        utilisateur = UtilisateurDao().se_connecter(pseudo, mdp)
        if utilisateur is not None:
            print(f"Connexion réussie ! Bienvenue {utilisateur.pseudo} : id {utilisateur.id_utilisateur}")
            return utilisateur  # You can return the user object for further use
        else:
            print("Connexion échouée. Pseudo ou mot de passe incorrect.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la connexion : {e}")

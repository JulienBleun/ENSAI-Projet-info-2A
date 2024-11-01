from src.dao.utilisateur_dao import UtilisateurDao

def connexion_view():
    """Fonction pour gérer la connexion d'un utilisateur."""
    pseudo = input("Entrez votre pseudo : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    utilisateur_dao = UtilisateurDao()

    try:
        utilisateur = utilisateur_dao.se_connecter(pseudo, mot_de_passe)
        if utilisateur:
            print("Connexion réussie !")
            return utilisateur  # You can return the user object for further use
        else:
            print("Connexion échouée. Pseudo ou mot de passe incorrect.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la connexion : {e}")

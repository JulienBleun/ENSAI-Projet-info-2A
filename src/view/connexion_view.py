import maskpass

from src.service.utilisateur_service import UtilisateurService


def connexion_view():
    """Fonction pour gérer la connexion d'un utilisateur."""
    pseudo = input("Entrez votre pseudo : ")
    mdp = maskpass.askpass(prompt="Entrez votre mot de passe : ")

    try:
        u = UtilisateurService()
        utilisateur = u.se_connecter(pseudo, mdp)
        if utilisateur is not None:
            print(f"\n\nConnexion réussie ! Heureux de vous revoir {utilisateur.pseudo}")
            return utilisateur  # Retourne l'utilisateur connecté
        else:
            print("\n\nConnexion échouée. Pseudo ou mot de passe incorrect.")
            return None
    except Exception as e:
        print(f"Une erreur est survenue lors de la connexion : {e}")
        return None

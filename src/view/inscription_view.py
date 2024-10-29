from src.dao.utilisateur_dao import UtilisateurDao

def inscription_view():
    """Fonction pour gérer l'inscription d'un utilisateur."""
    nom = input("Entrez votre nom : ")
    prenom = input("Entrez votre prénom : ")
    pseudo = input("Entrez votre pseudo : ")
    email = input("Entrez votre email : ")
    mot_de_passe = input("Entrez votre mot de passe : ")

    utilisateur_dao = UtilisateurDao()

    try:
        if utilisateur_dao.add_utilisateur(nom, prenom, pseudo, email, mot_de_passe):
            print("Inscription réussie !")
        else:
            print("L'inscription a échoué. Veuillez réessayer.")
    except Exception as e:
        print(f"Une erreur est survenue lors de l'inscription : {e}")

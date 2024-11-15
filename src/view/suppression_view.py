from src.dao.utilisateur_dao import UtilisateurDao

def suppression_view(utilisateur_id):
    """
    Vue pour supprimer un compte utilisateur.

    Paramètres :
    ------------
    utilisateur_id : int
        L'identifiant unique de l'utilisateur à supprimer.
    """
    print("\n--- Suppression du compte ---")
    
    # Confirmation de la suppression
    confirmation = input("Êtes-vous sûr de vouloir supprimer votre compte ? (oui/non) : ").strip().lower()
    if confirmation != "oui":
        print("Suppression annulée.")
        return

    # Suppression via le DAO
    dao = UtilisateurDao()
    try:
        succes = dao.delete_utilisateur(utilisateur_id)
        if succes:
            print("Compte supprimé avec succès.")
        else:
            print("Échec de la suppression du compte. Veuillez réessayer.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression : {e}")

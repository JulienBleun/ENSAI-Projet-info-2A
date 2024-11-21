from src.service.utilisateur_service import UtilisateurService

def suppression_view(id_utilisateur):
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

    # Suppression via la classe service
    try:
        succes = UtilisateurService().delete_utilisateur(id_utilisateur)
        if succes:
            print("Compte supprimé avec succès.")
        else:
            print("Échec de la suppression du compte. Veuillez réessayer.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression : {e}")

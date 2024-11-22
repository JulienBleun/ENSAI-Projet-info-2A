from src.service.utilisateur_service import UtilisateurService
from src.view.main_menu_view import afficher_menu_principal


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
    if confirmation == "non":
        print("Suppression annulée.")
        return

    # Suppression via la classe service
    try:
        succes = UtilisateurService().suppression(utilisateur_id)
        if succes:
            print("Compte supprimé avec succès. Retour au menu principal.")
            afficher_menu_principal()
        else:
            print("Échec de la suppression du compte. Veuillez réessayer.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la suppression : {e}")

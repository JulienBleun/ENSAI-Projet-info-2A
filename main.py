from src.view.main_menu_view import afficher_menu_principal
from src.view.menu_utilisateur_view import afficher_menu_utilisateur



def run_app():
    """Lance l'application et gère le flux entre le menu principal et le menu utilisateur."""
    utilisateur_connecte = None  # Aucun utilisateur connecté au début

    while True:
        if utilisateur_connecte is None:
            # Affichage du menu principal si aucun utilisateur n'est connecté
            utilisateur_connecte = afficher_menu_principal()

        if utilisateur_connecte is not None:
            # Affichage du menu utilisateur si un utilisateur est connecté
            afficher_menu_utilisateur(utilisateur_connecte.id_utilisateur)
            utilisateur_connecte = None  # Une fois l'utilisateur déconnecté, on revient au menu principal

if __name__ == "__main__":
    run_app()

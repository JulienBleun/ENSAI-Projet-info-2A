from src.view.main_menu_view import afficher_menu_principal

if __name__ == "__main__":
    try:
        afficher_menu_principal()  # Affiche le menu principal pour l'utilisateur
    except Exception as e:
        print(f"Une erreur est survenue lors de l'initialisation : {e}")



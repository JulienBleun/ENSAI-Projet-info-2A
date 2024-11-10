from src.view.main_menu_view import afficher_menu_principal
from src.utils.reset_database import ResetDatabase

if __name__ == "__main__":
    ResetDatabase().lancer()
    #ResetDatabase().populer()
    ResetDatabase().pop_manga_from_api()
    #try:
     #   afficher_menu_principal()
    #except Exception as e:
     #   print(f"Une erreur est survenue lors de l'initialisation : {e}")

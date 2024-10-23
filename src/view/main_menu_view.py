# Importer les fonctions 
from src.view.manga_view import rechercher_manga_view
from src.view.collection_view import afficher_mes_collections_view
from src.view.modif_view import modifier_compte_view
# from  xxx import deconnexion


def afficher_menu_principal(utilisateur_id):
    print("\n=== Menu Principal ===")
    print("1. Rechercher un manga")
    print("2. Accéder à mes collections")
    print("3. Modifier mon compte")
    print("4. Déconnexion")
    
    choix = input("Choisissez une option : ")

    options = {
        "1": lambda: rechercher_manga_view(utilisateur_id),
        "2": lambda: afficher_mes_collections_view(utilisateur_id),
        "3": lambda: modifier_compte_view(utilisateur_id),
        # "4": deconnexion  # Pas besoin de l'utilisateur_id pour déconnexion
    }

    action = options.get(choix)
    if action:
        action()
    else:
        print("Choix invalide.")
        afficher_menu_principal(utilisateur_id)

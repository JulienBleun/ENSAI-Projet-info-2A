from src.view.manga_view import trouver_manga_par_titre, trouver_manga_par_id
from src.view.collection_view import creer_collection_coherente_view, creer_collection_physique_view
from src.view.modifier_compte_view import modifier_compte_view
from src.view.deconnexion_view import deconnexion_view


def afficher_menu_utilisateur(utilisateur_id):
    """Affiche le menu de l'utilisateur après la connexion."""
    while True:
        print("\n--- Menu Utilisateur ---")
        print("1. Chercher un manga par titre")
        print("2. Créer une collection cohérente")
        print("3. Créer une collection physique")
        print("4. Modifier mon compte")
        print("5. Se déconnecter")
        print("6. Chercher un manga par id")

        choix = input("Choisissez une option : ")

        if choix == '1':
            trouver_manga_par_titre()
        elif choix == '2':
            creer_collection_coherente_view(utilisateur_id)
        elif choix == '3':
            creer_collection_physique_view(utilisateur_id)
        elif choix == '4':
            modifier_compte_view(utilisateur_id)
        elif choix == '6':
            trouver_manga_par_id()
        elif choix == '5':
            print("Déconnexion réussie.")
            deconnexion_view()
            break  # Quitte le menu utilisateur et retourne au menu principal
        else:
            print("Choix invalide. Veuillez réessayer.")

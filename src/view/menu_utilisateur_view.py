from src.view.manga_view import trouver_manga_par_titre, trouver_manga_par_id
from src.view.collection_view import creer_collection_coherente_view, creer_collection_physique_view, modifier_collection_coherente_view, supprimer_collection_coherente_view, afficher_collection_coherente_par_titre_view
from src.view.modifier_compte_view import modifier_compte_view
from src.view.deconnexion_view import deconnexion_view
from src.view.avis_view import modifier_avis_manga, supprimer_avis_manga, afficher_avis_manga
from src.view.suppression_view import suppression_view



def afficher_menu_utilisateur(utilisateur_id):
    """Affiche le menu de l'utilisateur après la connexion."""
    while True:
        print("\n--- Menu Utilisateur ---")
        print("1. Chercher un manga par titre")
        print("2. Chercher un manga par id")
        print("3. Créer une collection physique")
        print("4. Créer une collection cohérente")
        print("5. Afficher les avis d'un manga")
        print("6. Modifier un avis de manga")
        print("7. Supprimer un avis de manga")
        print("8. Modifier mon compte")
        print("9. Se déconnecter")
        print("10. Supprimer mon compte")
        print("13. Chercher une collection cohérente par titre")




        choix = input("Choisissez une option : ")

        if choix == '1':
            trouver_manga_par_titre(utilisateur_id)
        elif choix == '2':
            trouver_manga_par_id(utilisateur_id)
        elif choix == '3':
            creer_collection_physique_view(utilisateur_id)
        elif choix == '8':
            modifier_compte_view(utilisateur_id)
        elif choix == '4':
            creer_collection_coherente_view(utilisateur_id)
        elif choix == '6':
            modifier_avis_manga(utilisateur_id)
        elif choix == '7':
            supprimer_avis_manga(utilisateur_id)
        elif choix == '5':
            afficher_avis_manga()
        elif choix == '9':
            print("Déconnexion réussie.")
            deconnexion_view()
            break  # Quitte le menu utilisateur et retourne au menu principal
        elif choix == '10':
            suppression_view(utilisateur_id)
        elif choix == '11':
            modifier_collection_coherente_view(utilisateur_id)
        elif choix == '12':
            supprimer_collection_coherente_view(utilisateur_id)
        elif choix == '13':
            afficher_collection_coherente_par_titre_view()
        else:
            print("Choix invalide. Veuillez réessayer.")

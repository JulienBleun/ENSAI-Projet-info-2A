from src.view.manga_view import trouver_manga_par_titre, trouver_manga_par_id
from src.view.collection_coherente_view import creer_collection_coherente_view, modifier_collection_coherente_view, supprimer_collection_coherente_view, afficher_collection_coherente_par_titre_view, afficher_collection_coherente_par_titre__manga_view, afficher_toutes_les_collections_coherentes, afficher_collections_autre_utilisateur
from src.view.modifier_compte_view import modifier_compte_view
from src.view.deconnexion_view import deconnexion_view
from src.view.avis_view import modifier_avis_manga, supprimer_avis_manga, afficher_avis_manga, creer_avis_manga, afficher_avis_manga_utilisateur, afficher_avis_manga_autre_utilisateur
from src.view.suppression_view import suppression_view
from src.view.manga_physique_view import ajouter_manga_physique_view, modifier_manga_physique_view, afficher_collection_physique_view, supprimer_manga_physique_view, afficher_collection_physique_autre_utilisateur
from src.view.avis_collection_view import creer_avis_collection, modifier_avis_collection, supprimer_avis_collection, afficher_tous_les_avis_par_titre_collec, afficher_tous_mes_avis_collec, afficher_avis_collection_autre_utilisateur


def afficher_menu_utilisateur(utilisateur_id):
    """Affiche le menu de l'utilisateur après la connexion."""
    while True:
        print("\n--- Menu Utilisateur ---")
        print("1. Gérer les mangas")
        print("2. Gérer les avis")
        print("3. Gérer les collections")
        print("4. Trouver des informations sur un autre utilisateur")
        print("5. Modifier / supprimer mon compte")
        print("6. Se déconnecter")

        choix = input("Choisissez une option : ")

        if choix == '1':

            print("1. Chercher un manga par titre")
            print("2. Chercher un manga par id")
            print("3 : Ajouter un manga sous forme physique")
            print("4 : Modifier un de mes manga sous forme physique")
            print("5 : Supprimer un de mes manga sous forme physique")
            choix1 = input("Choisissez une option : ")
            if choix1 == '1':
                trouver_manga_par_titre(utilisateur_id)
            elif choix1 == '2':
                trouver_manga_par_id(utilisateur_id)
            elif choix1 == '3':
                ajouter_manga_physique_view(utilisateur_id)
            elif choix1 == '4':
                modifier_manga_physique_view(utilisateur_id)
            elif choix1 == '5':
                supprimer_manga_physique_view(utilisateur_id)
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == '2':
            print("1. Ajouter un avis de manga")
            print("2. Modifier un avis de manga")
            print("3. Supprimer un de mes avis de manga")
            print("4. Afficher tous les avis d'un certain manga")
            print("5. Afficher tous mes avis de manga")
            print("6. Ajouter un avis de collection cohérente")
            print("7. Modifier un avis de collection cohérente")
            print("8. Supprimer un avis de collection cohérente")
            print("9. Afficher tous les avis d'une certaine collection cohérente")
            print("10. Afficher tous mes avis de collection cohérente")
            choix2 = input("Choisissez une option : ")
            if choix2 == '1':
                creer_avis_manga(utilisateur_id)
            elif choix2 == '2':
                modifier_avis_manga(utilisateur_id)
            elif choix2 == '3':
                supprimer_avis_manga(utilisateur_id)
            elif choix2 == '4':
                afficher_avis_manga()
            elif choix2 == '5':
                afficher_avis_manga_utilisateur(utilisateur_id)
            elif choix2 == '6':
                creer_avis_collection(utilisateur_id)
            elif choix2 == '7':
                modifier_avis_collection(utilisateur_id)
            elif choix2 == '8':
                supprimer_avis_collection(utilisateur_id)
            elif choix2 == '9':
                afficher_tous_les_avis_par_titre_collec()
            elif choix2 == '10':
                afficher_tous_mes_avis_collec(utilisateur_id)
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == '3':
            print("1. Créer une collection cohérente")
            print("2. Modifier une collection cohérente")
            print("3. Supprimer une collection cohérente")
            print("4. Afficher toutes les collections cohérentes contenant "
                  "un certain manga")
            print("5. Afficher une collection cohérente à partir de son titre")
            print("6 : Afficher toutes mes collections cohérentes")
            print("7 : Afficher ma collection physique")

            choix3 = input("Choisissez une option : ")
            if choix3 == '1':
                creer_collection_coherente_view(utilisateur_id)
            elif choix3 == '2':
                modifier_collection_coherente_view(utilisateur_id)
            elif choix3 == '3':
                supprimer_collection_coherente_view(utilisateur_id)
            elif choix3 == '4':
                afficher_collection_coherente_par_titre__manga_view()
            elif choix3 == '5':
                afficher_collection_coherente_par_titre_view()
            elif choix3 == '6':
                afficher_toutes_les_collections_coherentes(utilisateur_id)
            elif choix3 == '7':
                afficher_collection_physique_view(utilisateur_id)
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == '4':
            print("1. Afficher les avis de mangas d'un autre utilisateur")
            print("2. Afficher les avis de collections d'un autre utilisateur")
            print("3. Afficher les collections cohérentes d'un utilisateur")
            print("4. Afficher la collection physique d'un utilisateur")
            choix4 = input("Choisissez une option : ")
            if choix4 == '1':
                afficher_avis_manga_autre_utilisateur()
            elif choix4 == '2':
                afficher_avis_collection_autre_utilisateur()
            elif choix4 == '3':
                afficher_collections_autre_utilisateur()
            elif choix4 == '4':
                afficher_collection_physique_autre_utilisateur()
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == '5':
            print("1. Modifier mon compte")
            print("2. Supprimer mon compte")
            choix5 = input("Choisissez une option : ")
            if choix5 == '1':
                modifier_compte_view(utilisateur_id)
            elif choix5 == '2':
                suppression_view(utilisateur_id)
            else:
                print("Choix invalide. Veuillez réessayer.")

        elif choix == '6':
            print("Déconnexion réussie.")
            deconnexion_view()
            break  # Quitte le menu utilisateur et retourne au menu principal

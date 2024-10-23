# Importer
from src.dao.manga_dao import MangaDao
from src.view.avis_view import ajouter_avis_view, lire_avis_view
from src.view.collection_view import ajouter_a_collection_view



def rechercher_manga_view(utilisateur_id):
    titre = input("Entrez le titre du manga : ")
    # Utiliser l'instance de MangaDao
    mangas = MangaDao.rechercher_manga_par_titre(titre)

    if mangas:
        for i, manga in enumerate(mangas, 1):
            print(f"{i}. {manga['title']} (ID: {manga['mal_id']})")

        choix = int(input("Choisissez un manga par numéro : "))
        manga_id = mangas[choix - 1]['mal_id']

        # Proposer le choix d'ajouter un avis, ajouter à une collection, ou lire les avis
        print("\nQue souhaitez-vous faire avec ce manga ?")
        print("1. Ajouter un avis")
        print("2. Ajouter à une collection")
        print("3. Lire les avis des autres utilisateurs")
        action = input("Choisissez une action (1, 2 ou 3) : ")

        if action == '1':
            ajouter_avis_view(utilisateur_id, manga_id)  # Appel pour ajouter un avis
        elif action == '2':
            ajouter_a_collection_view(utilisateur_id, manga_id)  # Appel pour ajouter à une collection
        elif action == '3':
            lire_avis_view(manga_id)  # Appel pour lire les avis des autres utilisateurs
        else:
            print("Action invalide.")
    else:
        print("Aucun manga trouvé.")

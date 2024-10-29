from src.dao.avis_manga_dao import AvisMangaDao
from src.utils.log_decorator import log





def ajouter_avis_view(utilisateur_id, manga_id):
    contenu = input("Entrez votre avis : ").strip()  # Stripping whitespace
    if contenu:  # Simple check to ensure content isn't empty
        AvisMangaDao().create_avis_manga(utilisateur_id, manga_id, contenu)  
        print("Avis ajouté avec succès.")
    else:
        print("L'avis ne peut pas être vide.")


def lire_avis_view(manga_id):
    avis = AvisMangaDao().read_avis_manga(manga_id)

    if avis:
        print("\nAvis pour ce manga :")
        for i, review in enumerate(avis, 1):
            print(f"{i}. Utilisateur: {review['utilisateur']}, Avis: {review['contenu']}")
    else:
        print("Aucun avis trouvé pour ce manga.")


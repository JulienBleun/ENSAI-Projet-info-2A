from src.dao.manga_dao import MangaDao

def trouver_manga_par_titre(titre):
    manga_dao = MangaDao()
    manga = manga_dao.rechercher_manga_par_titre(titre)

    if manga:
        print(f"Manga trouvé : {manga['titre']}")
        # Affichez plus d'informations sur le manga si nécessaire
    else:
        print("Aucun manga trouvé avec ce titre.")

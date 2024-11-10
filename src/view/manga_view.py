from src.dao.manga_dao import MangaDao
from src.dao.avis_manga_dao import AvisMangaDao  # Assure-toi d'utiliser la classe DAO appropriée
from src.business_object.avis_manga import AvisManga  # Assure-toi d'utiliser le bon modèle

def trouver_manga_par_titre(titre=None, utilisateur_id=None):
    """Recherche et affiche un manga par son titre, avec possibilité de laisser un avis."""
    if not titre:
        titre = input("Entrez le titre du manga que vous recherchez : ").strip()

    manga_dao = MangaDao()
    
    try:
        manga = manga_dao.rechercher_manga_par_titre(titre)
        if manga:
            print(f"Manga trouvé : {manga['titre']}")
            print(f"Auteur : {manga.get('auteur', 'Inconnu')}")
            print(f"Genre : {manga.get('genre', 'Inconnu')}")
            print(f"Note : {manga.get('note', 'Non disponible')}")
            print(f"Description : {manga.get('description', 'Non disponible')}")

            # Affichage des avis existants pour ce manga
            afficher_avis(manga['id_manga'])

            # Option de laisser un avis
            if utilisateur_id:  # Vérifie que l'utilisateur est connecté
                laisser_avis = input("Souhaitez-vous laisser un avis ? (o/n) : ").lower()
                if laisser_avis == 'o':
                    commentaire = input("Entrez votre commentaire : ")
                    note = input("Entrez votre note (de 0 à 10) : ")
                    try:
                        # Crée un objet AvisManga et l'ajoute via le DAO
                        avis = AvisManga(
                            id_utilisateur=utilisateur_id,
                            id_manga=manga['id_manga'],
                            commentaire=commentaire,
                            note=int(note)
                        )

                        avis_dao = AvisMangaDao()
                        if avis_dao.create_avis_manga(avis):
                            print("Votre avis a été ajouté avec succès !")
                        else:
                            print("Erreur lors de l'ajout de votre avis.")
                    except ValueError:
                        print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
        else:
            print("Aucun manga trouvé avec ce titre.")
    except Exception as e:
        print(f"Une erreur est survenue lors de la recherche : {e}")


def afficher_avis(manga_id):
    """Affiche les avis pour un manga donné."""
    avis_dao = AvisMangaDao()
    avis_list = avis_dao.read_avis_manga(manga_id)

    if avis_list:
        print("Avis pour ce manga :")
        for avis in avis_list:
            print(f"Utilisateur {avis.id_utilisateur} - Note : {avis.note}/10")
            print(f"Avis : {avis.commentaire}")
            print("----")
    else:
        print("Aucun avis pour ce manga.")

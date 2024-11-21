from src.service.manga_physique_service import MangaPhysiqueService
from src.business_object.collection_physique import CollectionPhysique
from src.service.collection_physique_service import CollectionPhysiqueService

def creer_collection_physique_view(utilisateur_id):

    titre = input("Comment souhaitez-vous appeler votre collection cohérente ? ")
    description = input("Quelle description voulez-vous donner ?")
    nombre = int(input('Combien de mangas physiques voulez-vous dans votre '
                       'collection ? '))
    contenu = []
    for i in range(nombre):
        nom = input(f"Quel est le nom du {i+1}ème manga que vous souhaitez inclure à la collection ? ")
        manga = MangaPhysiqueService().consulter_manga_physique(nom)
        contenu.append(manga)

    if CollectionPhysiqueService().creer_physique(id_collection=None,
                                                    id_utilisateur=utilisateur_id,
                                                    titre=titre,
                                                    description=description,
                                                    contenu=contenu):
        print("Collection physique créée avec succès.")
    else:
        print("Erreur lors de la création de la collection.")

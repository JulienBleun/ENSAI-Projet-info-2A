from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.dao.collection_physique_dao import CollectionPhysiqueDAO
from src.business_object.collection_coherente import CollectionCoherente
from src.service.manga_service import MangaService

def creer_collection_coherente_view(utilisateur_id):
    titre = input("Titre de la collection cohérente : ")
    description = input("Description : ")
    nombre = int(input('Combien de mangas voulez-vous dans votre collection ? '))
    contenu = []
    for i in range(nombre):
        nom = input(f"Quel est le nom du {i+1}ème manga que vous souhaitez inclure à la collection ?")
        manga = MangaService().consulter_manga_par_titre(nom)
        contenu.append(manga)
    collection = CollectionCoherente(id_collection=None, id_utilisateur=utilisateur_id, titre=titre, description=description, contenu=contenu)
    if CollectionCoherenteDAO().CreateCoherente(collection):
        print("Collection cohérente créée avec succès.")
    else:
        print("Erreur lors de la création de la collection.")

def creer_collection_physique_view(utilisateur_id):
    titre = input("Titre de la collection physique : ")
    dernier_tome_acquis = int(input("Dernier tome acquis : "))
    status = input("Statut de la série ('reading' ou 'dropped') : ")

    if CollectionPhysiqueDAO().CreatePhysique(titre, dernier_tome_acquis, status, utilisateur_id):
        print("Collection physique créée avec succès.")
    else:
        print("Erreur lors de la création de la collection.")

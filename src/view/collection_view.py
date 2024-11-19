from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.dao.collection_physique_dao import CollectionPhysiqueDAO
from src.business_object.collection_coherente import CollectionCoherente
from src.service.collection_coherente_service import CollectionCoherenteService
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

def modifier_collection_coherente_view(utilisateur_id):

    collection = CollectionCoherenteDAO().recup_collec_coherente_from_id(utilisateur_id)
    if collection:
        print('0 : Retour au menu principal')
        for i in range(0, len(collection)):
            print(f'{i+1} : {collection[i]["titre"]} avec la description : {collection[i]["id_collection"]}')

        numero_collection = int(input('Quel avis de manga souhaitez-vous modifier ? '))
        if numero_collection == 0:
            return
        else:
            collection_choisie = collection[numero_collection-1]
            titre = input(' Quel est votre nouveau titre ? ')
            description = input(' Quelle est votre nouvelle description ? ')
            nombre = int(input(' Combien de mangas voulez-vous dans votre nouvelle collection ? '))
            contenu = []
            for i in range(nombre):
                nom = input(f" Quel est le nom du {i+1}ème manga que vous souhaitez inclure à la collection ?")
                manga = MangaService().consulter_manga_par_titre(nom)
                contenu.append(manga)
            collection_coherente_a_modifier = CollectionCoherente(
                id_utilisateur=utilisateur_id,
                id_collection=int(collection_choisie['id_collection']),
                titre=titre,
                description=description, contenu=contenu)
            collection_modif = CollectionCoherenteService(
            ).mettre_a_jour_coherent(collection_coherente_a_modifier)
            if collection_modif:
                print(' Votre collection cohérente a bien été modifié')
            else:
                print(" Vous n'avez pas encore de collection cohérente")


def supprimer_collection_coherente_view(utilisateur_id):

    collection = CollectionCoherenteDAO().recup_collec_coherente_from_id(utilisateur_id)

    if collection:
        print('0 : Retour au menu principal')
        for i in range(0, len(collection)):
            print(f'{i+1} : {collection[i]["titre"]} avec la description : {collection[i]["description"]}')

        numero_collection = int(input('Quelle collection cohérente souhaitez-vous supprimer ? '))
        if numero_collection == 0:
            return
        else:
            collection_choisie = collection[numero_collection-1]
            id_a_supprimer = collection_choisie['id_collection']
            collection_sup = CollectionCoherenteService().supprimer_coherent(id_a_supprimer)
            if collection_sup:
                print('\n\nVotre collection cohérente a bien été supprimée')

    else:
        print("\n\nVous n'avez pas encore créé de collection cohérente")


#def afficher_collection_coherente_par_titre_view(): #Constuire l'affichage de collections selon un titre de manga qui serait dans la collection
 #   pass
        #SELECT tp.manga.titre, tp.collection_coherente.titre, tp.collection_coherente.description FROM tp.association_manga_collection_coherente
   # JOIN tp.collection_coherente ON tp.association_manga_collection_coherente.id_collection=tp.collection_coherente.id_collection
    #JOIN tp.manga ON tp.association_manga_collection_coherente.id_manga=tp.manga.id_manga
    #WHERE tp.manga.titre = 'One Piece'

def afficher_collection_coherente_par_titre_view():
    titre = input("Quel est le titre de la collection cohérente que vous cherchez ? : ")

    collection = CollectionCoherenteService().consulter_coherent(titre)

    if collection:
        print(f"Collection trouvée ! La collection '{titre}' contient les mangas :")

        for manga in collection.contenu:  # Itération directe sur les objets Manga
            print(manga.titre)

        print(f"Sa description est : '{collection.description}'")

    else:
        print(f"Aucune collection trouvée pour le titre '{titre}'.")


def creer_collection_physique_view(utilisateur_id):
    titre = input(" Titre de la collection physique : ")
    dernier_tome_acquis = int(input(" Dernier tome acquis : "))
    status = input(" Statut de la série ('reading' ou 'dropped') : ")

    if CollectionPhysiqueDAO().CreatePhysique(titre, dernier_tome_acquis, status, utilisateur_id):
        print(" Collection physique créée avec succès.")
    else:
        print(" Erreur lors de la création de la collection.")

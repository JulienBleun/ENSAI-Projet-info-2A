from src.dao.collection_physique_dao import CollectionPhysiqueDAO
from src.business_object.collection_physique import CollectionPhysique
from src.service.collection_physique_service import CollectionPhysiqueService
from src.service.manga_service import MangaService
from src.business_object.manga_physique import MangaPhysique

def creer_collection_physique_view(utilisateur_id):
    titre = input("Comment souhaitez-vous appeler votre collection physique ? ")
    description = input("Quelle description voulez-vous donner ?")
    nombre = int(input('Combien de mangas voulez-vous dans votre collection physique ? '))
    contenu = []
    for i in range(nombre):
        nom = input(f"Quel est le nom du {i+1}ème manga que vous souhaitez inclure à la collection ? ")
        manga = MangaService().consulter_manga_par_titre(nom)
        dernier_tome = int(input(f"Quel est le dernier tome acquis de '{manga.titre}' ? "))
        tomes_manquants = int(input(f"Combien de tomes manquent pour '{manga.titre}' ? "))
        statut = input(f"Quel est le statut de '{manga.titre}' ? (ex: possédé, en cours, etc.) ")
        
        manga_physique = MangaPhysique(
            id_manga_physique=None,
            id_manga=manga.id_manga,
            id_collection_physique=None,
            dernier_tome_acquis=dernier_tome,
            tomes_manquants=tomes_manquants,
            statut=statut
        )
        contenu.append(manga_physique)

    collection_physique = CollectionPhysique(id_collection=None, id_utilisateur=utilisateur_id, titre=titre, description=description, contenu=contenu)
    if CollectionPhysiqueDAO().create_physique(collection_physique):
        print("Collection physique créée avec succès.")
    else:
        print("Erreur lors de la création de la collection physique.")

def modifier_collection_physique_view(utilisateur_id):

    collection = CollectionPhysiqueDAO().read_physique(utilisateur_id)
    if collection:
        print('0 : Retour au menu principal')
        for i in range(0, len(collection)):
            print(f"{i+1} : '{collection[i]['titre']}' avec la description : '{collection[i]['description']}'")

        numero_collection = int(input(' Quelle collection physique souhaitez-vous modifier ? '))
        if numero_collection == 0:
            return
        else:
            collection_choisie = collection[numero_collection-1]
            titre = input(' Quel est votre nouveau titre ? ')
            description = input(' Quelle est votre nouvelle description ? ')
            nombre = int(input(' Combien de mangas voulez-vous dans votre nouvelle collection physique ? '))
            contenu = []
            for i in range(nombre):
                nom = input(f" Quel est le nom du {i+1}ème manga que vous souhaitez inclure à la collection ? ")
                manga = MangaService().consulter_manga_par_titre(nom)
                dernier_tome = int(input(f"Quel est le dernier tome acquis de '{manga.titre}' ? "))
                tomes_manquants = int(input(f"Combien de tomes manquent pour '{manga.titre}' ? "))
                statut = input(f"Quel est le statut de '{manga.titre}' ? (ex: possédé, en cours, etc.) ")

                manga_physique = MangaPhysique(
                    id_manga_physique=None,  # L'ID sera généré par la base de données
                    id_manga=manga.id,
                    id_collection_physique=None,  # L'ID de la collection sera défini plus tard
                    dernier_tome_acquis=dernier_tome,
                    tomes_manquants=tomes_manquants,
                    statut=statut
                )
                contenu.append(manga_physique)

            collection_physique_a_modifier = CollectionPhysique(
                id_utilisateur=utilisateur_id,
                id_collection=int(collection_choisie['id_collection']),
                titre=titre,
                description=description,
                contenu=contenu
            )
            collection_modif = CollectionPhysiqueService().mettre_a_jour_physique(collection_physique_a_modifier)
            if collection_modif:
                print('Votre collection physique a bien été modifiée.')
            else:
                print("Vous n'avez pas encore de collection physique.")

def supprimer_collection_physique_view(utilisateur_id):

    collection = CollectionPhysiqueDAO().read_physique(utilisateur_id)

    if collection:
        print('0 : Retour au menu principal')
        for i in range(0, len(collection)):
            print(f'{i+1} : {collection[i]["titre"]} avec la description : {collection[i]["description"]}')

        numero_collection = int(input('Quelle collection physique souhaitez-vous supprimer ? '))
        if numero_collection == 0:
            return
        else:
            collection_choisie = collection[numero_collection-1]
            id_a_supprimer = collection_choisie['id_collection']
            collection_sup = CollectionPhysiqueService().supprimer_physique(id_a_supprimer)
            if collection_sup:
                print('Votre collection physique a bien été supprimée.')
    else:
        print("Vous n'avez pas encore créé de collection physique.")

def afficher_collection_physique_par_titre_view():
    titre = input("Quel est le titre de la collection physique que vous cherchez ? ")

    collection = CollectionPhysiqueService().consulter_physique(titre)

    if collection:
        print(f"Collection trouvée ! La collection '{titre}' contient les mangas :")

        for manga in collection.contenu:  # Itération directe sur les objets MangaPhysique
            print(manga.titre_manga)

        print(f"Sa description est : '{collection.description}'")
    else:
        print(f"Aucune collection trouvée pour le titre '{titre}'.")

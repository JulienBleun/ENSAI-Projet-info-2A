from src.service.collection_coherente_service import CollectionCoherenteService
from src.service.avis_collection_service import AvisCollectionService
from src.dao.avis_collection_dao import AvisCollectionDao



def creer_avis_collection(utilisateur_id):

    titre = input("Entrez le titre de la collection cohérente"
                  " dont vous souhaitez écrire un avis : ")
    try:
        collection = CollectionCoherenteService().consulter_coherent(titre)
        if collection:
            try:
                id_collection = collection.id_collection
                commentaire = input("Entrez votre commentaire : ")
                note = input("Entrez votre note (de 0 à 10) : ")
                collec = AvisCollectionService().mettre_a_jour(
                                    id_utilisateur=utilisateur_id,
                                    commentaire=commentaire,
                                    note=int(note),
                                    id_collection=id_collection
                                )
                if collec:
                    print("Votre avis a été ajouté avec succès !")
                else:
                    print("Erreur lors de l'ajout de votre avis : Vous avez "
                          "déjà écrit un avis sur cette collection.")
            except ValueError:
                print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
        else:
            print("\n\nCette collection cohérente n'est malheureusement pas "
                  "dans notre base de données. Réessayez.")

    except Exception as e:
        print(f"Une erreur est survenue lors de la recherche : {e}")


def modifier_avis_collection(utilisateur_id):

    avis = AvisCollectionDao().recup_avis_collec_from_id(utilisateur_id)

    if avis:
        print('0 : Retour au menu principal')
        for i in range(0, len(avis)):
            print(f'{i+1} : ' + 'Modifier avis de ' + avis[i]['titre'])
        numero_avis = int(input('Quel avis de collection souhaitez-vous modifier ? '))
        if numero_avis == 0:
            return
        else:
            avis_choisi = avis[numero_avis-1]
            commentaire = input('Quel est votre nouveau commentaire ? ')
            note = int(input('Quelle est votre nouvelle note ? '))
            print(avis_choisi['id_collection'])
            avis_a_modifier = AvisCollectionService().mettre_a_jour(
                id_utilisateur=utilisateur_id,
                id_avis=avis_choisi['id_avis'],
                id_collection=avis_choisi['id_collection'],
                commentaire=commentaire,
                note=note)
            if avis_a_modifier:
                print('Votre avis a bien été modifié')


def supprimer_avis_collection(utilisateur_id):

    avis = AvisCollectionDao().recup_avis_collec_from_id(utilisateur_id)

    if avis:
        print('0 : Retour au menu principal')
        for i in range(0, len(avis)):
            print(f'{i+1} : ' + 'Supprimer avis de ' + avis[i]['titre'])
        numero_avis = int(input('Quel avis de collection souhaitez-vous supprimer ? '))
        if numero_avis == 0:
            return
        else:
            avis_choisi = avis[numero_avis-1]

            avis_suppr = AvisCollectionService().supprimer(avis_choisi['id_avis'])
            if avis_suppr:
                print('Votre avis a bien été supprimé')

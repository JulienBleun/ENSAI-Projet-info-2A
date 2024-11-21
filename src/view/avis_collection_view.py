from src.service.collection_coherente_service import CollectionCoherenteService
from src.service.avis_collection_service import AvisCollectionService


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
                collec = AvisCollectionService().rediger_avis_collection(
                                    id_utilisateur=utilisateur_id,
                                    commentaire=commentaire,
                                    note=int(note),
                                    id_collection=id_collection
                                )
                if collec:
                    print("Votre avis a été ajouté avec succès !")
                else:
                    print("Erreur lors de l'ajout de votre avis.")
            except ValueError:
                print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
        else:
            print("\n\nCette collection cohérente n'est malheureusement pas "
                  "dans notre base de données. Réessayez.")

    except Exception as e:
        print(f"Une erreur est survenue lors de la recherche : {e}")

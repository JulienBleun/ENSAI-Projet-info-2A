from src.service.collection_coherente_service import CollectionCoherenteService
from src.service.avis_collection_service import AvisCollectionService
from src.dao.avis_collection_dao import AvisCollectionDao
from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.dao.utilisateur_dao import UtilisateurDao
from src.utils.singleton import Singleton


class AvisCollectionView(metaclass=Singleton):

    def creer_avis_collection(self, utilisateur_id):

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
                        print("Erreur lors de l'ajout de votre avis : Vous avez "
                            "déjà écrit un avis sur cette collection.")
                except ValueError:
                    print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
            else:
                print("\n\nCette collection cohérente n'est malheureusement pas "
                    "dans notre base de données. Réessayez.")

        except Exception as e:
            print(f"Une erreur est survenue lors de la recherche : {e}")

    def modifier_avis_collection(self, utilisateur_id):

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
                avis_a_modifier = AvisCollectionService().mettre_a_jour(
                    id_utilisateur=utilisateur_id,
                    id_avis=avis_choisi['id_avis'],
                    id_collection=avis_choisi['id_collection'],
                    commentaire=commentaire,
                    note=note)
                if avis_a_modifier:
                    print('Votre avis a bien été modifié')
        else:
            print("\n\n Vous n'avez pas encore rédigé d'avis de collection")

    def supprimer_avis_collection(self, utilisateur_id):

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
        else:
            print("\n\n Vous n'avez pas encore rédigé d'avis de collection")

    def afficher_tous_les_avis_par_titre_collec(self):

        titre = input("De quelle collection cohérente voulez-vous voir les avis ?")
        id_collection = CollectionCoherenteDAO().recup_id_collec_from_titre(
                        titre)
        if id_collection is not None:
            id = id_collection['id_collection']
            avis_collection = AvisCollectionDao().recup_avis_collec_from_id_collec(id)
            if avis_collection:
                somme = 0
                print(f"La collection {titre} possède les avis suivants :")
                for i in range(0, len(avis_collection)):
                    print(f"Avis {i+1} : {avis_collection[i]['pseudo']} a noté cette"
                        f" collection {avis_collection[i]['note']} sur 10 et a "
                        f"mis le commentaire '{avis_collection[i]['commentaire']}' ")
                    somme += int(avis_collection[i]['note'])
                moyenne = somme/len(avis_collection)
                print(f"\n\n Nos utilisateurs ont en moyenne mis la note de {moyenne} "
                    "à cette collection")
            else:
                print("\n\n Aucun avis de collection ne correspond à ces informations")
        else:
            print("\n\n Aucun avis de collection ne correspond à ces informations")

    def afficher_tous_mes_avis_collec(self, utilisateur_id):

        avis = AvisCollectionDao().recup_avis_collec_from_id(utilisateur_id)

        if avis:
            print('Voici tous vos différents avis de collections cohérentes :')
            for i in range(0, len(avis)):
                print(f"Avis {i+1} : Vous avez noté la collection cohérente "
                    f"'{avis[i]['titre']}' {avis[i]['note']} sur 10 et "
                    f"vous avez mis le commentaire '{avis[i]['commentaire']}'")
        else:
            print("\n\n Vous n'avez pas encore rédigé d'avis de collection")

    def afficher_avis_collection_autre_utilisateur(self):

        pseudo = input("De quel pseudo souhaitez-vous voir les avis de collections"
                    " cohérentes ? ")
        id_autre_utilisateur = UtilisateurDao().read_profil(pseudo)
        id_recherche = int(id_autre_utilisateur['id_utilisateur'])

        avis = AvisCollectionDao().recup_avis_collec_from_id(id_recherche)
        if avis:
            print(f"\n Voici les différents avis de collections cohérentes de "
                f"{pseudo} ")
            for i in range(0, len(avis)):
                print(f"{i+1} : {avis[i]['titre']} : {pseudo} a mis la note de"
                    f" {avis[i]['note']} sur 10 avec le commentaire "
                    f"'{avis[i]['commentaire']}'")
        else:
            print("\n\n Aucun avis de collection ne correspond à ces informations")

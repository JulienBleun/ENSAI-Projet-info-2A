from src.service.manga_physique_service import MangaPhysiqueService
from src.utils.singleton import Singleton
from src.service.utilisateur_service import UtilisateurService


class MangaPhysiqueView(metaclass=Singleton):

    def ajouter_manga_physique_view(self, utilisateur_id):

        titre_manga = input('À partir de quel manga voulez-vous créer un '
                            'manga physique ? ')

        nb_tomes = int(input('Combien de tomes de ce manga possédez-vous au total ? '))
        tomes_acquis = []
        for i in range(nb_tomes):
            tome = input(f"Quel est le numéro du {i+1} tome de {titre_manga} que "
                        "vous possédez physiquement ? ")
            tomes_acquis.append(tome)
        statut = input("Est-ce que vous lisez ce manga en ce moment ?"
                    " Si oui 'Reading' sinon 'Dropped'")

        manga_physique = MangaPhysiqueService().creer_manga_physique(
            titre_manga=titre_manga,
            tomes_acquis=tomes_acquis,
            statut=statut,
            id_utilisateur=utilisateur_id)
        if manga_physique:
            print('Votre manga physique a été enregistré.')
        else:
            print("Erreur lors de la création de votre manga physique")

    def modifier_manga_physique_view(self, utilisateur_id):

        manga = MangaPhysiqueService().recup_manga_physique_from_id(utilisateur_id)
        # On récupère tous les mangas physiques de l'utilisateur connecté
        if manga:
            print("Voici vos mangas physiques : ")
            print('0 : Retour au menu principal')
            for i in range(0, len(manga)):
                print(f'{i+1} : ' + manga[i]['titre_manga'])
            numero_manga = int(input('Quel manga physique souhaitez-vous modifier ? '))
            if numero_manga == 0:
                return
            else:
                manga_choisi = manga[numero_manga-1]

                print(f"Voici les différents tomes du manga {manga_choisi['titre_manga']}"
                    " que vous possédiez aux dernières nouvelles :")

                tomes_acquis_str = manga_choisi['tomes_acquis']
                tomes_acquis = [int(x) for x in tomes_acquis_str.strip("{}").split(",")]
                for tome in tomes_acquis:
                    print(f"Tome {tome}")

                choix = input("Voulez-vous ajouter un ou plusieurs tomes ? (o/n)")
                if choix == 'o':
                    choix2 = int(input("Combien voulez-vous en ajouter ?"))
                    for i in range(choix2):
                        tome_ajout = int(input(f" Quel est le {i+1} ème tome que vous souhaitez ajouter au manga physique ? "))
                        tomes_acquis.append(tome_ajout)

                choix_bis = input("Voulez-vous supprimer un ou plusieurs tomes ? (o/n)") # Dans le cas où l'utilisateur aurait perdu un tome par exemple
                if choix_bis == 'o':
                    choix_bis2 = int(input("Combien voulez-vous en supprimer ?"))
                    for i in range(choix_bis2):
                        tome_suppr = int(input(f" Quel est le {i+1} ème tome que vous souhaitez supprimer du manga physique ? "))
                        tomes_acquis.remove(tome_suppr)

                statut = input("Est-ce que vous lisez encore ce manga ? "
                            "Si oui 'Reading' sinon 'Dropped'  ? ")

                manga_physique = MangaPhysiqueService().mettre_a_jour(
                    id_manga_physique=manga_choisi['id_manga_physique'],
                    titre_manga=manga_choisi['titre_manga'],
                    tomes_acquis=tomes_acquis,
                    statut=statut,
                    id_utilisateur=utilisateur_id)

                if manga_physique:
                    print('Votre manga physique a bien été modifié.')
        else:
            print("Vous n'avez pas encore de manga physique. Retour au menu principal")

    def afficher_collection_physique_view(self, utilisateur_id):

        manga = MangaPhysiqueService().recup_manga_physique_from_id(utilisateur_id)
        # On récupère tous les mangas physiques de l'utilisateur connecté
        if manga:
            print('0 : Retour au menu principal')
            print("Voici votre collection de mangas physiques : ")
            for i in range(0, len(manga)):
                print(f"{i+1} : {manga[i]['titre_manga']} avec le statut :"
                      f" '{manga[i]['statut']}'")
            numero_manga = int(input('Quel manga physique souhaitez-vous afficher ? '))
            if numero_manga == 0:
                return
            else:
                manga_choisi = manga[numero_manga-1]

                print(f"Voici les différents tomes du manga {manga_choisi['titre_manga']}"
                    " que vous possédiez aux dernières nouvelles :")

                tomes_acquis_str = manga_choisi['tomes_acquis']
                tomes_acquis = [int(x) for x in tomes_acquis_str.strip("{}").split(",")]
                for tome in tomes_acquis:
                    print(f"Tome {tome}")
        else:
            print("Vous n'avez pas encore de manga physique. Retour au menu principal")

    def supprimer_manga_physique_view(self, utilisateur_id):

        manga = MangaPhysiqueService().recup_manga_physique_from_id(utilisateur_id)
        # On récupère tous les mangas physiques de l'utilisateur connecté
        if manga:
            print("Voici vos mangas physiques : ")
            print('0 : Retour au menu principal')
            for i in range(0, len(manga)):
                print(f'{i+1} : ' + manga[i]['titre_manga'])
            numero_manga = int(input('Quel manga physique souhaitez-vous supprimer ? '))
            if numero_manga == 0:
                return
            else:
                manga_choisi = manga[numero_manga-1]
                id_supprime = int(manga_choisi['id_manga_physique'])
                manga_supprime = MangaPhysiqueService().supprimer_manga_physique(id_supprime)

                if manga_supprime:
                    print('Votre manga physique bien été supprimé.')
        else:
            print("Vous n'avez pas encore de manga physique. Retour au menu principal")

    def afficher_collection_physique_autre_utilisateur(self):

        pseudo = input("De quel pseudo souhaitez-vous voir les avis de manga ? ")
        id_autre_utilisateur = UtilisateurService().consulter_profil(pseudo)
        id_recherche = int(id_autre_utilisateur['id_utilisateur'])
        manga = MangaPhysiqueService().recup_manga_physique_from_id(id_recherche)
        # On récupère tous les mangas physiques de l'utilisateur cherché
        if manga:
            print(f"Voici la collection de mangas physiques de {pseudo}: ")
            for i in range(0, len(manga)):
                print(f'{i+1} : ' + manga[i]['titre_manga'])
            numero_manga = int(input('Quel manga physique souhaitez-vous afficher ? '))
            if numero_manga == 0:
                return
            else:
                manga_choisi = manga[numero_manga-1]

                print(f"Voici les différents tomes du manga {manga_choisi['titre_manga']}"
                    f" que {pseudo} possédait aux dernières nouvelles :")

                tomes_acquis_str = manga_choisi['tomes_acquis']
                tomes_acquis = [int(x) for x in tomes_acquis_str.strip("{}").split(",")]
                for tome in tomes_acquis:
                    print(f"Tome {tome}")

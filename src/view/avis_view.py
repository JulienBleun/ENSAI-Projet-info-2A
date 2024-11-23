from src.service.avis_manga_service import AvisMangaService
from src.business_object.avis_manga import AvisManga
from src.service.manga_service import MangaService
from src.service.utilisateur_service import UtilisateurService
from src.utils.singleton import Singleton


class AvisView(metaclass=Singleton):

    def creer_avis_manga(self, utilisateur_id):

        titre = input("Entrez le titre du manga dont vous souhaitez écrire un"
                      " avis : ")

        try:
            manga = MangaService().consulter_manga_par_titre(titre)
            if manga:
                if utilisateur_id:
                    try:  # Vérifie que l'utilisateur est connecté
                        commentaire = input("Entrez votre commentaire : ")
                        note = input("Entrez votre note (de 0 à 10) : ")
                        avis = AvisMangaService().rédiger_avis_manga(
                                        id_utilisateur=utilisateur_id,
                                        id_manga=int(manga.id_manga),
                                        commentaire=commentaire,
                                        note=int(note)
                                    )
                        if avis:
                            print("Votre avis a été ajouté avec succès !")
                        else:
                            print("Erreur lors de l'ajout de votre avis : Vous"
                                  " avez déjà écrit un avis sur ce manga.")
                    except ValueError:
                        print("Veuillez entrer une note valide (un nombre"
                              "entier entre 0 et 10).")
            else:
                print("\n\nCe manga n'est malheureusement pas dans notre base "
                      "de données. Réessayez.")

        except Exception as e:
            print(f"Une erreur est survenue lors de la recherche : {e}")

    def modifier_avis_manga(self, utilisateur_id):

        avis = AvisMangaService().recup_avis_from_id(utilisateur_id)

        if avis:
            print('0 : Retour au menu principal')
            for i in range(0, len(avis)):
                print(f'{i+1} : ' + avis[i]['titre'])

            numero_avis = int(input('Quel avis de manga souhaitez-vous modifier ? '))
            if numero_avis == 0:
                return
            else:
                manga_choisi = avis[numero_avis-1]
                commentaire = input('Quel est votre nouveau commentaire ? ')
                note = input('Quelle est votre nouvelle note ? ')
                avis_a_modifier = AvisManga(id_utilisateur=utilisateur_id,
                                            id_manga=manga_choisi['id_manga'],
                                            commentaire=commentaire,
                                            note=note, id_avis=manga_choisi['id_avis'])
                avis_modif = AvisMangaService().mettre_a_jour(avis_a_modifier)
                if avis_modif:
                    print('Votre avis a bien été modifié')

        else:
            print("\n\nVous n'avez pas encore rédigé d'avis de manga")

    def supprimer_avis_manga(self, utilisateur_id):

        avis = AvisMangaService().recup_avis_from_id(utilisateur_id)

        if avis:
            print('0 : Retour au menu principal')
            for i in range(0, len(avis)):
                print(f'{i+1} : ' + avis[i]['titre'])

            numero_avis = int(input('\n\nQuel avis de manga souhaitez-vous supprimer ? '))
            if numero_avis == 0:
                return
            else:
                manga_choisi = avis[numero_avis-1]
                avis_a_supprimer = AvisManga(id_utilisateur=utilisateur_id,
                                             id_manga=manga_choisi['id_manga'],
                                             commentaire=manga_choisi['commentaire'],
                                             note=manga_choisi['note'],
                                             id_avis=manga_choisi['id_avis'])
                avis_modif = AvisMangaService().supprimer(avis_a_supprimer)
                if avis_modif:
                    print('\n\nVotre avis a bien été supprimé')

        else:
            print("\n\nVous n'avez pas encore rédigé d'avis de manga")

    def afficher_avis_manga(self):

        titre = input('\n\nDe quel manga souhaitez-vous voir les avis ? ')

        avis = AvisMangaService().recup_avis_from_titre(titre)

        if avis:
            somme = 0
            for i in range(0, len(avis)):
                print(f"\n\n{avis[i]['pseudo']} a noté ce manga {avis[i]['note']}"
                    " sur 10 "
                    f"et a mis le commentaire : {avis[i]['commentaire']}")

                somme += avis[i]['note']

            moyenne = somme/len(avis)
            print(f'\n\nNos utilisateurs ont en moyenne mis la note de {moyenne}'
                ' à ce manga')
        else:
            print("\n\nInformation indisponible : aucun de nos utilisateurs n'a "
                "encore rédigé un avis sur ce manga.")

    def afficher_avis_manga_utilisateur(self, utilisateur_id):

        avis = AvisMangaService().recup_avis_from_id(utilisateur_id)

        if avis:
            print('Voici vos différents avis de mangas : ')
            for i in range(0, len(avis)):
                print(f"{i+1} : {avis[i]['titre']} : Vous avez mis la note de"
                    f" {avis[i]['note']} sur 10 avec le commentaire "
                    f"{avis[i]['commentaire']}")
        else:
            print("\n\nVous n'avez pas encore rédigé d'avis de manga")

    def afficher_avis_manga_autre_utilisateur(self):

        pseudo = input("De quel pseudo souhaitez-vous voir les avis de manga ? ")
        id_autre_utilisateur = UtilisateurService().consulter_profil(pseudo)
        if not id_autre_utilisateur:
            print(f"\n\n{pseudo} n'est pas dans notre base de données."
                  " Vérifiez qu'il s'agit du bon pseudo")
            return
        id_recherche = int(id_autre_utilisateur['id_utilisateur'])

        avis = AvisMangaService().recup_avis_from_id(id_recherche)

        if avis:
            print(f"Voici les différents avis de mangas de {pseudo} ")
            for i in range(0, len(avis)):
                print(f"{i+1} : {avis[i]['titre']} : {pseudo} a mis la note de"
                    f" {avis[i]['note']} sur 10 avec le commentaire "
                    f"'{avis[i]['commentaire']}'")
        else:
            print("\n\nAucun avis de manga ne correspond à ces informations")

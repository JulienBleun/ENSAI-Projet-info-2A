from src.dao.avis_manga_dao import AvisMangaDao
from src.service.avis_manga_service import AvisMangaService
from src.business_object.avis_manga import AvisManga


def modifier_avis_manga(utilisateur_id):

    avis = AvisMangaDao().recup_avis_from_id(utilisateur_id)

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
        print("Vous n'avez pas encore rédigé d'avis de mangas")


def supprimer_avis_manga(utilisateur_id):

    avis = AvisMangaDao().recup_avis_from_id(utilisateur_id)

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
        print("\n\nVous n'avez pas encore rédigé d'avis de mangas")


def afficher_avis_manga():

    titre = input('\n\nDe quel manga souhaitez-vous voir les avis ? ')

    avis = AvisMangaDao().recup_avis_from_titre(titre)

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

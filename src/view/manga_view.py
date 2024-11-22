from src.dao.manga_dao import MangaDao
from src.dao.avis_manga_dao import AvisMangaDao  # Assure-toi d'utiliser la classe DAO appropriée
from src.business_object.avis_manga import AvisManga  # Assure-toi d'utiliser le bon modèle
from src.service.manga_service import MangaService
from src.service.avis_manga_service import AvisMangaService
from src.utils.singleton import Singleton


class MangaView(metaclass=Singleton):

    def trouver_manga_par_id(self, utilisateur_id=None):

        id_manga = input("Entrez l'id du manga que vous recherchez : ")
        if not id_manga.isdigit():
            print("Erreur : L'identifiant du manga doit contenir uniquement des chiffres.")
            return
        try:
            manga = MangaService().consulter_manga(id_manga)

            if manga:

                print(f"\n\nManga trouvé : il s'agit de {manga.titre} écrit par"
                      f" {manga.auteur}.\n\nEn voici la description"
                      f" : {manga.descript}")
                # Option de laisser un avis
                if utilisateur_id:  # Vérifie que l'utilisateur est connecté
                    laisser_avis = input("Souhaitez-vous laisser un avis ? (o/n) : ").lower()
                    if laisser_avis == 'o':
                        commentaire = input("Entrez votre commentaire : ")
                        note = input("Entrez votre note (de 0 à 10) : ")

                        try:
                            avis = AvisMangaService().rédiger_avis_manga(
                                id_utilisateur=utilisateur_id,
                                id_manga=int(manga.id_manga),
                                commentaire=commentaire,
                                note=int(note)
                            )
                            if avis:
                                print("Votre avis a été ajouté avec succès !")
                            else:
                                print("Erreur lors de l'ajout de votre avis.")
                        except ValueError:
                            print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
            else:
                print("\n\nCe manga n'est malheureusement pas dans notre base "
                      "de données. Réessayez.")

        except Exception as e:
            print(f"Une erreur est survenue lors de la recherche : {e}")

    def trouver_manga_par_titre(self, utilisateur_id=None):

        titre = input("Entrez le titre du manga que vous recherchez : ")

        try:
            manga = MangaService().consulter_manga_par_titre(titre)

            if manga:
                print(f"\n\nManga trouvé : {manga.titre} a été écrit par"
                      f" {manga.auteur} et porte l'id {manga.id_manga}."
                      f"\n\nEn voici la description : {manga.descript}")

                # Option de laisser un avis
                if utilisateur_id:  # Vérifie que l'utilisateur est connecté
                    laisser_avis = input("Souhaitez-vous laisser un avis ? (o/n) : ").lower()
                    if laisser_avis == 'o':
                        commentaire = input("Entrez votre commentaire : ")
                        note = input("Entrez votre note (de 0 à 10) : ")

                        try:
                            avis = AvisMangaService().rédiger_avis_manga(
                                id_utilisateur=utilisateur_id,
                                id_manga=int(manga.id_manga),
                                commentaire=commentaire,
                                note=int(note)
                            )
                            if avis:
                                print("Votre avis a été ajouté avec succès !")
                            else:
                                print("Erreur lors de l'ajout de votre avis.")
                        except ValueError:
                            print("Veuillez entrer une note valide (un nombre entier entre 0 et 10).")
            else:
                print("\n\nCe manga n'est malheureusement pas dans notre base "
                      "de données. Réessayez.")

        except Exception as e:
            print(f"Une erreur est survenue lors de la recherche : {e}")

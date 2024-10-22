
def ajouter_avis_view(utilisateur_id, manga_id):
    contenu = input("Entrez votre avis : ")
    ajouter_avis_controller(utilisateur_id, manga_id, contenu)  # Utilisation du controller
    print("Avis ajouté avec succès.")


def lire_avis_view(manga_id):
    avis = obtenir_avis_pour_manga(manga_id)

    if avis:
        print("\nAvis pour ce manga :")
        for i, review in enumerate(avis, 1):
            print(f"{i}. Utilisateur: {review['utilisateur']}, Avis: {review['contenu']}")
    else:
        print("Aucun avis trouvé pour ce manga.")

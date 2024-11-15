from src.dao.utilisateur_dao import UtilisateurDao

def modifier_compte_view(utilisateur_id):
    print("\n--- Modification du compte ---")

    # Afficher les choix possibles
    print("Que souhaitez-vous modifier ?")
    print("1. Nom d'utilisateur")
    print("2. Mot de passe")
    print("3. Quitter")

    choix = input("Entrez le numéro de l'option souhaitée : ")

    nouveau_nom_utilisateur = ""
    nouveau_mot_de_passe = ""

    if choix == "1":
        nouveau_nom_utilisateur = input("Entrez votre nouveau nom d'utilisateur (laisser vide pour ne pas changer) : ")
    elif choix == "2":
        nouveau_mot_de_passe = input("Entrez votre nouveau mot de passe (laisser vide pour ne pas changer) : ")
    elif choix == "3":
        print("Modification annulée.")
        return  

    if UtilisateurDao().update_utilisateur(utilisateur_id, nouveau_nom_utilisateur, nouveau_mot_de_passe):
        print("Compte modifié avec succès!")
    else:
        print("Échec de la modification du compte.")




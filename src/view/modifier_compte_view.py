from src.dao.utilisateur_dao import UtilisateurDao

def modifier_compte_view(utilisateur_id):
    print("\n--- Modification du compte ---")
    nouveau_nom_utilisateur = input("Entrez votre nouveau nom d'utilisateur (laisser vide pour ne pas changer) : ")
    nouveau_mot_de_passe = input("Entrez votre nouveau mot de passe (laisser vide pour ne pas changer) : ")

    if UtilisateurDao().modifier_utilisateur(utilisateur_id, nouveau_nom_utilisateur, nouveau_mot_de_passe):
        print("Compte modifié avec succès!")
    else:
        print("Échec de la modification du compte.")

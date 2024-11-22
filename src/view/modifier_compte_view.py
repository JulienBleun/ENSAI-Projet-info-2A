import maskpass
from src.dao.utilisateur_dao import UtilisateurDao

def modifier_compte_view(utilisateur_id):
    print("\n--- Modification du compte ---")

    choix = input("Voulez-vous vraiment modifier vos informations ? (o/n)")
    if choix == 'o':

        nouveau_nom_utilisateur = input("Quel est votre nouveau pseudo ? ")
        nouveau_mot_de_passe = maskpass.askpass(prompt="Quel est votre "
                                                "nouveau mot de passe ? ")
    elif choix == "n":
        print("Modification annulée.")
        return

    if UtilisateurDao().update_utilisateur(utilisateur_id, nouveau_nom_utilisateur, nouveau_mot_de_passe):
        print("Compte modifié avec succès!")
    else:
        print("Échec de la modification du compte.")

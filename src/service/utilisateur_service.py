import tabulate
from src.utils.log_decorator import log
from src.business_object.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao

class UtilisateurService:
    """Classe contenant les méthodes de service de l'utilisateur."""

    @log
    def inscription(self, nom, prenom, pseudo, email, mot_de_passe):
        """Inscription d'un nouvel utilisateur.

        Paramètres :
        ------------
        nom : str
            Nom de l'utilisateur.
        prenom : str
            Prénom de l'utilisateur.
        pseudo : str
            Pseudo de l'utilisateur.
        email : str
            Email de l'utilisateur.
        mot_de_passe : str
            Mot de passe de l'utilisateur.

        Retourne :
        ----------
        Utilisateur ou None : L'utilisateur créé ou None si l'inscription a échoué.
        """

        # Crée une instance d'utilisateur avec les informations fournies
        nouveau_utilisateur = {
            "nom": nom,
            "prenom": prenom,
            "pseudo": pseudo,
            "email": email,
            "mot_de_passe": mot_de_passe,
        }

        # Ajoute l'utilisateur via le DAO et renvoie le nouvel utilisateur s'il a été ajouté avec succès
        if UtilisateurDao().add_utilisateur(nouveau_utilisateur):
            return nouveau_utilisateur
        else:
            return None





def supprimer(self, avis : AvisManga) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisMangaDao().delete_avis_manga(avis)

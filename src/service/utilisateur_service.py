
from tabulate import tabulate

from src.utils.log_decorator import log
from utils.mdp_utils import hacher_mot_de_passe

from src.business_object.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao


class UtilisateurService:
    """Classe contenant les méthodes de service de l utilisateur """
    @log
    def inscription(self, nom, prenom, pseudo, email, mdp):
        """"Création d'un utilisateur"""

        nouveau_utilisateur = Utilisateur(
            nom=nom,
            prenom=prenom,
            pseudo=pseudo,
            email=email,
            mdp=hacher_mot_de_passe(mdp, pseudo)
        )
        return nouveau_utilisateur if UtilisateurDao().add_Utilisateur(
               nouveau_utilisateur) else None






def supprimer(self, avis : AvisManga) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisMangaDao().delete_avis_manga(avis)

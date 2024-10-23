from utils.log_decorator import log

from business_object.utilisateur import utilisateur
from dao.utilisateur_dao import UtilisateurDao


class UtilisateurService:
    """Classe contenant les méthodes de service de l utilisateur """
    @log
    def inscription(self, utilisateur):
        nouveau_utilisateur = utilisateur(
                id_utilisateur=id_utilisateur,
                nom= nom ,
                mdp = mdp )
    return nouveau_utilisateur if UtilisateurDao().add_Utilisateur(nouveau_utilisateur) else None






def supprimer(self, avis : AvisManga) -> bool:

        # On supprime l'avis à partir de son id.

        return AvisMangaDao().delete_avis_manga(avis)

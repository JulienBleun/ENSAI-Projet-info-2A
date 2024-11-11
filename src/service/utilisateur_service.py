from src.utils.log_decorator import log
from src.utils.singleton import Singleton

from src.business_object.utilisateur import Utilisateur
from src.dao.utilisateur_dao import UtilisateurDao

class UtilisateurService(metaclass=Singleton):
    """Classe contenant les méthodes de service de l'utilisateur."""

    @log
    def inscription(self, nom, prenom, pseudo, email, mdp):

        nouveau_utilisateur = Utilisateur(
            nom=nom,
            prenom=prenom,
            pseudo=pseudo,
            email=email,
            mdp=mdp
        )
        return nouveau_utilisateur if UtilisateurDao().add_utilisateur(nouveau_utilisateur) else None

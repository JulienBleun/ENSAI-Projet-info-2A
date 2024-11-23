from unittest.mock import MagicMock
from src.service.utilisateur_service import UtilisateurService
from src.dao.utilisateur_dao import UtilisateurDao
from src.business_object.utilisateur import Utilisateur
import pytest



utilisateur_existant = Utilisateur(
    nom="Dupont",
    prenom="Jean",
    pseudo="jdupont",
    email="jean.dupont@example.com",
    mdp="securepassword123",
    id_utilisateur=1
)

def test_inscription_succes():
    """Test de l'inscription réussie d'un utilisateur."""
    # GIVEN
    nom, prenom, pseudo, email, mdp = "Dupont", "Jean", "jdupont", "jean.dupont@example.com", "securepassword123"
    UtilisateurDao().add_utilisateur = MagicMock(return_value=True)

    # WHEN
    utilisateur = UtilisateurService().inscription(nom, prenom, pseudo, email, mdp)

    # THEN
    assert utilisateur is not None
    assert utilisateur.nom == nom
    assert utilisateur.email == email


def test_inscription_echec_conditions():
    """Test de l'échec de l'inscription à cause de conditions invalides."""
    # GIVEN
    nom, prenom, pseudo, email, mdp = "D", "J", "jd", "email_non_valide", "short"
    
    # WHEN / THEN
    with pytest.raises(ValueError, match="Inscription échouée : Le nom doit comporter au moins 2 caractères."):
        UtilisateurService().inscription(nom, prenom, pseudo, email, mdp)


def test_inscription_echec_bdd():
    """Test de l'échec de l'inscription à cause de la base de données."""
    # GIVEN
    nom, prenom, pseudo, email, mdp = "Dupont", "Jean", "jdupont", "jean.dupont@example.com", "securepassword123"
    UtilisateurDao().add_utilisateur = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().inscription(nom, prenom, pseudo, email, mdp)

    # THEN
    assert utilisateur is None


def test_suppression_succes():
    """Test de la suppression réussie d'un utilisateur."""
    # GIVEN
    UtilisateurDao().delete_utilisateur = MagicMock(return_value=True)

    # WHEN
    resultat = UtilisateurService().suppression(utilisateur_existant.id_utilisateur)

    # THEN
    assert resultat


def test_suppression_echec():
    """Test de l'échec de la suppression d'un utilisateur."""
    # GIVEN
    UtilisateurDao().delete_utilisateur = MagicMock(return_value=False)

    # WHEN
    resultat = UtilisateurService().suppression(utilisateur_existant.id_utilisateur)

    # THEN
    assert not resultat


def test_se_connecter_succes():
    """Test de connexion réussie d'un utilisateur."""
    # GIVEN
    UtilisateurDao().se_connecter = MagicMock(return_value=utilisateur_existant)

    # WHEN
    utilisateur = UtilisateurService().se_connecter(utilisateur_existant.pseudo, utilisateur_existant.mdp)

    # THEN
    assert utilisateur is not None
    assert utilisateur.pseudo == utilisateur_existant.pseudo


def test_se_connecter_echec():
    """Test de l'échec de connexion d'un utilisateur."""
    # GIVEN
    UtilisateurDao().se_connecter = MagicMock(return_value=None)

    # WHEN
    utilisateur = UtilisateurService().se_connecter("pseudo_invalide", "mdp_invalide")

    # THEN
    assert utilisateur is None


def test_mettre_a_jour_utilisateur_succes():
    """Test de la mise à jour réussie d'un utilisateur."""
    # GIVEN
    UtilisateurDao().update_utilisateur = MagicMock(return_value=True)

    # WHEN
    resultat = UtilisateurService().mettre_a_jour_utilisateur(utilisateur_existant.id_utilisateur, "nouveau_pseudo", "nouveau_mdp")

    # THEN
    assert resultat


def test_mettre_a_jour_utilisateur_echec():
    """Test de l'échec de la mise à jour d'un utilisateur."""
    # GIVEN
    UtilisateurDao().update_utilisateur = MagicMock(return_value=False)

    # WHEN
    resultat = UtilisateurService().mettre_a_jour_utilisateur(utilisateur_existant.id_utilisateur, "nouveau_pseudo", "nouveau_mdp")

    # THEN
    assert not resultat


def test_consulter_profil_existant():
    """Test de la consultation réussie d'un profil utilisateur existant."""
    # GIVEN
    UtilisateurDao().read_profil = MagicMock(return_value=utilisateur_existant)

    # WHEN
    utilisateur = UtilisateurService().consulter_profil(utilisateur_existant.pseudo)

    # THEN
    assert utilisateur is not None
    assert utilisateur.pseudo == utilisateur_existant.pseudo


def test_consulter_profil_inexistant():
    """Test de la consultation d'un profil utilisateur inexistant."""
    # GIVEN
    UtilisateurDao().read_profil = MagicMock(return_value=None)

    # WHEN
    utilisateur = UtilisateurService().consulter_profil("pseudo_inexistant")

    # THEN
    assert utilisateur is None


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

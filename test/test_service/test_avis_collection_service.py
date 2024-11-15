from unittest.mock import MagicMock
from src.service.avis_collection_service import AvisCollectionService
from src.dao.avis_collection_dao import AvisCollectionDao
from src.business_object.avis_collection import AvisCollection


avis_existant = AvisCollection(
    id_avis=1,
    id_utilisateur=42,
    commentaire="Très bonne collection !",
    note=8,
    id_collection=201
)

avis_modifié = AvisCollection(
    id_avis=1,
    id_utilisateur=42,
    commentaire="Collection exceptionnelle avec de superbes séries.",
    note=9,
    id_collection=201
)

def test_rediger_avis_succes():
    """Test de la création réussie d'un avis pour une collection."""

    # GIVEN
    id_avis, id_utilisateur, commentaire, note, id_collection = 1, 42, "Très bonne collection !", 8, 201
    AvisCollectionDao().create_avis_collection = MagicMock(return_value=True)

    # WHEN
    nouvel_avis = AvisCollectionService().rédiger_avis_collection(
        id_utilisateur, commentaire, note, id_avis, id_collection
    )

    # THEN
    assert nouvel_avis is not None
    assert nouvel_avis.id_avis == id_avis
    assert nouvel_avis.id_collection == id_collection
    assert nouvel_avis.note == note

def test_rediger_avis_echec():
    """Test de l'échec de la création d'un avis pour une collection."""

    # GIVEN
    id_avis, id_utilisateur, commentaire, note, id_collection = 1, 42, "Très bonne collection !", 8, 201
    AvisCollectionDao().create_avis_collection = MagicMock(return_value=False)

    # WHEN
    nouvel_avis = AvisCollectionService().rédiger_avis_collection(
        id_avis, id_utilisateur, commentaire, note, id_collection
    )

    # THEN
    assert nouvel_avis is None

def test_mettre_a_jour_avis_succes():
    """Test de la mise à jour réussie d'un avis."""

    # GIVEN
    AvisCollectionDao().update_avis_collection = MagicMock(return_value=True)

    # WHEN
    avis_mis_a_jour = AvisCollectionService().mettre_a_jour(avis_modifié)

    # THEN
    assert avis_mis_a_jour is not None
    assert avis_mis_a_jour.commentaire == avis_modifié.commentaire
    assert avis_mis_a_jour.note == avis_modifié.note

def test_mettre_a_jour_avis_echec():
    """Test de l'échec de la mise à jour d'un avis."""

    # GIVEN
    AvisCollectionDao().update_avis_collection = MagicMock(return_value=False)

    # WHEN
    avis_mis_a_jour = AvisCollectionService().mettre_a_jour(avis_modifié)

    # THEN
    assert avis_mis_a_jour is None

def test_supprimer_avis_succes():
    """Test de la suppression réussie d'un avis."""

    # GIVEN
    AvisCollectionDao().delete_avis_collection = MagicMock(return_value=True)

    # WHEN
    resultat = AvisCollectionService().supprimer(avis_existant)

    # THEN
    assert resultat

def test_supprimer_avis_echec():
    """Test de l'échec de la suppression d'un avis."""

    # GIVEN
    AvisCollectionDao().delete_avis_collection = MagicMock(return_value=False)

    # WHEN
    resultat = AvisCollectionService().supprimer(avis_existant)

    # THEN
    assert not resultat

def test_consulter_avis_existant():
    """Test de la consultation d'un avis existant."""

    # GIVEN
    id_avis = 1
    AvisCollectionDao().read_avis = MagicMock(return_value=avis_existant)

    # WHEN
    avis = AvisCollectionService().consulter(id_avis)

    # THEN
    assert avis is not None
    assert avis.id_avis == id_avis
    assert avis.commentaire == avis_existant.commentaire

def test_consulter_avis_inexistant():
    """Test de la consultation d'un avis inexistant."""

    # GIVEN
    id_avis = 99
    AvisCollectionDao().read_avis = MagicMock(return_value=None)

    # WHEN
    avis = AvisCollectionService().consulter(id_avis)

    # THEN
    assert avis is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

from unittest.mock import MagicMock
from src.service.avis_manga_service import AvisMangaService
from src.dao.avis_manga_dao import AvisMangaDao
from src.business_object.avis_manga import AvisManga


avis_existant = AvisManga(
    id_avis=1,
    id_utilisateur=42,
    commentaire="Très bon manga !",
    note=9,
    id_manga=101
)

avis_modifié = AvisManga(
    id_avis=1,
    id_utilisateur=42,
    commentaire="Un manga exceptionnel avec une intrigue captivante.",
    note=10,
    id_manga=101
)

def test_rediger_avis_succes():
    """Test de la création réussie d'un avis pour un manga."""

    # GIVEN
    id_avis, id_utilisateur, id_manga, contenu, note = 1, 42, 101, "Très bon manga !", 9
    AvisMangaDao().create_avis_manga = MagicMock(return_value=True)

    # WHEN
    nouvel_avis = AvisMangaService().rédiger_avis_manga(
        id_avis, id_utilisateur, id_manga, contenu, note
    )

    # THEN
    assert nouvel_avis is not None
    assert nouvel_avis.id_avis == id_avis
    assert nouvel_avis.id_manga == id_manga
    assert nouvel_avis.note == note

def test_rediger_avis_echec():
    """Test de l'échec de la création d'un avis pour un manga."""

    # GIVEN
    id_avis, id_utilisateur, id_manga, contenu, note = 1, 42, 101, "Très bon manga !", 9
    AvisMangaDao().create_avis_manga = MagicMock(return_value=False)

    # WHEN
    nouvel_avis = AvisMangaService().rédiger_avis_manga(
        id_avis, id_utilisateur, id_manga, contenu, note
    )

    # THEN
    assert nouvel_avis is None

def test_mettre_a_jour_avis_succes():
    """Test de la mise à jour réussie d'un avis."""

    # GIVEN
    AvisMangaDao().update_avis_manga = MagicMock(return_value=True)

    # WHEN
    avis_mis_a_jour = AvisMangaService().mettre_a_jour(avis_modifié)

    # THEN
    assert avis_mis_a_jour is not None
    assert avis_mis_a_jour.commentaire == avis_modifié.commentaire
    assert avis_mis_a_jour.note == avis_modifié.note

def test_mettre_a_jour_avis_echec():
    """Test de l'échec de la mise à jour d'un avis."""

    # GIVEN
    AvisMangaDao().update_avis_manga = MagicMock(return_value=False)

    # WHEN
    avis_mis_a_jour = AvisMangaService().mettre_a_jour(avis_modifié)

    # THEN
    assert avis_mis_a_jour is None

def test_supprimer_avis_succes():
    """Test de la suppression réussie d'un avis."""

    # GIVEN
    AvisMangaDao().delete_avis_manga = MagicMock(return_value=True)

    # WHEN
    resultat = AvisMangaService().supprimer(avis_existant)

    # THEN
    assert resultat

def test_supprimer_avis_echec():
    """Test de l'échec de la suppression d'un avis."""

    # GIVEN
    AvisMangaDao().delete_avis_manga = MagicMock(return_value=False)

    # WHEN
    resultat = AvisMangaService().supprimer(avis_existant)

    # THEN
    assert not resultat

def test_consulter_avis_existant():
    """Test de la consultation d'un avis existant."""

    # GIVEN
    id_avis = 1
    AvisMangaDao().read_avis_manga = MagicMock(return_value=avis_existant)

    # WHEN
    avis = AvisMangaService().consulter(id_avis)

    # THEN
    assert avis is not None
    assert avis.id_avis == id_avis
    assert avis.commentaire == avis_existant.commentaire

def test_consulter_avis_inexistant():
    """Test de la consultation d'un avis inexistant."""

    # GIVEN
    id_avis = 99
    AvisMangaDao().read_avis_manga = MagicMock(return_value=None)

    # WHEN
    avis = AvisMangaService().consulter(id_avis)

    # THEN
    assert avis is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

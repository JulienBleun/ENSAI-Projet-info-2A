from unittest.mock import MagicMock
from src.service.manga_physique_service import MangaPhysiqueService
from src.dao.manga_physique_dao import MangaPhysiqueDAO
from src.business_object.manga_physique import MangaPhysique

# Définition d'une liste d'exemples de mangas physiques
liste_mangas_physiques = [
    MangaPhysique(id_manga_physique=1, id_manga=101, id_collection_physique=201, dernier_tome_acquis=10, tomes_manquant=[2, 5], statut="En cours"),
    MangaPhysique(id_manga_physique=2, id_manga=102, id_collection_physique=202, dernier_tome_acquis=5, tomes_manquant=[], statut="Terminé"),
    MangaPhysique(id_manga_physique=3, id_manga=103, id_collection_physique=203, dernier_tome_acquis=8, tomes_manquant=[6, 7], statut="En pause")
]

def test_creer_manga_physique_reussi():
    """Test de la création d'un manga physique réussie."""

    # GIVEN
    id_manga_physique, id_manga, id_collection_physique = 4, 104, 204
    dernier_tome_acquis, tomes_manquant, statut = 1, [], "En cours"
    MangaPhysiqueDAO().UpdateCoherent = MagicMock(return_value=True)

    # WHEN
    manga = MangaPhysiqueService().créer_manga_physique(
        id_manga_physique, id_manga, id_collection_physique,
        dernier_tome_acquis, tomes_manquant, statut
    )

    # THEN
    assert manga is not None
    assert manga.id_manga_physique == id_manga_physique
    assert manga.statut == statut

def test_creer_manga_physique_echec():
    """Test de l'échec de la création d'un manga physique."""

    # GIVEN
    id_manga_physique, id_manga, id_collection_physique = 5, 105, 205
    dernier_tome_acquis, tomes_manquant, statut = 2, [1], "En pause"
    MangaPhysiqueDAO().UpdateCoherent = MagicMock(return_value=False)

    # WHEN
    manga = MangaPhysiqueService().créer_manga_physique(
        id_manga_physique, id_manga, id_collection_physique,
        dernier_tome_acquis, tomes_manquant, statut
    )

    # THEN
    assert manga is None

def test_mettre_a_jour_reussi():
    """Test de mise à jour réussie d'un manga physique."""

    # GIVEN
    manga_existant = liste_mangas_physiques[0]
    manga_modifie = MangaPhysique(
        id_manga_physique=1, id_manga=101, id_collection_physique=201,
        dernier_tome_acquis=11, tomes_manquant=[], statut="En cours"
    )
    MangaPhysiqueDAO().update_manga_physique = MagicMock(return_value=True)

    # WHEN
    res = MangaPhysiqueService().mettre_a_jour(manga_modifie)

    # THEN
    assert res is not None
    assert res.dernier_tome_acquis == 11
    assert res.tomes_manquant == []

def test_mettre_a_jour_echec():
    """Test de l'échec de la mise à jour d'un manga physique."""

    # GIVEN
    manga_modifie = MangaPhysique(
        id_manga_physique=2, id_manga=102, id_collection_physique=202,
        dernier_tome_acquis=6, tomes_manquant=[3], statut="En pause"
    )
    MangaPhysiqueDAO().update_manga_physique = MagicMock(return_value=False)

    # WHEN
    res = MangaPhysiqueService().mettre_a_jour(manga_modifie)

    # THEN
    assert res is None

def test_consulter_manga_physique_existant():
    """Test de consultation d'un manga physique existant."""

    # GIVEN
    id_manga_physique = 1
    MangaPhysiqueDAO().read_manga_physique = MagicMock(return_value=liste_mangas_physiques[0])

    # WHEN
    manga = MangaPhysiqueService().consulter_manga_physique(id_manga_physique)

    # THEN
    assert manga is not None
    assert manga.id_manga_physique == 1
    assert manga.statut == "En cours"

def test_consulter_manga_physique_inexistant():
    """Test de consultation d'un manga physique inexistant."""

    # GIVEN
    id_manga_physique = 99
    MangaPhysiqueDAO().read_manga_physique = MagicMock(return_value=None)

    # WHEN
    manga = MangaPhysiqueService().consulter_manga_physique(id_manga_physique)

    # THEN
    assert manga is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

from unittest.mock import MagicMock
from src.service.manga_physique_service import MangaPhysiqueService
from src.dao.manga_physique_dao import MangaPhysiqueDAO
from src.business_object.manga_physique import MangaPhysique

# Définition d'une liste d'exemples de mangas physiques
liste_mangas_physiques = [
    MangaPhysique(
        id_manga_physique=1,
        titre_manga="One Piece",
        tomes_acquis=[1, 2, 3, 4],
        statut="En cours",
        id_utilisateur=101
    ),
    MangaPhysique(
        id_manga_physique=2,
        titre_manga="Naruto",
        tomes_acquis=[],
        statut="Terminé",
        id_utilisateur=102
    ),
    MangaPhysique(
        id_manga_physique=3,
        titre_manga="Bleach",
        tomes_acquis=[1, 2],
        statut="En pause",
        id_utilisateur=103
    )
]

def test_creer_manga_physique_reussi():
    """Test de la création d'un manga physique réussie."""

    # GIVEN
    titre_manga = "Attack on Titan"
    tomes_acquis, statut, id_utilisateur = [1, 2], "En cours", 104
    MangaPhysiqueDAO().create_manga_physique = MagicMock(return_value=True)

    # WHEN
    manga = MangaPhysiqueService().creer_manga_physique(
        titre_manga, tomes_acquis, statut, id_utilisateur
    )

    # THEN
    assert manga is not None
    assert manga.titre_manga == titre_manga
    assert manga.tomes_acquis == tomes_acquis
    assert manga.statut == statut

def test_creer_manga_physique_echec():
    """Test de l'échec de la création d'un manga physique."""

    # GIVEN
    titre_manga =  "Demon Slayer"
    tomes_acquis, statut, id_utilisateur = [1], "En pause", 105
    MangaPhysiqueDAO().create_manga_physique = MagicMock(return_value=False)

    # WHEN
    manga = MangaPhysiqueService().creer_manga_physique(
        titre_manga, tomes_acquis, statut, id_utilisateur
    )

    # THEN
    assert manga is None

def test_mettre_a_jour_reussi():
    """Test de mise à jour réussie d'un manga physique."""

    # GIVEN
    manga_existant = liste_mangas_physiques[0]
    manga_modifie = MangaPhysique(
        id_manga_physique=1,
        titre_manga="One Piece",
        tomes_acquis=[1, 2, 3, 4, 5],
        statut="En cours",
        id_utilisateur=101
    )
    MangaPhysiqueDAO().update_manga_physique = MagicMock(return_value=True)

    # WHEN
    res = MangaPhysiqueService().mettre_a_jour(id_manga_physique=1,
        titre_manga="One Piece",
        tomes_acquis=[1, 2, 3, 4, 5],
        statut="En cours",
        id_utilisateur=101)

    # THEN
    assert res is not None
    assert res.tomes_acquis == [1, 2, 3, 4, 5]

def test_mettre_a_jour_echec():
    """Test de l'échec de la mise à jour d'un manga physique."""

    # GIVEN
    manga_modifie = MangaPhysique(
        id_manga_physique=2,
        titre_manga="Naruto",
        tomes_acquis=[1],
        statut="En pause",
        id_utilisateur=102
    )
    MangaPhysiqueDAO().update_manga_physique = MagicMock(return_value=False)

    # WHEN
    res = MangaPhysiqueService().mettre_a_jour(id_manga_physique=1,
        titre_manga="One Piece",
        tomes_acquis=[1, 2, 3, 4, 5],
        statut="En cours",
        id_utilisateur=101)

    # THEN
    assert res is None

def test_consulter_manga_physique_existant():
    """Test de consultation d'un manga physique existant."""

    # GIVEN
    titre = "One Piece"
    MangaPhysiqueDAO().recup_manga_physique_from_titre = MagicMock(return_value=liste_mangas_physiques[0])

    # WHEN
    manga = MangaPhysiqueService().consulter_manga_physique(titre)

    # THEN
    assert manga is not None
    assert manga.id_manga_physique == 1
    assert manga.titre_manga == "One Piece"

def test_consulter_manga_physique_inexistant():
    """Test de consultation d'un manga physique inexistant."""

    # GIVEN
    titre = "One Piece 2"
    MangaPhysiqueDAO().recup_manga_physique_from_titre = MagicMock(return_value=None)

    # WHEN
    manga = MangaPhysiqueService().consulter_manga_physique(titre)

    # THEN
    assert manga is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

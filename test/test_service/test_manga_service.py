from unittest.mock import MagicMock
from service.manga_service import MangaService
from dao.manga_dao import MangaDao
from business_object.manga import Manga


liste_mangas = [
    Manga(id_manga=1, titre="One Piece", auteur="Eiichiro Oda", descript="Aventures d'un pirate nommé Luffy."),
    Manga(id_manga=2, titre="Naruto", auteur="Masashi Kishimoto", descript="Ninja"),
    Manga(id_manga=3, titre="Bleach", auteur="Tite Kubo", descript="Shinigami et hollows.")
]

def test_consulter_manga_existant():
    """Test de consultation d'un manga existant."""

    # GIVEN
    id_manga = 1
    MangaDao().trouver_par_id = MagicMock(return_value=liste_mangas[0])

    # WHEN
    manga = MangaService().consulter_manga(id_manga)

    # THEN
    assert manga is not None
    assert manga.id_manga == id_manga
    assert manga.titre == "One Piece"
    assert manga.auteur == "Eiichiro Oda"

def test_consulter_manga_inexistant():
    """Test de consultation d'un manga inexistant."""

    # GIVEN
    id_manga = 99
    MangaDao().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    manga = MangaService().consulter_manga(id_manga)

    # THEN
    assert manga is None

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])

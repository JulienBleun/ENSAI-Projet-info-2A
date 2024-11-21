import unittest
from src.business_object.manga import Manga

class TestManga(unittest.TestCase):

    def test_creation_manga(self):
        # GIVEN
        expected_titre = "One Piece"
        expected_auteur = "Eiichiro Oda"
        expected_id_manga = 12345
        expected_descript = "Super Manga"

        # WHEN
        manga = Manga(
            titre=expected_titre,
            auteur=expected_auteur,
            id_manga=expected_id_manga,
            descript = expected_descript
        )

        # THEN
        self.assertEqual(manga.titre, expected_titre)
        self.assertEqual(manga.auteur, expected_auteur)
        self.assertEqual(manga.id_manga, expected_id_manga)
        self.assertEqual(manga.descript, expected_descript)
if __name__ == '__main__':
    unittest.main()

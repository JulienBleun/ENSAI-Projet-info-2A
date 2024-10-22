import unittest
from src.business_object.manga import Manga

class TestManga(unittest.TestCase):

    def test_creation_manga(self):
        # GIVEN
        expected_titre = "One Piece"
        expected_auteur = "Eiichiro Oda"
        expected_id_manga = 12345

        # WHEN
        manga = Manga(
            titre=expected_titre,
            auteur=expected_auteur,
            id_manga=expected_id_manga
        )

        # THEN
        self.assertEqual(manga.titre, expected_titre)
        self.assertEqual(manga.auteur, expected_auteur)
        self.assertEqual(manga.id_manga, expected_id_manga)

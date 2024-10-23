import unittest
from src.business_object.manga_physique import MangaPhysique

class TestMangaPhysique(unittest.TestCase):

    def test_creation_manga_physique(self):
        # GIVEN
        expected_id_manga_physique = 1
        expected_id_collection_physique = 123
        expected_dernier_tome_acquis = 5
        expected_tomes_manquant = [6, 7, 8]
        expected_statut = "En cours"

        # WHEN
        manga_physique = MangaPhysique(
            id_manga_physique=expected_id_manga_physique,
            id_collection_physique=expected_id_collection_physique,
            dernier_tome_acquis=expected_dernier_tome_acquis,
            tomes_manquant=expected_tomes_manquant,
            statut=expected_statut
        )

        # THEN
        self.assertEqual(manga_physique.id_manga_physique, expected_id_manga_physique)
        self.assertEqual(manga_physique.id_collection_physique, expected_id_collection_physique)
        self.assertEqual(manga_physique.dernier_tome_acquis, expected_dernier_tome_acquis)
        self.assertEqual(manga_physique.tomes_manquant, expected_tomes_manquant)
        self.assertEqual(manga_physique.statut, expected_statut)


import unittest
from src.business_object.manga_physique import MangaPhysique

class TestMangaPhysique(unittest.TestCase):

    def test_creation_manga_physique(self):
        # GIVEN
        expected_id_manga_physique = 1
        expected_id_utilisateur = 3
        expected_titre_manga = "Naruto"
        expected_tomes_acquis = [5]
        expected_statut = "En cours"

        # WHEN
        manga_physique = MangaPhysique(
            id_manga_physique=expected_id_manga_physique,
            id_utilisateur=expected_id_utilisateur,  # Ajout de cette ligne
            titre_manga=expected_titre_manga,
            tomes_acquis=expected_tomes_acquis,
            statut=expected_statut
        )

        # THEN
        self.assertEqual(manga_physique.id_manga_physique, expected_id_manga_physique)
        self.assertEqual(manga_physique.id_utilisateur, expected_id_utilisateur)  # Ajout de cette ligne
        self.assertEqual(manga_physique.titre_manga, expected_titre_manga)
        self.assertEqual(manga_physique.tomes_acquis, expected_tomes_acquis)
        self.assertEqual(manga_physique.statut, expected_statut)

if __name__ == '__main__':
    unittest.main()

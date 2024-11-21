import unittest
from src.business_object.avis_manga import AvisManga


class TestAvisManga(unittest.TestCase):
    
    def test_creation_avis_manga(self):
        # GIVEN
        expected_id_avis = 1
        expected_id_utilisateur = 123
        expected_commentaire = "Un manga incroyable !"
        expected_note = 5
        expected_id_manga = 456

        # WHEN
        avis = AvisManga(
            id_avis=expected_id_avis,
            id_utilisateur=expected_id_utilisateur,
            commentaire=expected_commentaire,
            note=expected_note,
            id_manga=expected_id_manga
        )

        # THEN
        self.assertEqual(avis.id_avis, expected_id_avis)
        self.assertEqual(avis.id_utilisateur, expected_id_utilisateur)
        self.assertEqual(avis.commentaire, expected_commentaire)
        self.assertEqual(avis.note, expected_note)
        self.assertEqual(avis.id_manga, expected_id_manga)  # Changé de id_collection à id_manga

if __name__ == "__main__":
    unittest.main()
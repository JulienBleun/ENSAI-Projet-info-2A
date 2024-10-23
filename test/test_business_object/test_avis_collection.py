import unittest
from src.business_object.avis_collection import AvisCollection



class TestAvisCollection(unittest.TestCase):
    
    def test_creation_avis_collection(self):
        # GIVEN
        expected_id_avis = 1
        expected_id_utilisateur = 123
        expected_commentaire = "Une collection incroyable !"
        expected_note = 5
        expected_id_collection = 456

        # WHEN
        avis = AvisCollection(
            id_avis=expected_id_avis,
            id_utilisateur=expected_id_utilisateur,
            commentaire=expected_commentaire,
            note=expected_note,
            id_collection=expected_id_collection
        )

        # THEN
        self.assertEqual(avis.id_avis, expected_id_avis)
        self.assertEqual(avis.id_utilisateur, expected_id_utilisateur)
        self.assertEqual(avis.commentaire, expected_commentaire)
        self.assertEqual(avis.note, expected_note)
        self.assertEqual(avis.id_collection, expected_id_collection)

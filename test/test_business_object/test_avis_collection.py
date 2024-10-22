import unittest
from business_object.avis_collection import AvisCollection

class TestAvisCollection:
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
        assert avis.id_avis == expected_id_avis
        assert avis.id_utilisateur == expected_id_utilisateur
        assert avis.commentaire == expected_commentaire
        assert avis.note == expected_note
        assert avis.id_collection == expected_id_collection



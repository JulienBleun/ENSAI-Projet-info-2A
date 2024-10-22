import unittest
from src.business_object.avis_manga import AvisManga  

class TestAvisManga:
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
        assert avis.id_avis == expected_id_avis
        assert avis.id_utilisateur == expected_id_utilisateur
        assert avis.commentaire == expected_commentaire
        assert avis.note == expected_note
        assert avis.id_collection == expected_id_manga
    
    def test_creation_avis_manga_invalid_id_avis(self):
        # GIVEN
        invalid_id_avis = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            AvisManga(
                id_avis=invalid_id_avis,
                id_utilisateur=123,
                commentaire="Un manga incroyable !",
                note=5,
                id_manga=456
            )
    
    def test_creation_avis_manga_invalid_id_utilisateur(self):
        # GIVEN
        invalid_id_utilisateur = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            AvisManga(
                id_avis=1,
                id_utilisateur=invalid_id_utilisateur,
                commentaire="Un manga incroyable !",
                note=5,
                id_manga=456
            )

    def test_creation_avis_manga_invalid_note(self):
        # GIVEN
        invalid_note = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            AvisManga(
                id_avis=1,
                id_utilisateur=123,
                commentaire="Un manga incroyable !",
                note=invalid_note,
                id_manga=456
            )

    def test_creation_avis_manga_invalid_id_manga(self):
        # GIVEN
        invalid_id_manga = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            AvisManga(
                id_avis=1,
                id_utilisateur=123,
                commentaire="Un manga incroyable !",
                note=5,
                id_manga=invalid_id_manga
            )

    def test_creation_avis_manga_empty_commentaire(self):
        # GIVEN
        empty_commentaire = "" 
        
        # THEN
        with self.assertRaises(ValueError):
            # WHEN
            AvisManga(
                id_avis=1,
                id_utilisateur=123,
                commentaire=empty_commentaire,
                note=5,
                id_manga=456
            )


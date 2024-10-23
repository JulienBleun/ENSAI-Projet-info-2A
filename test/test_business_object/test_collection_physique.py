import unittest
from src.business_object.collection_physique import CollectionPhysique


class TestCollectionPhysique:
    def test_creation_collection_physique(self):
        # GIVEN
        expected_id_utilisateur = 123
        expected_id_collection = 250
        expected_titre = "One Piece"
        expected_description = "Un manga incroyable !"
        expected_contenu = "un long manga "

        # WHEN
        collection_physique = collection_physique(
            id_utilisateur=expected_id_utilisateur,
            collection=expected_collection,
            titre=expected_titre,
            description=expected_description, 
            contenu=expected_contenu
        )

        # THEN
        assert avis.id_utilisateur == expected_id_utilisateur
        assert avis.collection == expected_collection
        assert avis.titre == expected_titre
        assert avis.description == expected_description
        assert avis.contenu == expected_contenu

    def test_creation_collection_physique_id_utilisateur(self):
        # GIVEN
        invalid_id_utilisateur = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            collection_physique(
                id_utilisateur = invalid_id_utilisateur, 
                _id_collection = 250,
                titre = "One Piece",
                description = "Un manga incroyable !",
                contenu = "un long manga ",
            )

    def test_creation_collection_physique_id_collection(self):
        # GIVEN
        invalid_id_collection = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            collection_physique(
                id_utilisateur = 1, 
                _id_collection = invalid_id_collection,
                titre = "One Piece",
                description = "Un manga incroyable !",
                contenu = "un long manga ",
            )
    def test_creation_collection_physique_titre(self):
        # GIVEN 
        invalid_titre = 55
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            collection_physique(
                id_utilisateur = 1, 
                _id_collection = 545,
                titre = invalid_titre,
                description = "Un manga incroyable !",
                contenu = "un long manga ",

            )
    def test_creation_collection_physique_description(self):
        # GIVEN 
        invalid_description = 55
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            collection_physique(
                id_utilisateur = 1, 
                _id_collection = 545,
                titre = "abc",
                description = invalid_description,
                contenu = "un long manga ",

            )
def test_creation_collection_physique_contenu (self):
        # GIVEN 
        invalid_contenu = 55
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            collection_physique(
                id_utilisateur = 1, 
                _id_collection = 545,
                titre = invalid_titre,
                description = "Un manga incroyable !",
                contenu = invalid_contenu,

            )
    
if __name__ == '__main__':
    unittest.main()
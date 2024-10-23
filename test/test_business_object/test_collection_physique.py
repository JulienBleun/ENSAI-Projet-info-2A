import unittest
from src.business_object.collection_physique import CollectionPhysique
from src.business_object.manga_physique import MangaPhysique
from src.business_object.avis_collection import AvisCollection

from src.dao.collection_physique_dao import CollectionPhysiqueDAO
from src.dao.manga_physique_dao import MangaPhysiqueDAO
from src.dao.avis_collection_dao import AvisCollectionDao


class TestCollectionPhysique(unittest.TestCase):  # Inherit from unittest.TestCase
    def test_creation_collection_physique(self):
        # GIVEN
        expected_id_utilisateur = 123
        expected_id_collection = 250
        expected_titre = "One Piece"
        expected_description = "Un manga incroyable !"
        expected_contenu = "un long manga "

        # WHEN
        collection_physique = CollectionPhysique(  # Use the correct class name
            id_utilisateur=expected_id_utilisateur,
            id_collection=expected_id_collection,  # Use id_collection
            titre=expected_titre,
            description=expected_description, 
            contenu=expected_contenu
        )

        # THEN
        self.assertEqual(collection_physique.id_utilisateur, expected_id_utilisateur)  # Use self.assertEqual
        self.assertEqual(collection_physique.id_collection, expected_id_collection)  # Check collection_physique
        self.assertEqual(collection_physique.titre, expected_titre)
        self.assertEqual(collection_physique.description, expected_description)
        self.assertEqual(collection_physique.contenu, expected_contenu)

    def test_creation_collection_physique_id_utilisateur(self):
        # GIVEN
        invalid_id_utilisateur = "abc" 
        
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionPhysique(  # Use the correct class name
                id_utilisateur = invalid_id_utilisateur, 
                id_collection = 250,  # Use id_collection
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
            CollectionPhysique(  # Use the correct class name
                id_utilisateur = 1, 
                id_collection = invalid_id_collection,  # Use id_collection
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
            CollectionPhysique(  # Use the correct class name
                id_utilisateur = 1, 
                id_collection = 545,  # Use id_collection
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
            CollectionPhysique(  # Use the correct class name
                id_utilisateur = 1, 
                id_collection = 545,  # Use id_collection
                titre = "abc",
                description = invalid_description,
                contenu = "un long manga ",
            )

    def test_creation_collection_physique_contenu(self):  # Add self argument
        # GIVEN 
        invalid_contenu = 55
        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionPhysique(  # Use the correct class name
                id_utilisateur = 1, 
                id_collection = 545,  # Use id_collection
                titre = "One Piece",  # Use a valid titre
                description = "Un manga incroyable !",
                contenu = invalid_contenu,
            )

if __name__ == '__main__':
    unittest.main()

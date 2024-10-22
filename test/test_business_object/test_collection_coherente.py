import unittest
from src.business_object.collection_coherente import CollectionCoherente

class TestCollectionCoherente(unittest.TestCase):

    def test_creation_collection_coherente(self):
        # GIVEN
        expected_id_utilisateur = 1
        expected_id_collection = 1
        expected_titre = "Ma Collection"
        expected_description = "Une super collection"
        expected_contenu = "Contenu de la collection"

        # WHEN
        collection = CollectionCoherente(
            id_utilisateur=expected_id_utilisateur,
            id_collection=expected_id_collection,
            titre=expected_titre,
            description=expected_description,
            contenu=expected_contenu
        )

        # THEN
        self.assertEqual(collection.id_utilisateur, expected_id_utilisateur)
        self.assertEqual(collection.id_collection, expected_id_collection)
        self.assertEqual(collection.titre, expected_titre)
        self.assertEqual(collection.description, expected_description)
        self.assertEqual(collection.contenu, expected_contenu)

    def test_creation_collection_coherente_invalid_id_utilisateur(self):
        # GIVEN
        invalid_id_utilisateur = "abc"

        # THEN
        with self.assertRaises(ValueError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=invalid_id_utilisateur,
                id_collection=1,
                titre="Ma Collection",
                description="Une super collection",
                contenu="Contenu de la collection"
            )

    def test_creation_collection_coherente_invalid_id_collection(self):
        # GIVEN
        invalid_id_collection = "abc"

        # THEN
        with self.assertRaises(ValueError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=1,
                id_collection=invalid_id_collection,
                titre="Ma Collection",
                description="Une super collection",
                contenu="Contenu de la collection"
            )

    def test_creation_collection_coherente_invalid_titre(self):
        # GIVEN
        invalid_titre = 123

        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=1,
                id_collection=1,
                titre=invalid_titre,
                description="Une super collection",
                contenu="Contenu de la collection"
            )

    def test_creation_collection_coherente_invalid_description(self):
        # GIVEN
        invalid_description = 123

        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=1,
                id_collection=1,
                titre="Ma Collection",
                description=invalid_description,
                contenu="Contenu de la collection"
            )

    def test_creation_collection_coherente_invalid_contenu(self):
        # GIVEN
        invalid_contenu = 123

        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=1,
                id_collection=1,
                titre="Ma Collection",
                description="Une super collection",
                contenu=invalid_contenu
            )

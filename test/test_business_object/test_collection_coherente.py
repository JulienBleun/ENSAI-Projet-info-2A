import unittest
from src.business_object.collection_coherente import CollectionCoherente
from src.business_object.manga import Manga

manga_1 = Manga(id_manga=1, titre="Manga 1", auteur="Auteur 1", descript="Description 1")
manga_2 = Manga(id_manga=2, titre="Manga 2", auteur="Auteur 2", descript="Description 2")
class TestCollectionCoherente(unittest.TestCase):

    def test_creation_collection_coherente(self):
        # GIVEN
        expected_id_utilisateur = 1
        expected_id_collection = 1
        expected_titre = "Ma Collection"
        expected_description = "Une super collection"
        manga_1 = Manga(id_manga=1, titre="Manga 1", auteur="Auteur 1", descript="Description 1")
        manga_2 = Manga(id_manga=2, titre="Manga 2", auteur="Auteur 2", descript="Description 2")
        expected_contenu = [manga_1, manga_2]
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
        self.assertEqual(len(collection.contenu), 2)
        self.assertEqual(collection.contenu[0].id_manga, manga_1.id_manga)
        self.assertEqual(collection.contenu[1].id_manga, manga_2.id_manga)

    def test_creation_collection_coherente_invalid_id_utilisateur(self):
        # GIVEN
        invalid_id_utilisateur = "abc"

        # THEN
        with self.assertRaises(TypeError):
            # WHEN
            CollectionCoherente(
                id_utilisateur=invalid_id_utilisateur,
                id_collection=1,
                titre="Ma Collection",
                description="Une super collection",
                contenu=[manga_1, manga_2]
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
                contenu=[manga_1, manga_2]
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
                contenu=[manga_1, manga_2]
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
if __name__ == "__main__":
    unittest.main()
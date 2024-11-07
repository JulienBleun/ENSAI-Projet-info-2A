import unittest
from unittest.mock import MagicMock
from src.service.collection_coherente_service import CollectionCoherenteService
from src.dao.collection_coherente_dao import CollectionCoherenteDAO
from src.business_object.collection_coherente import CollectionCoherente
from src.business_object.manga import Manga


class TestCollectionCoherenteService(unittest.TestCase):
    def setUp(self):
        # Initialisation des mocks et du service
        self.service = CollectionCoherenteService()
        self.mock_dao = CollectionCoherenteDAO()
        self.service.dao = self.mock_dao  # Injection du DAO mocké
        
        # Exemple de données
        self.exemple_collection = CollectionCoherente(
            id_collection=1,
            id_utilisateur=100,
            titre="Collection Test",
            description="Description de test",
            contenu=[Manga(id_manga=1, titre="Manga 1", auteur="Pierre"), Manga(id_manga=2, titre="Manga 2", auteur="Hugo")]
        )

    def test_creer_coherent_ok(self):
        """Test de la méthode creer_coherent avec succès"""

        # GIVEN
        self.mock_dao.CreateCoherente = MagicMock(return_value=True)

        # WHEN
        nouvelle_collection = self.service.creer_coherent(
            id_collection=1,
            id_utilisateur=100,
            titre="Collection Test",
            description="Description de test",
            contenu=[Manga(id_manga=1, titre="Manga 1",auteur="Pierre"), Manga(id_manga=2, titre="Manga 2", auteur="Hugo")]
        )

        # THEN
        self.assertIsNotNone(nouvelle_collection)
        self.assertEqual(nouvelle_collection.titre, "Collection Test")
        self.mock_dao.CreateCoherente.assert_called_once_with(nouvelle_collection)




if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
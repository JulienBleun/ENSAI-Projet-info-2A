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


    def test_creer_coherent_echec(self):
        """Test de la méthode creer_coherent en cas d'échec de la création"""

        # GIVEN
        self.mock_dao.CreateCoherente = MagicMock(return_value=False)

        # WHEN
        nouvelle_collection = self.service.creer_coherent(
            id_collection=1,
            id_utilisateur=100,
            titre="Collection Test",
            description="Description de test",
            contenu=[Manga(id_manga=1, titre="Manga 1",auteur="Pierre")]
        )

        # THEN
        self.assertIsNone(nouvelle_collection)
        self.mock_dao.CreateCoherente.assert_called_once()

    def test_mettre_a_jour_coherent_ok(self):
        """Test de la méthode mettre_a_jour_coherent avec succès"""

        # GIVEN
        self.mock_dao.UpdateCoherent = MagicMock(return_value=True)

        # WHEN
        resultat = self.service.mettre_a_jour_coherent(self.exemple_collection)

        # THEN
        self.assertEqual(resultat, self.exemple_collection)
        self.mock_dao.UpdateCoherent.assert_called_once_with(self.exemple_collection)

    def test_mettre_a_jour_coherent_echec(self):
        """Test de la méthode mettre_a_jour_coherent en cas d'échec de la mise à jour"""

        # GIVEN
        self.mock_dao.UpdateCoherent = MagicMock(return_value=False)

        # WHEN
        resultat = self.service.mettre_a_jour_coherent(self.exemple_collection)

        # THEN
        self.assertIsNone(resultat)
        self.mock_dao.UpdateCoherent.assert_called_once_with(self.exemple_collection)

    def test_supprimer_coherent_ok(self):
        """Test de la méthode supprimer_coherent avec succès"""

        # GIVEN
        self.mock_dao.DeleteCoherent = MagicMock(return_value=True)

        # WHEN
        resultat = self.service.supprimer_coherent(1)

        # THEN
        self.assertTrue(resultat)
        self.mock_dao.DeleteCoherent.assert_called_once_with(1)

    def test_supprimer_coherent_echec(self):
        """Test de la méthode supprimer_coherent en cas d'échec"""

        # GIVEN
        self.mock_dao.DeleteCoherent = MagicMock(return_value=False)

        # WHEN
        resultat = self.service.supprimer_coherent(1)

        # THEN
        self.assertFalse(resultat)
        self.mock_dao.DeleteCoherent.assert_called_once_with(1)

    def test_consulter_coherent_ok(self):
        """Test de la méthode consulter_coherent avec succès"""

        # GIVEN
        self.mock_dao.ReadCoherent = MagicMock(return_value=self.exemple_collection)

        # WHEN
        resultat = self.service.consulter_coherent(1)

        # THEN
        self.assertEqual(resultat, self.exemple_collection)
        self.mock_dao.ReadCoherent.assert_called_once_with(1)




if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

    
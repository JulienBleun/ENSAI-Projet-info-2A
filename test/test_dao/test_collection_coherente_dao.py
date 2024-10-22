import unittest
from unittest.mock import MagicMock, patch
from business_object.collection_coherente import Collection_coherente

# In test_collection_coherente.py:
from src.dao.collection_coherente_dao import Collection_coherenteDAO

class TestCollectionCoherenteDAO(unittest.TestCase):

    @patch('dao.collection_coherente_dao.DBConnection')
    def test_create_coherent_success(self, mock_db_connection):
        # GIVEN
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value.connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {'id_collection': 1}  # Simulate successful insertion

        collection = Collection_coherente(id=1, titre="My Collection", description="A cool collection", mangas=[])
        dao = Collection_coherenteDAO()

        # WHEN
        created = dao.CreateCoherente(collection)

        # THEN
        self.assertTrue(created)
        mock_cursor.execute.assert_called_once()  # Verify the SQL query was executed

    @patch('dao.collection_coherente_dao.DBConnection')
    def test_update_coherent_success(self, mock_db_connection):
        # GIVEN
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value.connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 1  # Simulate one row updated

        collection = Collection_coherente(id=1, titre="Updated Title", description="Updated description", mangas=[])
        dao = Collection_coherenteDAO()

        # WHEN
        updated = dao.UpdateCoherent(collection)

        # THEN
        self.assertTrue(updated)
        mock_cursor.execute.assert_called_once()

    @patch('dao.collection_coherente_dao.DBConnection')
    def test_delete_coherent_success(self, mock_db_connection):
        # GIVEN
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value.connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.rowcount = 1  # Simulate one row deleted

        dao = Collection_coherenteDAO()
        collection_id = 1

        # WHEN
        deleted = dao.DeleteCoherent(collection_id)

        # THEN
        self.assertTrue(deleted)
        mock_cursor.execute.assert_called_once()

    @patch('dao.collection_coherente_dao.DBConnection')
    def test_read_coherent_success(self, mock_db_connection):
        # GIVEN
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_db_connection.return_value.connection.return_value = mock_connection
        mock_connection.cursor.return_value = mock_cursor
        mock_cursor.fetchone.return_value = {
            'id': 1,
            'titre': 'Test Collection',
            'description': 'A test collection',
            'mangas': []
        }

        dao = Collection_coherenteDAO()
        collection_id = 1

        # WHEN
        collection = dao.ReadCoherent(collection_id)

        # THEN
        self.assertIsNotNone(collection)
        self.assertEqual(collection.id, 1)
        self.assertEqual(collection.titre, 'Test Collection')
        mock_cursor.execute.assert_called_once()


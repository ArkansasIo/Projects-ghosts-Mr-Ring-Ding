import unittest
from unittest.mock import MagicMock, patch

from database import mysql


class MySQLTests(unittest.TestCase):
    @patch("database.mysql.connect")
    def test_add_memory_inserts_message(self, mock_connect):
        db = MagicMock()
        cursor = MagicMock()
        db.cursor.return_value = cursor
        mock_connect.return_value = db

        mysql.add_memory("session-1", "user", "Hello")

        cursor.execute.assert_called_once_with(
            "INSERT INTO memories(session_id, role, content) VALUES (%s, %s, %s)",
            ("session-1", "user", "Hello"),
        )
        db.close.assert_called_once()

    @patch("database.mysql.connect")
    def test_lookup_word_returns_dictionary_entry(self, mock_connect):
        db = MagicMock()
        cursor = MagicMock()
        cursor.fetchone.return_value = {"word": "hello", "definition": "a greeting"}
        db.cursor.return_value = cursor
        mock_connect.return_value = db

        result = mysql.lookup_word("hello")

        self.assertEqual(result["word"], "hello")
        cursor.execute.assert_called_once()
        db.close.assert_called_once()


if __name__ == "__main__":
    unittest.main()

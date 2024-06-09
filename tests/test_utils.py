import unittest
from unittest.mock import MagicMock, patch

from src.utils import get_transactions

class TestGetTransactions(unittest.TestCase):

    @patch("builtins.open")
    def test_get_transactions_valid_file(self, mock_open: MagicMock) -> None:
        mock_file = MagicMock()
        mock_file.read.return_value = '[{"transaction_id": 1, "amount": 100}]'
        mock_open.return_value.__enter__.return_value = mock_file
        new_transactions = get_transactions("test_file.json")
        self.assertEqual(new_transactions, [{"transaction_id": 1, "amount": 100}])

    @patch("builtins.open")
    def test_get_transactions_empty_file(self, mock_open: MagicMock) -> None:
        mock_file = MagicMock()
        mock_file.read.return_value = ""
        mock_open.return_value.__enter__.return_value = mock_file
        new_transactions = get_transactions("test_file.json")
        self.assertEqual(new_transactions, [])

    def test_get_transactions_file_not_found(self) -> None:
        with patch("builtins.open", side_effect=FileNotFoundError):
            new_transactions = get_transactions("nonexistent_file.json")
            self.assertEqual(new_transactions, [])

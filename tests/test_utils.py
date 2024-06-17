import unittest
import pandas as pd
from unittest.mock import MagicMock, patch, mock_open
from src.utils import get_transactions, get_transactions_csv, get_transactions_excel


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


    @patch("builtins.open", mock_open(read_data="id,amount\n1,100\n2,200"))
    @patch("csv.DictReader")
    @patch("src.utils.logger")
    def test_get_transactions_csv(self, mock_logger, mock_csv_reader):
        mock_csv_reader.return_value = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        result = get_transactions_csv("../data/transactions.csv")
        self.assertEqual(result, [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}])
        mock_logger.info.assert_called_with("открываем csv файл ")

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_get_transactions_csv(self, mock_file: MagicMock) -> None:
        result = get_transactions_csv("test.xlsx")
        self.assertEqual(result, [])


    data = {
        "id": [4699552.0],
        "state": ["EXECUTED"],
        "date": ["2022-03-23T08:29:37Z"],
        "amount": [23423.0],
        "currency_name": ["Peso"],
        "currency_code": ["PHP"],
        "from": ["Discover 7269000803370165"],
        "to": ["American Express 1963030970727681"],
        "description": ["Перевод с карты на карту"],
    }

    df = pd.DataFrame(data)

    df.to_excel("test.xlsx", index=False)

    @patch("pandas.read_excel", return_value=df)
    def test_get_transactions_excel(self, mock_read_excel: MagicMock) -> None:
        result = get_transactions_excel("test.xlsx")
        self.assertEqual(
            result,
            [
                {
                    'id': 4699552.0,
                    'state': 'EXECUTED',
                    'date': '2022-03-23T08:29:37Z',
                    'amount': 23423.0,
                    'currency_name': 'Peso',
                    'currency_code': 'PHP',
                    'from': 'Discover 7269000803370165',
                    'to': 'American Express 1963030970727681',
                    'description': 'Перевод с карты на карту'
                }
            ],
        )

import unittest
from unittest.mock import patch, Mock
from api_wrapper import APIWrapper

class TestAPIWrapper(unittest.TestCase):
    def setUp(self):
        self.api = APIWrapper(api_key="test_api_key")

    @patch('api_wrapper.requests.get')
    def test_get_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_get.return_value = mock_response

        response = self.api.get("test_endpoint")
        self.assertEqual(response, {"data": "test"})

    @patch('api_wrapper.requests.get')
    def test_get_failure(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(requests.exceptions.HTTPError):
            self.api.get("invalid_endpoint")

if __name__ == "__main__":
    unittest.main()

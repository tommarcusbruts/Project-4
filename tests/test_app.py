import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_slow(self):
        response = self.client.get('/slow')
        self.assertEqual(response.status_code, 200)

    def test_metrics(self):
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

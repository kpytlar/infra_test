import unittest

from app import app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_app(self):
        resp = self.app.get('/')
        assert b"Hello, World!" in resp.data

if __name__ == '__main__':
    unittest.main()

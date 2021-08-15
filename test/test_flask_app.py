import unittest
from flask import Flask

from src import app as myapp

class TestFlaskScript(unittest.TestCase):


    def setUp(self):
        self.app = myapp.app.test_client()


    def test_root_context(self):
        """Test root context."""
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(b'Hello, World! How do you do', response.data)


if __name__ == '__main__':
    unittest.main()

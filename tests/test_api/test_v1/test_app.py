import os

import flask.testing
from api.v1.app import app
from api.v1.views import *
import unittest
import flask

class Test_AppCase(unittest.TestCase):
    """ test app.py"""

    def test_create_app(self):
        """ check if app instance with blueprint is created"""
        with app.test_client() as c:
            self.assertIsInstance(c, flask.testing.FlaskClient)



if __name__ == '__main__':
    unittest.main()
    
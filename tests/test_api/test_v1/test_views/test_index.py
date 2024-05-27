#!/usr/bin/python3
'''testing the index route'''
import unittest
import pep8
from os import getenv
import requests
import json
from api.v1.app import *


storage = getenv('HBNB_TYPE_STORAGE')


class TestIndex(unittest.TestCase):
    """ test the index.py"""
    def test_status(self):
        with app.test_client() as c:
            resp = c.get('/api/v1/status')
            data = json.loads(resp.data.decode('utf-8'))
            self.assertEqual(data, {'status': 'OK'})

#!/usr/bin/python3
'''testing the index route'''
import unittest
import pep8
from os import getenv
import requests
import json
from api.v1.app import *
from flask import request, jsonify
from models.state import State
from models.city import City
from models import storage


class TestCities(unittest.TestCase):
    """ test cities """
    def test_list_cities(self):
        with app.test_client() as c:
            new_state = State(name="Nairobi")
            storage.new(new_state)
            new_city = City(name="CBD", state_id=new_state.id)
            storage.new(new_city)
            resp = c.get('/api/v1/states/{}/cities'.format(new_state.id))
            self.assertEqual(resp.status_code, 200)
            resp2 = c.get('/api/v1/states/{}/cities/'.format(new_state.id))
            self.assertEqual(resp2.status_code, 200)

    def test_create_city(self):
        """ tests creating a city"""
        with app.test_client() as c:
            new_state = State(name="Nairobi")
            storage.new(new_state)
            new_city = City(name="CBD", state_id=new_state.id)
            storage.new(new_city)
            resp = c.post('/api/v1/states/{}/cities'.format(new_state.id),
                          data = json.dumps({'name':"CBD"}),
                          content_type="application/json")
            self.assertEqual(resp.status_code, 201)

    def test_delete_city(self):
        """ test deleting a city"""
        with app.test_client() as c:
            new_state = State(name="Nairobi")
            storage.new(new_state)
            new_city = City(name="CBD", state_id=new_state.id)
            storage.new(new_city)
            resp = c.get('/api/v1/cities/{}'.format(new_city.id))
            self.assertEqual(resp.status_code, 200)
            resp1 = c.delete("/api/v1/cities/{}".format(new_city.id))
            self.assertEqual(resp1.status_code, 404)
            resp2 = c.get('/api/v1/cities/{}'.format(new_city.id))
            self.assertEqual(resp2.status_code, 404)
       
    def test_get_city(self):
        """ test getting a city"""
        with app.test_client() as c:
            new_state = State(name="Nairobi")
            storage.new(new_state)
            new_city = City(name="CBD", state_id=new_state.id)
            storage.new(new_city)
            resp = c.get("/api/v1/states/{}/cities".format(new_state.id))
            self.assertEqual(resp.status_code, 200)

    def test_update_city(self):
        '''test city PUT route'''
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            new_city = City(name="Chensville", state_id=new_state.id)
            storage.new(new_city)
            resp = c.put('api/v1/cities/{}'.format(new_city.id),
                         data=json.dumps({"name": "Becktropolis"}),
                         content_type="application/json")
            self.assertEqual(resp.status_code, 200)
            
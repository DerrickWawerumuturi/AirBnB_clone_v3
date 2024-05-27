#!/usr/bin/python3
'''testing the index route'''
import unittest
import json
from api.v1.app import app
from models.state import State
from models.city import City
from models import storage


class TestCities(unittest.TestCase):
    '''test city'''
    def test_lists_cities_of_state(self):
        '''test cities GET route'''
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            storage.save()
            new_city = City(name="Chensville", state_id=new_state.id)
            storage.new(new_city)
            storage.save()
            resp = c.get('/api/v1/states/{}/cities'.format(new_state.id))
            self.assertEqual(resp.status_code, 200)
            resp2 = c.get('/api/v1/states/{}/cities/'.format(new_state.id))
            self.assertEqual(resp2.status_code, 200)

    def test_create_city(self):
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            storage.save()
            resp = c.post(
                '/api/v1/states/{}/cities'.format(new_state.id),
                data=json.dumps({"name": "Chentown"}),
                content_type='application/json'
            )
            self.assertEqual(resp.status_code, 201)

    def test_delete_city(self):
        '''test city DELETE route'''
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            storage.save()
            new_city = City(name="Chensville", state_id=new_state.id)
            storage.new(new_city)
            storage.save()
            resp = c.delete('/api/v1/cities/{}'.format(new_city.id))
            self.assertEqual(resp.status_code, 404)
            resp2 = c.get('/api/v1/cities/{}'.format(new_city.id))
            self.assertEqual(resp2.status_code, 404)

    def test_get_city(self):
        '''test city GET by id route'''
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            storage.save()
            new_city = City(name="Chensville", state_id=new_state.id)
            storage.new(new_city)
            storage.save()
            resp = c.get('/api/v1/cities/{}'.format(new_city.id))
            self.assertEqual(resp.status_code, 200)

    def test_update_city(self):
        '''test city PUT route'''
        with app.test_client() as c:
            new_state = State(name="Beckystan")
            storage.new(new_state)
            storage.save()
            new_city = City(name="Chensville", state_id=new_state.id)
            storage.new(new_city)
            storage.save()
            resp = c.put('/api/v1/cities/{}'.format(new_city.id),
                         data=json.dumps({"name": "Becktropolis"}),
                         content_type="application/json")
            self.assertEqual(resp.status_code, 200)


if __name__ == '__main__':
    unittest.main()

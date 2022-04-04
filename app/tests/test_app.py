import json
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from random import randint

import flask_unittest

from app import create_app

class App(flask_unittest.ClientTestCase):
    app = create_app()
    
    def test_search(self, client):
        response = client.get("/autocomplete/pik")
        self.assertEqual(response.status_code, 200)
   
    def test_create_new_pokemon_valid_document(self, client):
        documnet_id = randint(100, 200)
        # Valid document
        body = {
                "pokadex_id": documnet_id,
                "name": "Bulbasaur",
                "nickname": "Gavrial",
                "level": 20,
                "type": "GRASS",
                "skills": [
                    "Tackle",
                    "Growl",
                    "Vine Whip",
                    "Poison Powder",
                    "Sleep Powder",
                    "Take Down",
                    "Razor Leaf",
                    "Growth"
                ]
        }
        response = client.post("/pokemon", data=json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_create_new_pokemon_invalid_id(self, client):   
        #invalid document (the same id)
        body = {
                "pokadex_id": 25,
                "name": "Bulbasaur",
                "nickname": "Gavrial",
                "level": 20,
                "type": "ELECTRIC",
                "skills": [
                    "Tackle",
                    "Growl",
                    "Vine Whip",
                    "Poison Powder",
                    "Sleep Powder",
                    "Take Down",
                    "Razor Leaf",
                    "Growth"
                ]
        }
        response = client.post("/pokemon", data=json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, 409)
   
    def test_create_pokemon_invalid_documnet(self, client):
        body = {
            "pokadex_id": "f",
                "name": "Bulbasaur",
                "nickname": "Gavrial",
                "level": 20,
                "type": "ELECTRIC",
                "skills": [
                    "Tackle",
                    "Growl",
                    "Vine Whip",
                    "Poison Powder",
                    "Sleep Powder",
                    "Take Down",
                    "Razor Leaf",
                    "Growth"
                ]
        }
        response = client.post("/pokemon", data=json.dumps(body), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        body = {
            "pokadex_id": 25,
                "name": "Bulbasaur",
                "nickname": "Gavrial",
                "level": 20,
                "type": "v",
                "skills": [
                    "Tackle",
                    "Growl",
                    "Vine Whip",
                    "Poison Powder",
                    "Sleep Powder",
                    "Take Down",
                    "Razor Leaf",
                    "Growth"
                ]
        }
        response = client.post("/pokemon", data=json.dumps(body),content_type="application/json")
        self.assertEqual(response.status_code, 400)

    def test_search(self,client):
        reponse = client.get("/autocomplete/pik")
        self.assertEqual(reponse.status_code, 200)

    def test_search_bad_charecters(self,client):
        reponse = client.get("/autocomplete/pi,")
        self.assertEqual(reponse.status_code, 400)

    
if __name__ == "__main__":
    unittest.main()
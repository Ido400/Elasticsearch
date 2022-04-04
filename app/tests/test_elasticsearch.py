import os
import sys
import unittest
from random import randint

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from elasticsearch_utils import create_document, create_query_regex_all_str, search_documents
from const import POKEMON_INDEX_NAME
from regex_strategy import StartWithTheLetters

class TestElastic(unittest.TestCase):
    def test_create_document(self):
        documnet_id = randint(300,400)
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
        create_document(POKEMON_INDEX_NAME, documnet_id, body)
    
    def test_create_regex_query(self):
        regex_strategy = StartWithTheLetters()
        query = create_query_regex_all_str("pik", ["name"], regex_strategy)
        query_check = {"query":{"bool":{"should":[{"regexp":{"name":{"value":regex_strategy.format_regex("pik")}}}]}}}
        self.assertEqual(query, query_check)

if __name__ == "__main__":
    unittest.main()
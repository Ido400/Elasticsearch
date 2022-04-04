import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest

from modules.pokemon import Pokemon

class PokemonValidator(unittest.TestCase):
    def test_create_invalid_type(self):
        with self.assertRaises(ValueError) as context:
            pokemon = Pokemon(pokadex_id=1, name="ido", nickname="ido_",
                                level=20, type="ido", skills=["ido"])

        self.assertTrue(context.exception)
   
    def test_create_invalid_skills(self):
        with self.assertRaises(ValueError) as context:
            pokemon = Pokemon(pokadex_id=1, name="ido", nickname="ido_",
                                level=20, type="ELECTRIC", skills=[])
        self.assertTrue(context.exception)
    
   
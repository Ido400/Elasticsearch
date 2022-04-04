ELASTICSEARCH_HOST = "elasticsearch"

POKEMON_INDEX_NAME = "pokemon"
POKEMON_INDEX_MAPPING = {'mappings': {'properties': {'level': {'type': 'long'},
                                                     'name': {'type': 'text',
                                                              'fields': {
                                                                  'keyword': {
                                                                      'type': 'keyword'}}},
                                                     'nickname': {'type': 'text',
                                                                  'fields': {
                                                                      'keyword': {'type': 'keyword'}}},
                                                     'pokadex_id': {'type': 'long'},
                                                     'skills': {'type': 'text',
                                                                'fields': {
                                                                    'keyword': {'type': 'keyword'}}},
                                                     'type': {'type': 'text',
                                                              'fields': {
                                                                  'keyword': {'type': 'keyword'}}}}}}
POKEMON_TYPES=["ELECTRIC", "GROUND", "FIRE", "WATER", "WIND", "PSYCHIC", "GRASS"]

FLASK_CACHE_CONFIG = {
    "DEBUG": True,        
    "CACHE_TYPE": "SimpleCache", 
    "CACHE_DEFAULT_TIMEOUT": 300
}

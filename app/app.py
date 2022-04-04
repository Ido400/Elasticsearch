from flask import Flask

from app.logging_controller import create_logger

LOGGER = create_logger("data_senes_task")

from app.elasticsearch_utils import get_es_cli
from app.cache import cache
from const import FLASK_CACHE_CONFIG

config = FLASK_CACHE_CONFIG

app = Flask(__name__)

def create_app():
    return app
    
app.config.from_mapping(config)
cache = cache.init_app(app) 

from app.routes.pokemon_route import pokemon_route

app.register_blueprint(pokemon_route)


@app.route('/')
def health():
    es_cli = get_es_cli()
    return 'My Pokemon Service is UP!'


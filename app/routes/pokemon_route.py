from flask import Blueprint, request, jsonify

from app.modules.pokemon import Pokemon
from app.elasticsearch_utils import create_document, search_documents
from app.elasticsearch_utils import create_query_string
from const import POKEMON_INDEX_NAME
from app.errors.exists_document import ExistsDocument
from app.errors.elastic_connection import FailedConnectionElastic
from app.regex_strategy import check_for_letter_pattern


pokemon_route = Blueprint("pokemon", __name__)

@pokemon_route.route("/pokemon", methods=["POST"])
def create_pokemon():
    """
    This endpoint will create a new pokemon.

    expect:
        {
        "pokadex_id": ,
        "name": "",
        "nickname": "",
        "level": ,
        "type": "",
        "skills": [
            
        ]
    }
    """
    try: 
        pokemon = Pokemon(**request.get_json())
        create_document(POKEMON_INDEX_NAME, pokemon.pokadex_id,pokemon.dict())
        return "Created the Pokemon", 200
    except TypeError:
        return "Invalid input type error", 400
    except ValueError:
        return "Invalid input value error",400
    except ExistsDocument:
        return "Document already exists", 409


@pokemon_route.route("/autocomplete/<data>", methods=["GET"]) 
def autocomplete(data:str):
    """
    This endpoint search for a documents.

    Args:
    -----
        data(str): The first characters of the search
    """
    try:
        check_for_letter_pattern(data)
        query = create_query_string(data.lower())
        search_results = search_documents(POKEMON_INDEX_NAME, query)["hits"]["hits"]
        if(search_results == []):
            return "There is no match", 204
        return jsonify(search_results), 200
    except FailedConnectionElastic:
        return "The server Failed", 500
    except ValueError:
        return "Invalid data", 400
import logging
from typing import Dict

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConflictError, ConnectionError

from app.errors.elastic_connection import FailedConnectionElastic
from app.modules.pokemon import LOGGER
from app.cache import cache
from app.errors.exists_document import ExistsDocument
from app.logging_controller import exception
from const import ELASTICSEARCH_HOST, POKEMON_INDEX_NAME, POKEMON_INDEX_MAPPING

INDEX_TO_MAPPING = {POKEMON_INDEX_NAME: POKEMON_INDEX_MAPPING}

LOGGER = logging.getLogger(__name__)

def get_es_cli():
    return Elasticsearch(hosts=[ELASTICSEARCH_HOST])

def delete_index_if_exists(index_name):
    es_cli = get_es_cli()
    if es_cli.indices.exists(index_name):
        es_cli.indices.delete(index_name)

def create_index(index_name):
    es_cli = get_es_cli()
    return es_cli.indices.create(index_name, INDEX_TO_MAPPING[index_name])

@exception(LOGGER)
def create_document(index_name:str, id:int, documnet:dict):
    """
    This method will create a new document in the desire index.

    Args:
    -----
        index_name(str):The name of the index 
        id(int): The id of the new document
        document(dict): The document that will be created
    """
    try:
        with get_es_cli() as es_cli:
            return es_cli.create(index=index_name,id=id, document=documnet)
    except ConflictError:
        raise ExistsDocument(f"The id:{id} document already exists")

def create_query_string(data:str) -> dict:
    """
    This method will create a regex query for searching a document.

    Args:
    -----
        data(str): The data that we are searching for.
        fields(list): The filed that we are desire search on.
        regex_strategy(Regex): The desire pattern of our regex search
    
    Retruns:
    --------
        This method will return a dict of the regex query.

    """
    query  =  {"query":{"query_string": {"query":f"{data}*"}}}
    return query

@exception(LOGGER)
@cache.cached(timeout=50)
def search_documents(index_name:str, query:dict):
    """
    This method will search on the specific index and return the value it
    found.

    Args:
    -----
        index_name(str): The name of the index
        query(dict): The query that we use for the search
    
    Retrun:
    -------
        Returns the search result.
    """
    try:
        with get_es_cli() as es_cli:
            data = es_cli.search(index=index_name, body=query)
            return data
    except ConnectionError:
         raise FailedConnectionElastic("Can't connect to elastic")
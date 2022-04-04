from const import POKEMON_INDEX_NAME
from app.elasticsearch_utils import delete_index_if_exists, create_index


if __name__ == "__main__":
    delete_index_if_exists(POKEMON_INDEX_NAME)
    create_index(POKEMON_INDEX_NAME)

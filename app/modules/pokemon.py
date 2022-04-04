import logging

from pydantic import BaseModel, Field, validator
from typing import List
from typing_extensions import Annotated

from const import POKEMON_TYPES
from app.logging_controller import exception

LOGGER = logging.getLogger(__name__)

class Pokemon(BaseModel):
    """
    Pokemon module 
    """
    pokadex_id:int
    name:Annotated[str, Field(max_length=100)]
    nickname:Annotated[str, Field(max_length=100)]
    level:int 
    type:Annotated[str, Field(max_length=100)]
    skills:Annotated[List[str], Field(max_length=100)]
    
    @exception(LOGGER)
    @validator("type")
    def type_validator(cls, v):
        """
        The validator check if the type exists in POKEMON_TYPES list.
        """
        if(v not in POKEMON_TYPES):
            raise ValueError("The type is not exists!")
        return v
    
    @exception(LOGGER)
    @validator("skills")
    def skills_validator(cls, v):
        """
        The validator check if skills are found.
        """
        if(len(v) == 0):
            raise ValueError("You need to write at least one skill")
        return v
    
  
    @staticmethod
    def get_str_fields():
        """
        Return list of the fields that are string type.
        """
        return  ["name", "nickname", "type", "skills"]


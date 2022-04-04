from abc import ABC, abstractmethod
import re

class Regex(ABC):
    """
    Regex strategy use to deasing a pattern
    for each case that we want to search for in our search
    query. 
    """
    @abstractmethod
    def format_regex(self, data:str) -> str:
        """
        This method will take the data and add it into a regex patten 
        and it will return a new pattern with the data. 
        """
        pass

class StartWithTheLetters(Regex):
    def format_regex(self, data: str):
        """
        This pattern use for searching words that start with 
        the data arg letters.
        """
        return f"^{data}.*"


def check_for_letter_pattern(data:str):
    """
    This method will check if the data contain only
    letters by the pattern ^[A-Za-z\s]*$. It will raise a
    ValueError if data don't match the pattern.

    Args:
    -----
        data(str): The data that we check for a match of the pattern
    """
    regex = re.compile("^[A-Za-z\s]*$")
    if(regex.match(data) == None):
        raise ValueError("The data in invalid")

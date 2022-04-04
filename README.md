
## PaaS - Pokemon as a Service

### Practical Part

Build an API service (using python and flask), by the following specifications.

1. ##### "Create a new Pokemon" endpoint -
    - Gets a JSON object of a Pokemon
    - Validates the input
    - Index it in ElasticSearch

   Here are 2 examples of Pokemon objects:

    ```// Possible pokemon types are : ["ELECTRIC", "GROUND", "FIRE", "WATER", "WIND", "PSYCHIC", "GRASS"]```
   
    ````
    {
       "pokadex_id": 25,
       "name": "Pikachu",
       "nickname": "Baruh Ha Gever",
       "level": 60,
       "type": "ELECTRIC",
       "skills": [
           "Tail Whip",
           "Thunder Shock",
           "Growl",
           "Play Nice",
           "Quick Attack",
           "Electro Ball",
           "Thunder Wave"
       ]
    }
    {
        "pokadex_id": 1,
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
    ````

2. ##### "Auto-complete" endpoint
    - This end point will get a simple query-string argument (like: "gr")
    - Will return the Pokemon objects that one of their TEXT fields contains (as a prefix of a word) our query-string-argument
    - Implement some simple caching for those search API
    
    **NOTICE** - Pokemon's TEXT fields can change often (tomorrow we will add evolve_to field). Design your solution, knowing that our autocomplete should support those new fields as well!
    
    Examples (assuming the Pokemon example in the previous section were indexed)
    ```
    // GET /api/autocomplete/pik
    [
        {
            "pokadex_id": 25,
            "name": "Pikachu",
            "nickname": "Baruh Ha Gever",
            "level": 60,
            "type": "ELECTRIC",
            "skills": [
                "Tail Whip",
                "Thunder Shock",
                "Growl",
                "Play Nice",
                "Quick Attack",
                "Electro Ball",
                "Thunder Wave"
            ]
        }
    ]
   ```
    ```
    // GET /api/autocomplete/grow
    [
        {
            "pokadex_id": 25,
            "name": "Pikachu",
            "nickname": "Baruh Ha Gever",
            "level": 60,
            "type": "ELECTRIC",
            "skills": [
                "Tail Whip",
                "Thunder Shock",
                "Growl",
                "Play Nice",
                "Quick Attack",
                "Electro Ball",
                "Thunder Wave"
            ]
        },
        {
            "pokadex_id": 1,
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
    ]
    ```
   ```
    // GET /api/autocomplete/geve
    [
        {
            "pokadex_id": 25,
            "name": "Pikachu",
            "nickname": "Baruh Ha Gever",
            "level": 60,
            "type": "ELECTRIC",
            "skills": [
                "Tail Whip",
                "Thunder Shock",
                "Growl",
                "Play Nice",
                "Quick Attack",
                "Electro Ball",
                "Thunder Wave"
            ]
        }
    ]
    ```
    ````
    // GET /api/autocomplete/leaf
    [
       {
           "pokadex_id": 1,
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
    ]
    ````

### Theoretical Part (NO CODE)

Now we would like to collect usage-log, of our API (in your service), as used by our users.

- We want to log all requests, even if they had failed
- We want to be able to identify the order of which a specific user, used our API (assume that there is a authentication mechanism)
- We may have multiple instances of the server you created. 
- In the future we would want to run analytics over those logs, so it would be a nice benefit to have easy and simple access to them

##### Questions, answer in your words:

- How would you implement it? where would you store it? 
- What would you do differently in a much larger scale of data and usage

~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*


### Set Up for Code part
Docker engine should be installed on your working environment: https://docs.docker.com/get-docker/

##### Running the system

In the context of DataSenseTask directory, run : ``sudo docker-compose up``

This will creat two containers:
1. elasticsearch - ElasticSearch instance of version 7.16. A new volume is created to store ElasticSearch data. Note that this volume will be created once, at the first system run.  
2. pokemon_app - Flask application instance, running in debug mode. 
Notice that if the content of ``requirements.txt`` or `Dockerfiile` is changes, you have to re-build pokemon_app image using `docker-compose build`
   
   
For ElasticSearch index creation, run : ``recreate_es_index.sh``
It will delete tbe current index, if exists, and create a new "pokemon" index. 

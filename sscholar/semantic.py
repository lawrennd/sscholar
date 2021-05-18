import pymongo
from pymongo import MongoClient


with open('_config.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

class Client():
    """Data structure for connecting to the Semantic Scholar data base."""
    def __init__(directory=config.mongodb_directory):
        self._client = MongoClient()
        self._db = self._client._db
        self._collection = self._db.papers


    def _find(query, number):
        return self._collection.find(query)



    
    

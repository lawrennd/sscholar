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


    def _find_files():
        """Find all files in the data downloaded from semantic scholar."""
        from pathlib import Path

        self._data_files = []
        for path in Path(config.semantic_dir).rglob('*.gz'):
            data_files.append(path.name)
        self._data_files.sort()
    

for file in files[3758:]:
    if file in ['license.txt', 'manifest.txt', 's2-corpus-1001']:
        continue
    with gzip.open(os.path.join(semantic_dir, file)) as f:
        it = jsonstream.load(f)
        while True:
            try:
                collection.insert_one(next(it))
            except StopIteration as e:
                print('completed file ' + file)
                break
            except json.JSONDecodeError:
                missing_files.append(file)
                print('Decode Error file:' + file)
    
    

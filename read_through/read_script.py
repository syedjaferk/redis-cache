
from pymongo.mongo_client import MongoClient
import json

def find_data(key):
    MONGO_CONN_STR = "mongodb://host.docker.internal:27017"
    mongo_client = MongoClient(MONGO_CONN_STR)
    database = mongo_client['test']
    collection = database["todos"]
    db_data = collection.find_one({'id': key}, {"_id": 0})
    return db_data

def read_cache(event):
    key = event['key']
    data = execute('GET', key)
    if data:
        return data
    data = find_data(key)
    execute('SET', key, data['name'])
    override_reply(data['name'])
    return data['name']

GB('KeysReader').map(read_cache).register(commands=['get'], mode='sync')

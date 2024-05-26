from gearsclient import GearsRemoteBuilder as GearsBuilder
from gearsclient import execute
from pymongo.mongo_client import MongoClient

import random

def find_data(key):
    MONGO_CONN_STR = "mongodb://localhost:27017"
    mongo_client = MongoClient(MONGO_CONN_STR)
    database = mongo_client['test']
    collection = database["todos"]
    db_data = collection.find_one({'id': key}, {"_id": 0})
    return db_data

def read_cache(event):
    key = event['key']
    data = execute('HGETALL', key)
    if data:
        return data
    data = find_data(key)
    execute('HMSET', key, data)
    override_reply(data)
    return data

GearsBuilder(reader='KeysReader', requirements=["pymongo"]).map(read_cache).register(commands=['hgetall'], mode='sync')

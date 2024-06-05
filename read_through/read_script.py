
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
    data = execute('JSON.GET', key)
    if data:
        return data
    data = find_data(key)
    json_str = json.dumps(data)
    execute('JSON.SET', key, '.', json_str)
    override_reply(json_str)
    return json_str

GB('KeysReader').map(read_cache).register(commands=['JSON.GET'], mode='sync')

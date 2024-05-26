# from gearsclient import GearsRemoteBuilder as GearsBuilder
from pymongo.mongo_client import MongoClient
# from gearsclient import execute
import redis

import logging
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def read_through_cache(keys):

    MONGO_CONN_STR = "mongodb://localhost:27017"
    mongo_client = MongoClient(MONGO_CONN_STR)
    database = mongo_client['test']
    collection = database["todos"]

    key = keys['key']
    cached_data = execute('HGETALL', key)
    
    if cached_data:
        # Cache hit
        return cached_data
    
    # Cache miss - query the database
    db_data = collection.find_one({'id': key}, {"_id": 0})

    if db_data:
        execute('HMSET', key, db_data)
    override_reply(db_data)
    return db_data

GB("KeysReader").map(fetch_data).register(commands=['get'], eventTypes=['keymiss'])

# gb = GearsBuilder(requirements=["pymongo"])
# # gb.foreach(read_through_cache)
# # gb.register()
# gb.map(lambda x: read_through_cache(x))
# res = gb.register(prefix="*", trigger='KeysReader')
# print(res)
# # gb.register(trigger='MyTrigger', mode='async_local', onRegistered=lambda: my_trigger_function(param1, param2))
# # gb.run(trigger='KeysReader')

# # def maximum(a, x):
# #   ''' Returns the maximum '''
# #   a = a if a else 0  # initialize the accumulator
# #   print("HI ")
# #   return 12344

# # gb = GearsBuilder()
# # gb.map(lambda x: int(x['value']['age']))
# # gb.accumulate(maximum)
# # res = gb.register('person:*')
# print(res)
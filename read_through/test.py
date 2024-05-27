from pymongo.mongo_client import MongoClient

MONGO_CONN_STR = "mongodb://localhost:27017"
mongo_client = MongoClient(MONGO_CONN_STR)
database = mongo_client['test']
collection = database["todos"]
db_data = collection.find_one({'id': "3"}, {"_id": 0})

print(db_data['name'])
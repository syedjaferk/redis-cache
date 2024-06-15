from rgsync import RGJSONWriteBehind, RGWriteBehind
from rgsync.Connectors import MongoConnection, MongoConnector
import os

MONGODB_URL = os.environ.get('MONGO_URI')

connection = MongoConnection('', '', '', '', MONGODB_URL)
db = 'test'

user_connector = MongoConnector(connection=connection, db=db, tableName='todos', pk='id')

RGJSONWriteBehind(GB, keysPrefix='todos:12', connector=user_connector, name='WatchHistoryWriteBehind1', version='99.99.99')

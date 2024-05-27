from rgsync import RGJSONWriteBehind, RGWriteBehind
from rgsync.Connectors import MongoConnection, MongoConnector

MONGODB_URL = "mongodb://host.docker.internal:27017"

connection = MongoConnection('', '', '', '', MONGODB_URL)
db = 'test'

user_connector = MongoConnector(connection=connection, db=db, tableName='users', pk='userId')

RGJSONWriteBehind(GB, keysPrefix='users', connector=user_connector, name='WatchHistoryWriteBehind1', version='99.99.99')

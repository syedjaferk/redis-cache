from rgsync import RGJSONWriteBehind, RGWriteBehind, RGJSONWriteThrough
from rgsync.Connectors import MongoConnection, MongoConnector

MONGODB_URL = "mongodb://host.docker.internal:27017"

connection = MongoConnection('', '', '', '', MONGODB_URL)
db = 'dbSpeedMernDemo'

user_connector = MongoConnector(connection, db, 'movies', 'movieId')

RGJSONWriteThrough(GB, keysPrefix='MovieEntity', connector=user_connector, name='MoviesWriteThrough', version='99.99.99')



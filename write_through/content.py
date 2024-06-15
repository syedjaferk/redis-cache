from rgsync import RGJSONWriteBehind, RGJSONWriteThrough
from rgsync.Connectors import MongoConnector, MongoConnection
# change mongodb connection (admin)
import os
# mongodb://usrAdmin:passwordAdmin@10.10.20.2:27017/dbSpeedMernDemo?authSource=admin
# mongoUrl = "mongodb://172.19.0.2:27017"
mongoUrl = os.environ.get('MONGO_URI')
# MongoConnection(user, password, host, authSource?, fullConnectionUrl?)
connection = MongoConnection("", "", "", "", mongoUrl)
# change MongoDB database
db = "dbSpeedMernDemo"
collection = "movies"

movieConnector = MongoConnector(connection, db, 'movies', 'movieId')
RGJSONWriteBehind(GB, keysPrefix='MovieEntity',
connector=movieConnector, name='MoviesWriteBehind',
version='99.99.99')
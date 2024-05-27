import redis
from redis.commands.json.path import Path
from redis.commands.json import JSON

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

user = {
    "user":{
        "name": "Sarah Zamir",
        "email": "sarah.zamir@example.com",
        "age": 30,
        "city": "Paris"
    }
}

JSON(r).set("users:4", Path.root_path(), user)

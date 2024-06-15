import redis
from redis.commands.json.path import Path
from redis.commands.json import JSON

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

user = {
    "id":"test_id",
    "name":"some todo",
    "description": "some description"
}

JSON(r).set("todos:test_id", Path.root_path(), user)

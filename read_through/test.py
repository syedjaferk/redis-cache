from gearsclient import GearsRemoteBuilder as GearsBuilder, execute
import redis


r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.config_set('notify-keyspace-events', 'KEA')
res = r.hgetall("1")
# execute("")

print(res)
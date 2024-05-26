import redis
# from gearsclient import GearsRemoteBuilder as GearsBuilder
# from gearsclient import execute

async def fetch_data(r):
    # key = r['key']
    # value = 1000
    # execute('SET', key, value)  
    # return execute('GET', key)  
    # return value
    override_reply('key miss')
    return r


# res = GearsBuilder().foreach(fetch_data).register(tigger='GET', mode="sync", onRegistered=fetch_data)

# # Register the RedisGears function
# def register_read_through_cache():
#     gb = GearsBuilder('KeysReader')
#     gb.foreach(fetch_data)
#     gb.register(commands=['get'], eventTypes=['keymiss'])

# # Register the function when the script runs
# register_read_through_cache()
# print(res)

GB("KeysReader").map(fetch_data).register(commands=['get'], eventTypes=['keymiss'])
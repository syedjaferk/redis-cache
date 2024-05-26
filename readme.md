
## Redis:

```
docker run --name redis_container redis
```

## MongoDb:

```
docker run --name mongo_container mongo
```

To Restore data to mongo db, 

```
docker exec -i <mongodb container> sh -c 'mongorestore --archive' < db.dump
```


## 1. Cache Aside

1. When the application needs to read data from db, it will first check the cache. 
2. If its present in the cache, returns it. 
3. Else fetch from the db and write to cache and returns it. 


## 2. Read Through

### Redis

```
docker run -p 6379:6379 redislabs/redisgears:edge
```
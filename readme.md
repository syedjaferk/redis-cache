
## Redis:

```
docker run -p 6379:6379 redislabs/redismod:latest
```

## MongoDb:

```
docker run --name mongo_container mongo
```

To Restore data to mongo db, 

```
docker exec -i <mongodb container> sh -c 'mongorestore --archive' < db.dump
```

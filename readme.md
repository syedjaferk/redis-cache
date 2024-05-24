
## 1. Cache Aside

1. When the application needs to read data from db, it will first check the cache. 
2. If its present in the cache, returns it. 
3. Else fetch from the db and write to cache and returns it. 

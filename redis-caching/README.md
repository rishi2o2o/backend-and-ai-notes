# Redis Cache

Redis is an open-source, in-memory data structure store used primarily as a lightning-fast cache and database. By keeping frequently accessed data in RAM rather than on a slower physical disk, Redis delivers sub-millisecond responses, dramatically speeding up web applications and reducing the load on primary databases.


## How It Works

Instead of querying a heavy database every time an application requests data, a Redis cache is placed in between your application and your main data source.

* Cache-Aside Pattern: When a request is made, the application first checks Redis. If the data is found (cache hit), it is returned instantly.

* Database Fallback: If the data is missing (cache miss), the application queries the main database, saves a copy of that data in Redis, and then returns it to the user. Future requests for that same data are then served immediately from memory.



import redis
import time
import json

redis_cache = redis.Redis(host='localhost', port=6379, decode_responses=True)

mock_db = {  # user_id -> user_data
    1: {"name": "Bob", "email": "bob@email.com"},
    2: {"name": "Hal", "email": "hal@email.com"}
}

def get_user_data(user_id :int) -> dict:
    cached_user = redis_cache.get(user_id)
    
    if cached_user:
        print("Fetching from cache...")
        return json.loads(cached_user)

    print("Fetching from database...")
    time.sleep(2)  # mock slow db query
    user = mock_db.get(user_id, None)

    if user:
        redis_cache.setex(user_id, 60, json.dumps(user))
        return user


if __name__ == "__main__":
    # First call: Slow (Database)
    print(get_user_data(1))

    # Second call: Fast (Redis)
    print(get_user_data(1))




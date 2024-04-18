import redis
redis_host = 'localhost'
redis_port = 6379
client = redis.Redis(host=redis_host, port=redis_port, db=0)

import redis
import random
from app.utils import random_string

db = {
    'key': random_string()
}
TTL = 60 * 5  # 5 minutes


class ProbabilisticRedisClient:
    def __init__(self, host='localhost', port=6379, db=0):
        """Initialize the Redis client with a connection to the specified Redis server.

        Args:
            host (str): Hostname of the Redis server.
            port (int): Port on which Redis server is listening.
            db (int): Database number to connect to.
        """
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)

    def set(self, key, value, ttl=None):
        """Set a key in Redis with an optional TTL (time to live in seconds)."""
        if ttl:
            self.client.setex(key, ttl, value)
        else:
            self.client.set(key, value)

    def get(self, key):
        """Retrieve a key from Redis and probabilistically decide to delete it based on its TTL."""
        ttl = self.client.ttl(key)
        if ttl == -1:  # No expiration
            return self.client.get(key)

        probability = self.calculate_clear_probability(ttl)
        if random.random() < probability:
            self.client.delete(key)
            print(f"Key '{key}' was cleared probabilistically based on its TTL.")
            return None  # Return None to simulate that the key has expired

        return self.client.get(key)

    @staticmethod
    def calculate_clear_probability(ttl):
        """Calculate the probability of clearing a key based on its TTL."""
        if ttl > 0:
            return 1 - (ttl / TTL)
        return 0

    def delete(self, key):
        """Delete a specific key from Redis."""
        self.client.delete(key)


if __name__ == '__main__':

    redis_client = ProbabilisticRedisClient()
    redis_client.set('key', db.get('key'), ttl=TTL)

    while True:
        if not redis_client.get('key'):
            redis_client.set('key', db.get('key'), TTL)

import redis
import random
from .utils import random_string


class ProbabilisticRedisClient:
    def __init__(self, host='localhost', port=6379, db=0, clear_probability=0.05):
        """Initialize the Redis client with a connection to the specified Redis server.

        Args:
            host (str): Hostname of the Redis server.
            port (int): Port on which Redis server is listening.
            db (int): Database number to connect to.
            clear_probability (float): Probability with which the cache should be cleared.
        """
        self.client = redis.Redis(host=host, port=port, db=db, decode_responses=True)
        self.clear_probability = clear_probability

    def set(self, key, value):
        """Set a key in Redis, potentially clearing the cache probabilistically before doing so."""
        self.probabilistic_clear()
        self.client.set(key, value)

    def get(self, key):
        """Retrieve a key from Redis."""
        return self.client.get(key)

    def probabilistic_clear(self):
        """Clear the cache with a defined probability."""
        if random.random() < self.clear_probability:
            self.client.flushdb()
            print('Cache cleared probabilistically.')

    def delete(self, key):
        """Delete a specific key from Redis."""
        self.client.delete(key)


#
if __name__ == '__main__':
    # Initialize the client with a 5% chance of clearing the entire cache on each set operation
    redis_client = ProbabilisticRedisClient(clear_probability=0.05)

    # Operations
    redis_client.set(random_string(), random_string())
    redis_client.set(random_string(), random_string())
    redis_client.set(random_string(), random_string())
    redis_client.set(random_string(), random_string())
    redis_client.set(random_string(), random_string())

import random
from app.utils import random_string
from app.client import client as r

keys = r.keys('*')
try:
    while True:
        if keys:
            r.get(random.choice(keys))  # Access a random key to trigger eviction conditions
        key = random_string(10)
        value = random_string(50)
        r.set(key, value, ex=60 * 60)  # Set key with 1 hour expiration
        if r.get(key) is None:
            print(f'Eviction occurred at key: {key}')
except Exception as e:
    print(f'Stopped writing due to error: {e}')
finally:
    print('Current keys in Redis:', r.keys('*'))

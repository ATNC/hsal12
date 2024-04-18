
This project involves building a master-slave Redis cluster, testing all eviction strategies, and implementing a wrapper for the Redis client that includes probabilistic cache clearing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- pip
- Redis

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository
2. Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Running the tests

### Eviction Strategies

The `app/eviction_testing.py` file contains the code for testing all eviction strategies. It continuously writes keys to Redis and reads a random key to trigger eviction conditions.

### Probabilistic Cache Clearing

The `app/probabilistic_expiration.py` file contains a wrapper for the Redis client that implements probabilistic cache clearing. The `ProbabilisticRedisClient` class has a `probabilistic_clear` method that clears the cache with a defined probability.

### Docker Compose

This application can also be run using Docker Compose. Here are the steps:

1. Install Docker and Docker Compose on your machine. You can find the installation guides on the official Docker documentation.

2. Clone the repository.

3. Navigate to the project directory.

4. Build and run the Docker containers using the following command:

```bash
docker-compose up --build
```

5. The application should now be running on the specified ports in the `docker-compose.yml` file.

6. To stop the application and remove the containers, use the following command:

```bash
docker-compose down
```

Please note that you need to have a `docker-compose.yml` file in your project directory for these steps to work. This file should define the services that make up your app so they can be run together in an isolated environment.
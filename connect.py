import configparser
import pathlib

from mongoengine import connect
# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi
import redis
from redis_lru import RedisLRU


# docker run --name redis-cache -d -p 6379:6379 redis
r = redis.Redis(host="localhost", port=6379, password=None, db=0)
cache = RedisLRU(r)

file_config = pathlib.Path(__file__).parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read(file_config)

username = config.get('DEV_DB', 'USER')
password = config.get('DEV_DB', 'PASSWORD')
database = config.get('DEV_DB', 'DB_NAME')

uri = f"mongodb+srv://{username}:{password}@{database}/?retryWrites=true&w=majority"

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
session_hw = connect("home_work_8",host=uri, ssl=True)


# sample_con = client.sample_airbnb

# if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    # data = sample_con.listingsAndReviews.find().limit(2)
    # for i in data:
    #     print(f'{i["name"]}:{i["description"]}')
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://hw8webgoit:Goitpython12@cluster0.0uvhgzn.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.home_work_8
sample_con = client.sample_airbnb

if __name__ == "__main__":
    # Send a ping to confirm a successful connection
    data = sample_con.listingsAndReviews.find().limit(2)
    for i in data:
        print(f'{i["name"]}:{i["description"]}')
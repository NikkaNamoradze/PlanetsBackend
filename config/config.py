
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nikkanamoradze:Namora123@planetscluster.vnhyz.mongodb.net/?retryWrites=true&w=majority&appName=PlanetsCluster"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.Planets
planets_collection = db["planets"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

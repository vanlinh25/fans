import pymongo
DB_URL = "mongodb://localhost:27017/"
DB_NAME = "test"


client = pymongo.MongoClient(DB_URL)
db = client[DB_NAME]
fan = db["fans"]

import pymongo
DB_URL = "mongodb://localhost:27017/"
DB_NAME = "test"

def getConnection():
    try:
        client = pymongo.MongoClient(DB_URL)
        db = client[DB_NAME]
        return db
    except:
        print("error to connect db")
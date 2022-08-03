import motor.motor_asyncio
from beanie import init_beanie

from data.models.idol import Idol

DB_URL = "mongodb://localhost:27017/"
DB_NAME = "test"
# client = pymongo.MongoClient(DB_URL)
# db = client[DB_NAME]
# fan = db["fans"]

async def initDB():
    client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
    await init_beanie(client[DB_NAME], document_models=[Idol])




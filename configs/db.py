import motor.motor_asyncio
from beanie import init_beanie
import pymongo

from data.models.idol import Idol
from configs.settings import get_settings


async def initDB():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(get_settings().DB_URL)
        await init_beanie(client[get_settings().DB_NAME], document_models=[Idol])
    except:
        print("Fail to connect to DB")
        


def getDB():
    client = pymongo.MongoClient(get_settings().DB_URL)
    db = client[get_settings().DB_NAME]
    return db
    

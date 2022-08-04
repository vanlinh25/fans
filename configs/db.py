import motor.motor_asyncio
from beanie import init_beanie

from data.models.idol import Idol
from configs.settings import get_settings

async def initDB():
    try:
        client = motor.motor_asyncio.AsyncIOMotorClient(get_settings().db_url)
        await init_beanie(client[get_settings().db_name], document_models=[Idol])
    except:
        print("Fail to connect to DB")




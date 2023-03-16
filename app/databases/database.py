from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os

from dotenv import load_dotenv

load_dotenv()

user_db = os.getenv("USER_DB")
password_db = os.getenv("MONGO_PASSWORD")


client = AsyncIOMotorClient(
    f"mongodb+srv://{user_db}:{password_db}@padelapp.ikvhpet.mongodb.net/test"
    
)


engine = AIOEngine(client=client)

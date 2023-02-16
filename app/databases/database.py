from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os 

from dotenv import load_dotenv

load_dotenv()

user_db = os.environ.get('USER_DB')
password = os.getenv("MONGO_PASSWORD")

client = AsyncIOMotorClient("mongodb+srv://alvaro-padelapp:a7gyfaxRHVgRSIiT@padelapp.ikvhpet.mongodb.net/test")


engine = AIOEngine(client=client)
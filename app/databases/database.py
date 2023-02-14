from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import os 

from dotenv import load_dotenv

load_dotenv()

password = os.getenv("MONGO_PASSWORD")

#client = AsyncIOMotorClient(f"mongodb+srv://alvaro:{password}@data-base-padel.k5g0psy.mongodb.net/registro-padel")
client = AsyncIOMotorClient("mongodb://localhost:27017")

#engine = AIOEngine(client=client)
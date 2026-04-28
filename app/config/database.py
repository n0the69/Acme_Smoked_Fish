from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

class Database:

    def __init__(self):
        uri = os.getenv("MONGO_URI")
        dbname = os.getenv("DB_NAME")

        self.client = MongoClient(uri)
        self.db = self.client[dbname]

database = Database()
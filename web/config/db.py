from pymongo import MongoClient
import os
import dotenv


dotenv.load_dotenv()

USER = os.environ.get("MONGOUSR")
PASSWORD = os.environ.get("MONGOPASS")
DBNAME = os.environ.get("dbname")

db_client = MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@cluster0.rycij.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").cervesia

from sqlmodel import create_engine
import os
import dotenv

dotenv.load_dotenv()

USER = os.environ.get("user")
PASSWORD = os.environ.get("pass")
DBNAME = os.environ.get("dbname")

def connect():
    engine = create_engine(f"postgresql+psycopg2://{USER}:{PASSWORD}@localhost:5432/{DBNAME}")
    return engine

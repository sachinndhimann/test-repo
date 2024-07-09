from sqlalchemy import create_engine, MetaData
from databases import Database

DATABASE_URL = "postgresql://user:password@db:5432/database"

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)

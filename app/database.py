from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_PATH)

try:
    with engine.connect() as connection:
        print("Database Connection is successful")
except Exception as e:
    print("Database connection failed")
    print("Error:",e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
Base = declarative_base()

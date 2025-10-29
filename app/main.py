from fastapi import FastAPI
from app.database import engine
from app.db_models import Base
from routes import user, transactions

try:
    Base.metadata.create_all(bind=engine)
    print("tables created")
except Exception as e:
    print("error creating table: ",e)

myapp = FastAPI()

# including routers here:
myapp.include_router(user.user_route)
myapp.include_router(transactions.transaction_route)


from app.database import SessionLocal
from sqlalchemy import UUID
from sqlalchemy.orm import Session 
from app.db_models import User
from fastapi import HTTPException,status
from pydantic import EmailStr

# function to retrieve database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 



        #hjgd

# function to fetch the user by his/her id
def fetch_user_by_id(id:UUID,dbase:Session):
    db_user = dbase.query(User).filter(User.id == id).first()
    if db_user is None:
        raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail="There is no user with the provided id"
        )
    return db_user

# function to fetch the user by his/her email
def fetch_user_by_email(email:EmailStr,dbase:Session):
    db_user = dbase.query(User).filter(User.email == email).first()
    if db_user is None:
        raise HTTPException(
           status_code=status.HTTP_404_NOT_FOUND,
           detail="There is no user with the provided email"
        )
    return db_user
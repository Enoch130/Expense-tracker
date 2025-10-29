from fastapi import APIRouter, Depends, HTTPException, status
from app.database import SessionLocal
from sqlalchemy.orm import Session 
from app.db_models import User
from app.pd_models import UserIn,UserOut,UserLastNameIn,UserFirstNameIn,UserPhoneIn,UserEmailIn,userlogin,UserPasswordIn
from passlib.context import CryptContext
from uuid import UUID
from pydantic import EmailStr
from typing import List
from app.operations import get_db,fetch_user_by_email,fetch_user_by_id


user_route = APIRouter(prefix="/users",tags=["Users Route"])
   

# creating a password context variable
pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# create a new item into the backend
@user_route.post("/SignUp", response_model=UserOut)
async def signup_new_user(user:UserIn, db:Session = Depends(get_db)):
    # let us hash the password first 
    hashed_password = pass_context.hash(user.password)
    new_user = User(email = user.email, firstname = user.firstname, middlename = user.middlename, lastname = user.lastname,password=hashed_password,phonenumber=user.phonenumber)

    db.add(new_user) # telling sqlalchemy to add this to the database
    db.commit() # this saves new changes in the database
    db.refresh(new_user)  # this updates the user object
    return new_user

# log in endpoint for users
@user_route.post("/login",response_model=UserOut)
async def login_user(user:userlogin,db:Session=Depends(get_db)):
    db_user = fetch_user_by_email(email=user.email,dbase=db)
    #verifying the password provided
    verified = pass_context.verify(user.password,db_user.password)
    if not verified:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Password is incorrect"
        )
    return db_user


# get something from backend
@user_route.get("/get_user_by_id",response_model=UserOut) # this is the endpoint
async def get_user_by_id(id:UUID, db:Session = Depends(get_db)):
    user = fetch_user_by_id(id=id,dbase=db)
    return user

#get user by email
@user_route.get("/get_user_by_email",response_model=UserOut) # this is the endpoint
async def get_user_by_email(email:EmailStr, db:Session = Depends(get_db)):
    user = fetch_user_by_email(email=email,dbase=db)
    return user

# get all users from the database
@user_route.get("/get_all_users",response_model=List[UserOut]) # this is the endpoint
async def get_user_by_id(db:Session = Depends(get_db)):
    users = db.query(User).all()
    return users

# update items in the backend
@user_route.put("/update_phoneNumber",response_model=UserOut)
async def update_phone_number(user:UserPhoneIn,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=user.id,dbase=db)
    if db_user.phonenumber == user.phoneNumber:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Phone number is the same. It should be different."
        )
    elif user.phoneNumber is None:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Please provide a phone number"
        )
    db_user.phonenumber = user.phoneNumber
    db.commit()
    db.refresh(db_user)
    return db_user

#endpoint to change the first name of users:
@user_route.put("/update_first_name",response_model=UserOut)
async def update_firstname(user:UserFirstNameIn,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=user.id,dbase=db)
    if db_user.firstname == user.firstname:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "First name is the same. It should be different."
        )
    elif user.firstname is None:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Please provide your first name"
        )
    db_user.firstname = user.firstname
    db.commit()
    db.refresh(db_user)
    return db_user

#endpoint to change the last name of users
@user_route.put("/update_last_name", response_model = UserOut)
async def update_lastname(user:UserLastNameIn,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=user.id,dbase=db)
    if db_user.lastname == user.lastname:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Last name is the same. It should be different."
        )
    elif user.lastname is None:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Please provide your last name"
        )
    db_user.lastname = user.lastname
    db.commit()
    db.refresh(db_user)
    return db_user

#endpoint to change the email of users
@user_route.put("/update_email", response_model = UserOut)
async def update_email(user:UserEmailIn,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=user.id,dbase=db)
    if db_user.email == user.email:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Email is the same. It should be different."
        )
    elif user.email is None:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Please provide your email"
        )
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user

#password is not working
@user_route.put("/update_password", response_model = UserOut)
async def update_password(user:UserPasswordIn,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=user.id,dbase=db)
    verified = pass_context.verify(user.password,db_user.password)
    if verified:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Password is the same. It should be different."
        )
    elif user.password is None:
        raise HTTPException(
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail = "Please provide your new password"
        )
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

# delete items in the backend
@user_route.delete("/delete_user")
async def delete_user(id:UUID, db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=id,dbase=db)
    db.delete(db_user)
    db.commit()
    return db_user

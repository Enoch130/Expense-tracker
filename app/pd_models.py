# pydantic model - validate data, define how the input should be
from pydantic import BaseModel,EmailStr
from uuid import UUID
from datetime import datetime


class UserIn(BaseModel):
    firstname:str
    middlename:str=None
    lastname:str
    email:EmailStr
    password:str
    phonenumber:str

#model for log in user
class userlogin(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    firstname:str
    id:UUID
    email:EmailStr
    lastname:str
    phonenumber:str

# model for updates coming
class UserLastNameIn(BaseModel):
    id:UUID
    lastname:str

class UserPhoneIn(BaseModel):
    id:UUID
    phoneNumber:str
    
class UserFirstNameIn(BaseModel):
    id:UUID
    firstname:str
    
class UserEmailIn(BaseModel):
    id:UUID
    email:EmailStr

class UserPasswordIn(BaseModel):
    id:UUID
    password:str

class TransactionIn(BaseModel):
    title:str
    description:str
    type:str
    cost:float
    owner_id:UUID
    medium:str

class TransactionOut(BaseModel):
    title:str
    description:str
    type:str
    cost:float
    medium:str
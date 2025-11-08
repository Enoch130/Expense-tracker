from sqlalchemy import Column,String,Integer,Float,DateTime,ForeignKey
from app.database import Base
import uuid # it is the python uuid universally unique identifier
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship




# The user class
class User(Base):
    # giving the table a name
    __tablename__ = "users"
    # defining relevant colums in the table
    id = Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    email = Column(String,unique=True, index = True)
    firstname = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    middlename = Column(String,nullable=True)
    password = Column(String,nullable=False)
    phonenumber = Column(String,nullable=False)
    date_created = Column(DateTime,default=datetime.now)
    transactions = relationship("Transaction", back_populates="owner")




# fkdg
#kf

# gklfv

# transaction model
class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(UUID(as_uuid=True),primary_key=True,index = True,default=uuid.uuid4)
    title = Column(String,nullable=False)
    description = Column(String,nullable=True)
    type = Column(String,nullable=False)
    cost = Column(Float,nullable=False)
    medium = Column(String, nullable=False)
    date_created = Column(DateTime,default=datetime.now)
    date_of_transaction = Column(DateTime,nullable=True)
    owner_id = Column(UUID(as_uuid=True),ForeignKey("users.id"))
    owner = relationship("User",back_populates="transactions")





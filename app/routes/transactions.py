from fastapi import APIRouter,Depends,HTTPException,status
from app.pd_models import TransactionIn,TransactionOut
from sqlalchemy.orm import Session
from app.operations import get_db
from app.db_models import User,Transaction
from operations import fetch_user_by_id
from uuid import UUID
from typing import List




transaction_route = APIRouter(prefix="/transactions",tags=["Transactions Route"])




@transaction_route.post("/create_transaction")  
async def create_transaction(transaction:TransactionIn,db:Session=Depends(get_db)):
    # verify if the user exists before proceeding
    user = fetch_user_by_id(id=transaction.owner_id,dbase=db)
    new_transaction = Transaction(
                        title=transaction.title,
                        description=transaction.description,
                        type=transaction.type,
                        cost=transaction.cost,
                        medium=transaction.medium,
                        owner_id=transaction.owner_id
                        )
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

# endpoint to fetch all transactions of a user by their id
@transaction_route.get("/get_all_user_transactions",response_model=List[TransactionOut])
async def get_transactions(id:UUID,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=id, dbase=db)
    db_transctions = db.query(Transaction).filter(Transaction.owner_id == id).all()
    return db_transctions


@transaction_route.delete("/delete_transaction",response_model=List[TransactionOut])
async def get_transactions(id:UUID,db:Session=Depends(get_db)):
    db_user = fetch_user_by_id(id=id, dbase=db)
    db_transctions = db.query(Transaction).filter(Transaction.owner_id == id).all()
    return db_transctions
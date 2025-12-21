from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi  import status,Response
from fastapi.params import Depends
from ..import schemas
from ..database import get_db # wer have to go 2 directories back.
from ..import models
from passlib.context import CryptContext # by using the we hash the password.


router = APIRouter()

pwd_context = CryptContext(schemes=["argon2"],deprecated="auto") # This will hash the password.



# Route for the sellers.
# Creating the new user.
@router.post('/seller',response_model=schemas.DisplaySeller,tags = ['Sellers']) # the response model is added here.
def create_seller(request:schemas.Seller,db:Session = Depends(get_db)): # now we have access to the database session.
    hashedpassword = pwd_context.hash(request.password) # the hashed password is stored here.
    new_seller = models.Seller(username=request.username,email=request.email,password=hashedpassword)
    db.add(new_seller) # this will add the data to the database.
    db.commit() # commits the data to the database.
    db.refresh(new_seller) # Refreshes the database.
    return new_seller


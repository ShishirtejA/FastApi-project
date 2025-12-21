from fastapi import APIRouter,Depends,status,HTTPException
from ..import schemas,database,models
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..database import get_db
from datetime import datetime,timedelta
from jose import jwt,JWTError
# This file is for creating the login router.

SECRET_KEY = "5b4546aa2072faa19798fcd5f35ea92ae162ff9e849726c5228f0fd231e53529" # secret key for JWT token.
ALGORITHM = "HS256" #algorithm should be defined while generating the JWT Token.
ACCESS_TOKEN_EXPIRE_MINUTES = 20 # token expiry time.

router = APIRouter() # instance is created.
pwd_context = CryptContext(schemes=["argon2"],deprecated="auto") # This will hash the password.

# This is for generating the token.
def generate_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)#This will give the current time.# expiration date
    to_encode.update({"exp":expire}) # updating the encode.
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm = ALGORITHM ) 
    return encoded_jwt
    

@router.post('/login')
def login(request:schemas.Login,db: Session = Depends(get_db)): # It accepts the request...Login schema is given here
    seller = db.query(models.Seller).filter(models.Seller.username == request.username).first()
    if not seller:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = 'Username not found or invalid user')
    if not pwd_context.verify(request.password,seller.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Invalid password")
    # generate JWT Token for the user.
    access_token = generate_token(
        data = {"sub":seller.username} # by this the user gets the token.   
    )
    return {"access_token":access_token,"token_type":"bearer"}
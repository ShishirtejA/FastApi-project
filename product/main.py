from fastapi import FastAPI,Response,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from . import schemas
from . import models
from .database import engine,SessionLocal
from fastapi  import status
from passlib.context import CryptContext # by using the we hash the password.
from .database import get_db
from .routers import product,seller,login
# this file if for creating the routes.
app = FastAPI(
    title = "Products API",
    description="Get details for all the products on the website.",
    terms_of_service="http://www.google.com",
    # docs_url='/documentation' #This changes the docs url,
    redoc_url=None
)


app.include_router(product.router) # this will give us all the routes from the product.
app.include_router(seller.router) # this will give us all the routes from the seller.
app.include_router(login.router) # this will give us all the routes from the login.
models.Base.metadata.create_all(engine) # this is used to create the all the models(models.py) which we created into the dstabase tables.
pwd_context = CryptContext(schemes=["argon2"],deprecated="auto") # This will hash the password.


        
# THE BELOW ARE ALL THE 'CRUD' OPERATIONS.


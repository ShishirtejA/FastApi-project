from pydantic import BaseModel
from typing import Optional

# this file is for creating the pydantic models.

# Request body.
class Product(BaseModel):
    name: str
    description: str
    price: int

# This is the response model for Product.
class DisplayProduct(BaseModel):
    name: str
    description: str
    class config:
        orm_mode = True

class Seller(BaseModel):
    username: str
    email: str
    password: str


# This is the response model for the Seller.
class DisplaySeller(BaseModel):
    username: str
    email: str
    class config:
        orm_mode = True


# This is for the login router.

class Login(BaseModel):
    username: str
    password: str
    
    
# This is for JWT token generation.
class Token(BaseModel):
    acces_token: str
    token_type: str
    
# This holds the username of the token user..
class TokenData(BaseModel):
    username: Optional[str] = None
    
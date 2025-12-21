from sqlalchemy import Column,Integer,String
from .database import Base # This is important.
# This file is for creating the table in the database.
#Creating the table.
# Model->table.

#table in the database.
class Product(Base): # Inherited form the base class.
    __tablename__ = 'products' 
    id = Column(Integer,primary_key=True,index=True) # This is the primary key.
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    
# This is the seller table.
class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
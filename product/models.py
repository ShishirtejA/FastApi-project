from sqlalchemy import Column,Integer,String
from .database import Base # This is important.
from sqlalchemy import ForeignKey # This is to create a foreign key.
from sqlalchemy.orm import relationship # to create the relatonship between 2 models.

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
    seller_id = Column(Integer,ForeignKey('sellers.id'))  # table_name and column are associated here. #Now Foreign key is established.
    seller = relationship('Seller',back_populates='product') # by this the relationship is established between sellers and products.
    
# This is the seller table.
class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    product = relationship('Product',back_populates='seller') # by this the relationship is established between sellers and products.
    
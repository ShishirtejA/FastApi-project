from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi  import status,Response
from fastapi.params import Depends
from ..database import get_db # wer have to go 2 directories back.
from ..import models,schemas

# We use API Routers all the routes cannot be mwntioned in the main.py that would get clumsy..so we use the API Routers and give the routes of all the pydantic models in their corresponding files.

router = APIRouter()

#Here we use router.get,router.post
#Creating the product.
@router.post('/product',status_code=status.HTTP_201_CREATED,tags = ['Products']) # http C0de:-201 i.e the data is added to the database.
def add(request:schemas.Product,db:Session = Depends(get_db)): # now we want to post the data in the database.
    seller = db.query(models.Seller).first()
    if not seller:
        return {"error": "No seller found"}
    new_product = models.Product(name=request.name,description=request.description,price=request.price,seller_id = seller.id)
    db.add(new_product) # This will add it to the database.
    db.commit()
    db.refresh(new_product) # this refreshes the database.
    return request

# To fetch the data from the database.(all)
@router.get('/products',tags = ['Products'])
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all() # this fetches all the rows from the table.
    return products # api response

# To get the single data from the database.
@router.get('/product/{id}',response_model=schemas.DisplayProduct,tags = ['Products']) # by using the response model we only display the neccesary data of the product,unneccesary data of the product is hidden.
def product(id,response:Response,db:Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"product not found"}
    return product

#deleting the data.
@router.delete('/product/{id}',tags = ['Products'])
def delete(id,db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False) # by this the database entry will be deleted.
    db.commit() # saves the changes
    return {'product deleted!!!'}

# #Updating the data.
@router.put('/product/{id}',tags = ['Products'])
def update(id,request:schemas.Product,db: Session = Depends(get_db)): # accepting the request i.e accepting the given data for updating the data.
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product: # If product is not found pass the function,if found update the product.
        pass
    product.update(request.dict()) # the request is passed here i.e the data. 
    db.commit()
    return {"Product successfully updated!!"}

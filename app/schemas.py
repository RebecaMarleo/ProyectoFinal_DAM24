from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class Client(BaseModel):
    nombre:str
    direccion:Optional[str]
    telefono:int
    correo:str

class UpdatedClient(BaseModel):
    nombre:str = None
    direccion:Optional[str] = None
    telefono:int = None
    correo:str = None

class Sale(BaseModel):
    id_cliente:int
    fecha:datetime=datetime.now()
    ultima_modificacion:datetime=datetime.now()

class UpdatedSale(BaseModel):
    id_cliente:int = None
    fecha:datetime = None
    ultima_modificacion:datetime=datetime.now()

class Product(BaseModel):
    nombre:str
    precio:float

class UpdatedProduct(BaseModel):
    nombre:str = None
    precio:float = None

class ProductSale(BaseModel):
    id_venta:int
    id_producto:int

class UpdatedProductSale(BaseModel):
    id_venta:int = None
    id_producto:int = None
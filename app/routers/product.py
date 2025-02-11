from fastapi import APIRouter, Depends
from app.schemas import Product, UpdatedProduct
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)

# obtener
@router.get("")
def obtener_productos(db:Session=Depends(get_db)):
    data = db.query(models.Product).all()
    print(data)
    return data

@router.get("/{product_id}")
def obtener_producto(product_id:int, db:Session=Depends(get_db)):
    producto = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not producto:
        return {"Respuesta": "Producto no encontrado"}
    return producto

# crear
@router.post("")
def crear_producto(product:Product, db:Session=Depends(get_db)):
    producto = product.model_dump()
    nuevo_producto = models.Product(
        nombre = producto["nombre"],
        precio = producto["precio"]
    )
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return {"Respuesta": "Producto creado con éxito"}

# modificar
@router.patch("/{product_id}")
def actualizar_producto(product_id:int, updatedProduct:UpdatedProduct, db:Session=Depends(get_db)):
    producto = db.query(models.Product).filter(models.Product.id == product_id)
    if not producto.first():
        return {"Respuesta": "Producto no encontrado"}
    producto.update(updatedProduct.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Producto actualizado con éxito"}

# eliminar
@router.delete("/{product_id}")
def eliminar_producto(product_id:int, db:Session=Depends(get_db)):
    producto = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not producto:
        return {"Respuesta": "Producto no encontrado"}
    db.delete(producto)
    db.commit()
    return {"Respuesta": "Producto eliminado con éxito"}
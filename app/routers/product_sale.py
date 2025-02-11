from fastapi import APIRouter, Depends
from app.schemas import ProductSale, UpdatedProductSale
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/product-sale",
    tags=["Product sale"]
)

# obtener
@router.get("")
def obtener_productos_ventas(db:Session=Depends(get_db)):
    data = db.query(models.Product_Sale).all()
    print(data)
    return data

@router.get("/{product_sale_id}")
def obtener_producto_venta(product_sale_id:int, db:Session=Depends(get_db)):
    producto_venta = db.query(models.Product_Sale).filter(models.Product_Sale.id == product_sale_id).first()
    if not producto_venta:
        return {"Respuesta": "Relación producto-venta no encontrada"}
    return producto_venta

# crear
@router.post("")
def crear_producto_venta(product_sale:ProductSale, db:Session=Depends(get_db)):
    producto_venta = product_sale.model_dump()
    nuevo_producto_venta = models.Product_Sale(
        id_venta = producto_venta["id_venta"],
        id_producto = producto_venta["id_producto"]
    )
    db.add(nuevo_producto_venta)
    db.commit()
    db.refresh(nuevo_producto_venta)
    return {"Respuesta": "Relación producto-venta creada con éxito"}

# modificar
@router.patch("/{product_sale_id}")
def actualizar_producto_venta(product_sale_id:int, updatedProductSale:UpdatedProductSale, db:Session=Depends(get_db)):
    producto_venta = db.query(models.Product_Sale).filter(models.Product_Sale.id == product_sale_id)
    if not producto_venta.first():
        return {"Respuesta": "Relación producto-venta no encontrada"}
    producto_venta.update(updatedProductSale.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Relación producto-venta actualizada con éxito"}

# eliminar
@router.delete("/{product_sale_id}")
def eliminar_producto_venta(product_sale_id:int, db:Session=Depends(get_db)):
    producto_venta = db.query(models.Product_Sale).filter(models.Product_Sale.id == product_sale_id).first()
    if not producto_venta:
        return {"Respuesta": "Relación producto-venta no encontrada"}
    db.delete(producto_venta)
    db.commit()
    return {"Respuesta": "Relación producto-venta con éxito"}
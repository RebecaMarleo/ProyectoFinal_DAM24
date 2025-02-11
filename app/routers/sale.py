from fastapi import APIRouter, Depends
from app.schemas import Sale, UpdatedSale
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/sale",
    tags=["Sale"]
)

# obtener
@router.get("")
def obtener_ventas(db:Session=Depends(get_db)):
    data = db.query(models.Sale).all()
    print(data)
    return data

@router.get("/{sale_id}")
def obtener_venta(sale_id:int, db:Session=Depends(get_db)):
    venta = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not venta:
        return {"Respuesta": "Venta no encontrada"}
    return venta

# crear
@router.post("")
def crear_venta(sale:Sale, db:Session=Depends(get_db)):
    venta = sale.model_dump()
    nueva_venta = models.Sale(
        id_cliente = venta["id_cliente"],
        fecha = venta["fecha"],
        ultima_modificacion = venta["ultima_modificacion"]
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return {"Respuesta": "Venta creada con éxito"}

# modificar
@router.patch("/{sale_id}")
def actualizar_venta(sale_id:int, updatedSale:UpdatedSale, db:Session=Depends(get_db)):
    venta = db.query(models.Sale).filter(models.Sale.id == sale_id)
    if not venta.first():
        return {"Respuesta": "Venta no encontrada"}
    venta.update(updatedSale.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Venta actualizada con éxito"}

# eliminar
@router.delete("/{sale_id}")
def eliminar_venta(sale_id:int, db:Session=Depends(get_db)):
    venta = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if not venta:
        return {"Respuesta": "Venta no encontrada"}
    db.delete(venta)
    db.commit()
    return {"Respuesta": "Venta eliminada con éxito"}
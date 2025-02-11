from fastapi import APIRouter, Depends
from app.schemas import Client, UpdatedClient
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models
from typing import List

router = APIRouter(
    prefix="/client",
    tags=["Client"]
)

# obtener
@router.get("")
def obtener_clientes(db:Session=Depends(get_db)):
    data = db.query(models.Client).all()
    print(data)
    return data

@router.get("/{client_id}")
def obtener_cliente(client_id:int, db:Session=Depends(get_db)):
    cliente = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not cliente:
        return {"Respuesta": "Cliente no encontrado"}
    return cliente

# crear
@router.post("")
def crear_cliente(client:Client, db:Session=Depends(get_db)):
    cliente = client.model_dump()
    # clientes.append(cliente)
    nuevo_cliente = models.Client(
        nombre = cliente["nombre"],
        direccion = cliente["direccion"],
        telefono = cliente["telefono"],
        correo = cliente["correo"]
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return {"Respuesta": "Cliente creado con éxito"}

# modificar
@router.patch("/{client_id}")
def actualizar_cliente(client_id:int, updatedClient:UpdatedClient, db:Session=Depends(get_db)):
    cliente = db.query(models.Client).filter(models.Client.id == client_id)
    if not cliente.first():
        return {"Respuesta": "Cliente no encontrado"}
    cliente.update(updatedClient.model_dump(exclude_unset=True))
    db.commit()
    return {"Respuesta": "Cliente actualizado con éxito"}

# eliminar
@router.delete("/{client_id}")
def eliminar_cliente(client_id:int, db:Session=Depends(get_db)):
    cliente = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not cliente:
        return {"Respuesta": "Cliente no encontrado"}
    db.delete(cliente)
    db.commit()
    return {"Respuesta": "Cliente eliminado con éxito"}
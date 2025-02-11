from app.db.database import Base
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__ = "cliente"
    id = Column(Integer,primary_key=True,autoincrement=True)
    nombre = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String)
    venta = relationship("Sale",backref="cliente",cascade="delete,merge")

class Sale(Base):
    __tablename__ = "venta"
    id = Column(Integer,primary_key=True,autoincrement=True)
    id_cliente = Column(Integer,ForeignKey("cliente.id",ondelete="CASCADE"))
    productos = relationship("Product_Sale",backref="venta",cascade="delete,merge")
    fecha = Column(DateTime,default=datetime.now)
    ultima_modificacion = Column(DateTime,default=datetime.now,onupdate=datetime.now)

class Product(Base):
    __tablename__ = "producto"
    id = Column(Integer,primary_key=True,autoincrement=True)
    ventas = relationship("Product_Sale", backref="producto",cascade="delete,merge")
    nombre = Column(String)
    precio = Column(Float)

class Product_Sale(Base):
    __tablename__ = "producto_venta"
    id = Column(Integer,primary_key=True,autoincrement=True)
    id_venta = Column(Integer,ForeignKey("venta.id",ondelete="CASCADE"))
    id_producto = Column(Integer, ForeignKey('producto.id'))
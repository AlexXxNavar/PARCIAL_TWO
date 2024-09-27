from sqlalchemy import Column, Integer, String, Date, Time, Enum, ForeignKey, Boolean
from sqlalchemy.types import DECIMAL
from sqlalchemy.orm import relationship
from .conexion import Base

#Modelo de empleados
class Empleados(Base):
    __tablename__ = 'empleados'
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), index=True)
    apellido = Column(String(100), index=True)
    email = Column(String(100), index=True)
    telefono = Column(String(100), index=True)
    direccion = Column(String(100), index=True)
    puesto = Column(String(100), index=True)
    salario = Column(DECIMAL(10,2), index=True)

from pydantic import BaseModel
from typing import Optional
from datetime import date, time
import enum
from decimal import Decimal

#Esquema de empleado
class EmpleadoBase(BaseModel):
    nombre : str
    apellido : str
    email : str
    telefono : str
    direccion : str
    puesto : str
    salario : Decimal
    
    class Config: 
         from_attributes = True
         
class Empleado(EmpleadoBase):
    id_empleado : int
    
    class Config: 
         from_attributes = True
         

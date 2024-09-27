from sqlalchemy.orm import Session
from .models import Empleados
from .schemas import EmpleadoBase

#CRUD de empleados
def get_empleado(db: Session):
    return db.query(Empleados).all()

def get_empleado_by_id(db: Session, id_empleado: int):
    return db.query(Empleados).filter(Empleados.id_empleado == id_empleado).first()

def create_empleado(db: Session, empleado: EmpleadoBase):
    new_empleado = Empleados(empleado=empleado.nombre, apellido=empleado.apellido, email=empleado.email, telefono=empleado.telefono, direccion=empleado.direccion, puesto=empleado.puesto, salario=empleado.salario)
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado

def create_empleado(db: Session, empleado: EmpleadoBase):
    new_empleado = Empleados(
        nombre=empleado.nombre,
        apellido=empleado.apellido,
        email=empleado.email,
        telefono=empleado.telefono,
        direccion=empleado.direccion,
        puesto=empleado.puesto,
        salario=empleado.salario
    )
    db.add(new_empleado)
    db.commit()
    db.refresh(new_empleado)
    return new_empleado


def delete_empleado(db: Session, id_empleado: int):
    db_empleado = db.query(Empleados).filter(Empleados.id_empleado == id_empleado).first()
    if db_empleado:
        db.delete(db_empleado)
        db.commit()
    return db_empleado


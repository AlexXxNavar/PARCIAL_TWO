from typing import Annotated, List
from starlette.responses import RedirectResponse
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from . import crud
from .conexion import SessionLocal, engine
from .schemas import EmpleadoBase, Empleado
from .models import Base
from datetime import datetime, timedelta
from fastapi.responses import JSONResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Ruta de inicio
@app.get('/')
def inicio():
    return RedirectResponse(url='/docs/')

#Rutas de empleados
@app.get('/empleadosObtener/', response_model=List[Empleado])
def empleados_obtener(db: Session = Depends(get_db)):
    empleados = crud.get_empleado(db)
    return empleados

@app.get('/empleadosObtener/{id_empleado}', response_model=Empleado)
def empleado_obtener(id_empleado: int, db: Session = Depends(get_db)):
    empleado = crud.get_empleado_by_id(db, id_empleado)
    if empleado is None:
        return empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")

@app.post('/empleadosCrear/', response_model=Empleado)
def empleado_crear(empleado: EmpleadoBase, db: Session = Depends(get_db)):
    return crud.create_empleado(db, empleado)

@app.put('/empleadosActualizar/{id_empleado}', response_model=Empleado)
def actualizar_empleado(id_empleado: int, empleado: EmpleadoBase, db: Session = Depends(get_db)):
    actualizar_empleado = crud.update_empleado(db, id_empleado, empleado=empleado)
    if actualizar_empleado is None:
        return actualizar_empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")

@app.delete('/empleadosEliminar/{id_empleado}', response_model=Empleado)
def eliminar_empleado(id_empleado: int, db: Session = Depends(get_db)):
    eliminar_empleado = crud.delete_empleado(db, id_empleado)
    if eliminar_empleado is None:
        return eliminar_empleado
    raise HTTPException(status_code=404, detail="El empleado con el id {id_empleado} no se encuentra en la base de datos")


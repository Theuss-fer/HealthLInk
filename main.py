from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Hospitalar API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/hospitals", response_model=list[schemas.HospitalResponse])
def list_hospitals(db: Session = Depends(get_db)):
    return db.query(models.Hospital).all()


@app.get("/hospitals/{hospital_id}", response_model=schemas.HospitalResponse)
def get_hospital(hospital_id: int, db: Session = Depends(get_db)):
    hospital = db.query(models.Hospital).filter(
        models.Hospital.id == hospital_id
    ).first()

    if not hospital:
        raise HTTPException(status_code=404, detail="Hospital não encontrado")

    return hospital


@app.get("/hospitals/nearby", response_model=list[schemas.HospitalResponse])
def nearby_hospitals(lat: float, lng: float, db: Session = Depends(get_db)):
    return crud.get_nearby_hospitals(db, lat, lng)


@app.post("/hospitals", response_model=schemas.HospitalResponse)
def create_hospital(hospital: schemas.HospitalBase, db: Session = Depends(get_db)):
    new_hospital = models.Hospital(**hospital.dict())
    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)
    return new_hospital

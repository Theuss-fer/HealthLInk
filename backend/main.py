from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from database import SessionLocal, engine
import models
import schemas
import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema Hospitalar API")


# ---------- DATABASE DEPENDENCY ----------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- AUTH ROUTES ----------

@app.post("/register", response_model=schemas.Token)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    hashed_password = auth.get_password_hash(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    access_token = auth.create_access_token(
        data={"sub": new_user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}


from fastapi.security import OAuth2PasswordRequestForm

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(
        models.User.email == form_data.username
    ).first()

    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    if not auth.verify_password(form_data.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    access_token = auth.create_access_token(
        data={"sub": db_user.email}
    )

    return {"access_token": access_token, "token_type": "bearer"}


# ---------- HOSPITAL ROUTES ----------

@app.get("/hospitals", response_model=list[schemas.HospitalResponse])
def list_hospitals(db: Session = Depends(get_db)):
    return db.query(models.Hospital).all()


@app.post("/hospitals", response_model=schemas.HospitalResponse)
def create_hospital(
    hospital: schemas.HospitalBase,
    db: Session = Depends(get_db),
    current_user = Depends(auth.get_current_user)  # 🔒 protegida
):
    new_hospital = models.Hospital(**hospital.dict())
    db.add(new_hospital)
    db.commit()
    db.refresh(new_hospital)
    return new_hospital

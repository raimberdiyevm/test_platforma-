from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Savol

router = APIRouter(prefix="/savollar", tags=["Savollar"])

# Database ulanishi
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1️⃣ API: Barcha savollarni olish
@router.get("/")
def get_savollar(db: Session = Depends(get_db)):
    return db.query(Savol).all()

# 2️⃣ API: ID bo‘yicha bitta savol olish
@router.get("/{savol_id}")
def get_savol(savol_id: int, db: Session = Depends(get_db)):
    return db.query(Savol).filter(Savol.id == savol_id).first()

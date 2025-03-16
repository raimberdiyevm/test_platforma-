from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.database import SessionLocal
from app.models import Savol, Natija

router = APIRouter(prefix="/test", tags=["Test"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3️⃣ API: Test uchun tasodifiy 25 ta savolni olish
@router.get("/")
def get_test(db: Session = Depends(get_db)):
    savollar = db.query(Savol).order_by(func.random()).limit(25).all()
    if not savollar:
        raise HTTPException(status_code=404, detail="Savollar topilmadi")
    return savollar

# 4️⃣ API: Test natijasini hisoblash va bazaga saqlash
@router.post("/natija")
def check_test(ism: str, javoblar: dict, db: Session = Depends(get_db)):
    togri_soni = 0
    jami_savollar = len(javoblar)

    for savol_id, user_javob in javoblar.items():
        savol = db.query(Savol).filter(Savol.id == int(savol_id)).first()
        if savol and savol.togri_javob == user_javob:
            togri_soni += 1

    natija_text = "O'tdingiz" if togri_soni >= 15 else "Yiqildingiz"

    # Natijani bazaga saqlash
    yangi_natija = Natija(ism=ism, togrilar=togri_soni, jami_savollar=jami_savollar, natija=natija_text)
    db.add(yangi_natija)
    db.commit()

    return {"ism": ism, "togri": togri_soni, "jami_savollar": jami_savollar, "natija": natija_text}

# 5️⃣ API: Barcha natijalarni olish
@router.get("/natijalar")
def barcha_natijalar(db: Session = Depends(get_db)):
    return db.query(Natija).all()

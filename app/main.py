from fastapi import FastAPI
from app.routers import savollar, test # type: ignore
from app.database import engine
from app.models import Base

# Barcha jadvallarni yaratish
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Savollar API", description="Test tizimi uchun API")

# Routerlarni ulash
app.include_router(savollar.router)
app.include_router(test.router)

@app.get("/")
def home():
    return {"message": "FastAPI ishlayapti! 🚀"}

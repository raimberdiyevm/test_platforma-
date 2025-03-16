from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.database import Base

class Savol(Base):
    __tablename__ = "savollar"

    id = Column(Integer, primary_key=True, index=True)
    matn = Column(String, nullable=False)
    variant_a = Column(String, nullable=False)
    variant_b = Column(String, nullable=False)
    variant_c = Column(String, nullable=False)
    variant_d = Column(String, nullable=False)
    togri_javob = Column(String, nullable=False)

class Natija(Base):
    __tablename__ = "natijalar"

    id = Column(Integer, primary_key=True, index=True)
    ism = Column(String(100), nullable=False)
    togrilar = Column(Integer, nullable=False)
    jami_savollar = Column(Integer, nullable=False)
    natija = Column(String(10), nullable=False)
    sana = Column(TIMESTAMP, server_default=func.now())

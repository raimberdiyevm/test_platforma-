from app.database import SessionLocal

try:
    db = SessionLocal()
    print("✅ Bazaga muvaffaqiyatli ulandik!")
    db.close()
except Exception as e:
    print(f"❌ Xatolik yuz berdi: {e}")

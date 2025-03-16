from app.database import SessionLocal
from app.models import Savol
from parse_docx import parse_docx

def insert_savollar(file_path):
    db = SessionLocal()
    savollar = parse_docx(file_path)

    if not savollar:
        print("❌ Xatolik: Hech qanday savol topilmadi!")
        return

    for savol in savollar:
        if len(savol["variantlar"]) < 4:
            print(f"⚠ Xatolik: Kamida 4 ta variant bo‘lishi kerak! {savol}")
            continue

        new_savol = Savol(
            matn=savol["matn"],
            variant_a=savol["variantlar"][0]["javob"],
            variant_b=savol["variantlar"][1]["javob"],
            variant_c=savol["variantlar"][2]["javob"],
            variant_d=savol["variantlar"][3]["javob"],
            togri_javob=[v["javob"] for v in savol["variantlar"] if v["togri"]][0]
        )
        db.add(new_savol)
    
    db.commit()
    db.close()
    print(f"✅ {len(savollar)} ta savol bazaga muvaffaqiyatli yuklandi!")

# Faylni yuklash
file_path = "bdoc.docx"
insert_savollar(file_path)

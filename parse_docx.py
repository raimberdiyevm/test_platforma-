from docx import Document

def parse_docx(file_path):
    doc = Document(file_path)
    savollar = []
    current_savol = None
    javoblar = []

    for para in doc.paragraphs:
        text = para.text.strip()

        if text.startswith("+++++"):  # Yangi savol boshlanishi
            if current_savol and javoblar:
                current_savol["variantlar"] = javoblar
                savollar.append(current_savol)
            current_savol = {"matn": ""}
            javoblar = []

        elif text.startswith("#"):  # To‘g‘ri javob
            javoblar.append({"javob": text[1:].strip(), "togri": True})
        elif text.startswith("="):  # Variantlar
            javoblar.append({"javob": text.replace("=", "").strip(), "togri": False})
        elif text:  # Savol matni
            current_savol["matn"] = text

    if current_savol and javoblar:
        current_savol["variantlar"] = javoblar
        savollar.append(current_savol)

    return savollar

# Test qilish
file_path = "bdoc.docx"
parsed_savollar = parse_docx(file_path)

if parsed_savollar:
    for i, savol in enumerate(parsed_savollar[:5], 1):
        print(f"{i}) {savol}")
else:
    print("❌ Xatolik: Hech qanday savol topilmadi! `.docx` formatini tekshiring!")

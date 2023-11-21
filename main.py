from docx_functions import modify_docx

# Применяем функцию к каждому документу
documents = ["doc1.docx", "doc2.docx", "doc3.docx", "doc4.docx", "doc5.docx"]

for doc_path in documents:
    modify_docx(doc_path)
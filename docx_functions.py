from docx import Document
from docx.shared import Pt

def modify_docx(file_path):
    # Открываем документ
    doc = Document(file_path)

    # Изменяем шрифт, размер шрифта и межстрочный интервал для каждого параграфа
    for para in doc.paragraphs:
        for run in para.runs:
            run.font.name = 'Times New Roman'
            run.font.size = Pt(14)
        para.paragraph_format.line_spacing = 1.5

    # Сохраняем изменения
    doc.save(file_path)
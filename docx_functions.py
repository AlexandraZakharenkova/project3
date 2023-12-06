# Импортируем необходимые модули
from docx import Document

# Определяем функцию для изменения параметров шрифта и межстрочного интервала
def change_font_and_spacing(file_path, font_name, font_size, line_spacing):
    # Открываем файл
    doc = Document(file_path)

    # Изменяем параметры шрифта и межстрочного интервала
    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = font_size
        paragraph.paragraph_format.line_spacing = line_spacing

    # Сохраняем изменения
    doc.save(file_path)
# Изменение шрифта, размера шрифта и межстрочного интервала в документе

Этот скрипт позволяет изменить шрифт, размер шрифта и межстрочный интервал в документе формата docx. Он применяется к нескольким документам одновременно.

## Использование

1. Установите необходимые зависимости с помощью следующей команды:

pip install python-docx


2. Скопируйте скрипт в свой проект.

3. Укажите пути к документам, которые необходимо изменить, в переменной `documents`. Документы должны быть в формате docx.

4. Запустите скрипт.

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

# Применяем функцию к каждому документу
documents = ["doc1.docx", "doc2.docx", "doc3.docx", "doc4.docx", "doc5.docx"]

for doc_path in documents:
    modify_docx(doc_path)


## Зависимости

Для работы скрипта необходимо установить следующую зависимость:
- python-docx: `pip install python-docx`

## Лицензия

Этот проект распространяется под лицензией [MIT License](LICENSE).
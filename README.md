# Изменение шрифта, размера шрифта и межстрочного интервала в документе

Данная программа позволяет модифицировать документы в формате docx, изменяя шрифт, размер шрифта и межстрочный интервал для каждого параграфа.

## Установка и использование

1. Установите библиотеку `python-docx`, если она ещё не установлена:

   pip install python-docx

2. Создайте файл `main.py` со следующим содержимым:

    from docx_functions import modify_docx

    # Применяем функцию к каждому документу
    documents = ["doc1.docx", "doc2.docx", "doc3.docx", "doc4.docx", "doc5.docx"]

    for doc_path in documents:
        modify_docx(doc_path)

3. Создайте файл `docx_functions.py` со следующим содержимым:

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

4. Запустите файл `main.py`, чтобы применить функцию `modify_docx` к каждому документу из списка `documents`.

   python main.py

   Документы будут изменены в соответствии с заданными параметрами.

## Примечание

- Для работы программы требуется библиотека `python-docx`. Убедитесь, что она установлена перед запуском программы.

- Документы, которые требуется модифицировать, должны находиться в одной директории с файлом `main.py`.

- Перед запуском программы убедитесь, что у вас есть права на изменение указанных документов.
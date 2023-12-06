# Изменение параметров шрифта и межстрочного интервала в документах Word

Данный код представляет собой Python скрипт, который позволяет изменять параметры шрифта и межстрочного интервала в документах формата docx. 

## Установка

Для работы скрипта необходимо установить несколько зависимостей. Выполните следующие команды:

```bash
pip install python-docx
```

## Использование

1. Импортируйте необходимые библиотеки и модули:

```python
import os
from docx import Document
from docx_functions import change_font_and_spacing
```

2. Укажите путь к папке с файлами, которые нужно изменить:

```python
folder = 'путь_к_папке_с_файлами'
```

3. Установите необходимые параметры для изменения:

```python
font_name = 'times new roman'
font_size = 14
line_spacing = 1.5
```

4. Проходимся по всем файлам в указанной папке и вызываем функцию для изменения параметров шрифта и межстрочного интервала:

```python
for filename in os.listdir(folder):
    if filename.endswith('.docx'):
        file_path = os.path.join(folder, filename)
        change_font_and_spacing(file_path, font_name, font_size, line_spacing)
        print(f'документ "{filename}" успешно изменен.')
```

## Функция `change_font_and_spacing`

Функция `change_font_and_spacing` определена во втором файле `docx_functions.py` и выполняет поставленные действия. Для использования данной функции, импортируйте необходимые модули:

```python
from docx import Document
```

Пример вызова функции:

```python
doc = Document('путь_к_файлу.docx')
change_font_and_spacing(doc, font_name, font_size, line_spacing)
doc.save('путь_к_файлу.docx')
```

Функция принимает следующие параметры:

- `file_path`: путь к файлу docx
- `font_name`: имя шрифта
- `font_size`: размер шрифта
- `line_spacing`: межстрочный интервал

Функция открывает файл, изменяет параметры шрифта и межстрочного интервала для каждого параграфа и сохраняет изменения в исходном файле.
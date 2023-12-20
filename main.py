# Импортируем необходимые библиотеки и модули
import os
from docx import Document

# Импортируем функции из второго файла
from docx_functions import change_font_and_spacing

# Указываем папку с файлами
folder = 'files'

# Указываем параметры для изменения
font_name = 'times new roman'
font_size = 14
line_spacing = 1.5

# Проходимся по всем файлам в папке
for filename in os.listdir(folder):
    if filename.endswith('.docx'):
        file_path = os.path.join(folder, filename)

        # Вызываем функцию для изменения параметров шрифта и межстрочного интервала
        change_font_and_spacing(file_path, font_name, font_size, line_spacing)

        print(f'документ \"{filename}\" успешно изменен.')

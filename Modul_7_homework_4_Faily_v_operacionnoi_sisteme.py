import os

directory = 'C:\\Windows\\help'

# Используем os.walk для обхода каталога, путь к которому указывает переменная directory
for dirpath, dirnames, filenames in os.walk(directory):
    print(dirpath, dirnames, filenames)

os.path.join(directory) # Применяем os.path.join для формирования полного пути к файлам.

os.path.getmtime(directory) # Получаем дату модификации файла.

os.path.getsize(directory) # Получаем размера файла.

os.path.dirname(directory) # получить родительскую директорию

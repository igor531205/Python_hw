# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


import os


def convert_path_to_tuple(_full_path: str) -> tuple:
    """Функция транспонирования абсолютного пути до файла в кортеж из трёх элементов."""

    path_to_file, full_filename = os.path.split(_full_path)
    file_name, file_extension = full_filename.split('.')

    return path_to_file, file_name, file_extension


FULL_PATH = 'C:\Windows\win.ini'

print(f'{FULL_PATH=} {convert_path_to_tuple(FULL_PATH)=}')

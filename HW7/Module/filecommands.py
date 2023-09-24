import os


def create_files(number_of_files: int, extension: str, directory: str = os.getcwd()):

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        with open(f'{directory}/text_file{i}.{extension}', 'w+', encoding='utf-8') as f:
            f.write(f'{directory}/text_file{i}.{extension}')


def rename_files(final_name: str, number_of_digits: int, orig_extension: str, final_extension: str,
                 orig_name_range: list, directory: str = os.getcwd()):
    """Функция группового переименования файлов.

    :param final_name: желаемое конечное имя файлов (при переименовании в конце имени добавляется порядковый номер).
    :param number_of_digits: количество цифр в порядковом номере.
    :param orig_extension: расширение исходного файла (Переименование должно работать только для этих файлов).
    :param final_extension: расширение конечного файла.
    :param orig_name_range: диапазон сохраняемого оригинального имени (для диапазона [3, 6] берутся буквы с 3 по 6,
    к ним прибавляется желаемое конечное имя, если оно передано, далее счётчик файлов и расширение).
    :param directory: директория (по-умолчанию текущая).
    """

    count = 0
    for file in os.listdir(directory):

        if file.endswith(orig_extension):

            count += 1
            os.rename(f'{directory}/{file}',
                      f'{directory}/{file.split(".")[0][orig_name_range[0]:orig_name_range[1]]}' +
                      f'{final_name}{count:0>{number_of_digits}}.{final_extension}')

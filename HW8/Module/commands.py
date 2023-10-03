import os
import json
import csv
import pickle


def folder_crawl(directory: str = os.getcwd()):
    """Функция обхода директории.

    :param directory: директория (по-умолчанию текущая).
    """
    print(directory)
    pass
    result = []
    for root, dirs, files in os.walk(directory):

        dir_size = 0
        for file in files:

            file_path = os.path.join(root, file)
            size = os.path.getsize(file_path)
            dir_size += size
            result.append({'path': file_path, 'type': 'file', 'size': size, 'parent_directory': root})

        result.append({'path': root, 'type': 'directory', 'size': dir_size, 'parent_directory': os.path.dirname(root)})

    with open('result.json', 'w') as json_file:

        json.dump(result, json_file, indent=1)

    with open('result.csv', 'w', newline='') as csv_file:

        writer = csv.DictWriter(csv_file, fieldnames=['path', 'type', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(result)

    with open('result.pickle', 'wb') as pickle_file:

        pickle.dump(result, pickle_file)

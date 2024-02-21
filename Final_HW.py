# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
from collections import namedtuple
import logging

# Настройка логирования
logging.basicConfig(filename='directory_info.log',
                    filemode='w',
                    encoding='utf-8',
                    level=logging.INFO
                    )
logger = logging.getLogger(__name__)

# Определение объекта namedtuple для хранения информации
FSObject = namedtuple('FSObject', ['name', 'ext', 'is_dir', 'parent'])


def collect_directory_info(directory_path):
    try:
        # Создание пустого списка для хранения объектов FSObject
        fs_objects = []

        # Получение абсолютного пути
        path_string = os.path.abspath(directory_path)

        # Итерация по содержимому директории
        for item in os.listdir(path_string):
            obj_name, obj_ext = None, None
            item_path = os.path.join(path_string, item)

            if os.path.isfile(item_path):
                # Если это файл, разделяем имя и расширение
                obj_name, obj_ext = os.path.splitext(item)
            else:
                # Если это каталог, устанавливаем расширение как None
                obj_name = item
                obj_ext = None

            # Создание объекта FSObject и добавление его в список
            fs_objects.append(FSObject(name=obj_name, ext=obj_ext, is_dir=os.path.isdir(item_path), parent=path_string))

            # Запись информации в лог
            logging.info(f"{fs_objects[-1]}")

        # Возвращение списка объектов FSObject
        return fs_objects

    except Exception as exc:
        # Обработка исключений и запись ошибки в лог
        logging.error(f"Error: {exc}")
        return None


if __name__ == "__main__":
    import sys

    # Получение пути из командной строки
    if len(sys.argv) != 2:
        print('Final_HW.py', collect_directory_info('C:\\Users\\liz-f\\OneDrive\\Рабочий стол'))
        sys.exit(1)

    directory_path = sys.argv[1]

    # Вызов функции и вывод результата
    result = collect_directory_info(directory_path)
    if result:
        print("Directory information collected successfully.")
    else:
        print("An error occurred. Check the log file for details.")
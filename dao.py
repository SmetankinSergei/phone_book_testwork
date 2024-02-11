import json
import os
from typing import List, Union, Dict, Any


def write_new_entry(data: str) -> None:
    """
        Добавляет новую запись в файл книги.
        :return: None
    """
    path: str = os.path.join('src', 'phone_book.json')
    with open(path, 'a') as data_file:
        entry_id: str = str(len(get_data()) + 1)
        data_file.write('{"id": ' + entry_id + ', ' + '"data": ' + data + '}' + ',\n')


def write_all_data(data: Union[List[Dict[str, Any]], List[str]]) -> None:
    """
        Перезаписывает весь файл книги новыми данными.
        :param data: Новые данные для записи в файл
        :return: None
    """
    path: str = os.path.join('src', 'phone_book.json')
    with open(path, 'w'):
        pass
    for entry in data:
        update_entry(json.dumps(entry))


def update_entry(entry: str) -> None:
    """
        Обновляет запись в файле книги.
        :return: None
    """
    path: str = os.path.join('src', 'phone_book.json')
    with open(path, 'a') as data_file:
        data_file.write(entry + ',\n')


def get_data() -> List[str]:
    """
        Получает все данные из файла книги.
        :return: Список строк, содержащих данные записей из файла
    """
    path: str = os.path.join('src', 'phone_book.json')
    with open(path, 'r') as data_file:
        return data_file.readlines()

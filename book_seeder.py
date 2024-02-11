from random import randint, choice
from string import ascii_lowercase
from typing import List

from entry import Entry


def seed(amount: int) -> None:
    """
        Генерирует указанное количество записей и записывает их в файл.
        :param amount: Количество записей, которые нужно сгенерировать
    """
    entries: List[Entry] = []
    for _ in range(amount):
        first_name: str = generate_name()
        last_name: str = generate_name()
        middle_name: str = generate_name()
        organization: str = generate_name()
        org_phone: str = generate_phone()
        personal_phone: str = generate_phone()
        entries.append(Entry(first_name, last_name, middle_name, organization, org_phone, personal_phone))
    for entry in entries:
        entry.write_to_file()


def generate_name() -> str:
    """
        Генерирует случайное имя переменной длины и возвращает его.
        :return: Случайно сгенерированное имя
    """
    name_length: int = randint(4, 10)
    name: str = ''
    for _ in range(name_length):
        name += choice(ascii_lowercase)
    return name.capitalize()


def generate_phone() -> str:
    """
        Генерирует случайный телефонный номер и возвращает его.
        :return: Случайно сгенерированный телефонный номер
    """
    phone: str = '+7-9'
    for i in range(12):
        if i in [2, 6, 9]:
            phone += '-'
        else:
            phone += str(randint(0, 9))
    return phone


# seed(100)

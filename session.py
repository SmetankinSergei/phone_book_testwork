import json
from math import ceil
from typing import Dict, Any, Tuple, List, Optional

import dao
from constants import PARAMETERS_NAMES, PARAMETER_MESSAGE, PARAMETERS, SEARCH_MESSAGE, SEARCH_OPTIONS
from entry import Entry


class Session:
    def __init__(self) -> None:
        self.__book_data: List[str] = dao.get_data()
        self.__search_actions: Dict[Tuple[str, ...], Any] = {('id',): self.__search_by_id,
                                                             tuple(PARAMETERS): self.__search_by_one_parameter,
                                                             ('all',): self.__search_by_all_parameters}

    def show_page(self) -> None:
        """
            Отображает содержимое страницы с записями из книги.
            :return: None
        """
        self.__book_data: List[str] = dao.get_data()
        entries_amount: int = self.get_number('entries on page amount', len(self.__book_data))
        max_page: int = ceil(len(self.__book_data) / entries_amount)
        num_page: int = self.get_number('page number', max_page)
        if num_page == max_page:
            entries_amount_on_last_page: int = len(self.__book_data) - ((max_page - 1) * entries_amount)
            entries: List[Any] = [Entry.get_entry_by_data(self.__book_data[i].strip(',\n'))
                                  for i in range((num_page - 1) * entries_amount,
                                                 (num_page - 1) * entries_amount + entries_amount_on_last_page)]
        else:
            entries = [Entry.get_entry_by_data(self.__book_data[i].strip(',\n'))
                       for i in range((num_page - 1) * int(entries_amount), num_page * entries_amount)]
        print(f'\nPAGE №{num_page}')
        for entry in entries:
            entry['entry'].show_console_version(entry)

    def search_entry(self) -> None:
        """
           Выполняет поиск записей в книге по заданным критериям.
           :return: None
        """
        self.__book_data: List[str] = dao.get_data()
        option: str = SEARCH_OPTIONS[self.get_number('option number', 8, SEARCH_MESSAGE)]
        keyword: str = input('Enter a keyword to search --> ')
        for key in self.__search_actions:
            if option in key:
                self.__search_actions[key](keyword, option)

    def __search_by_id(self, keyword: str, option: Optional[str] = None) -> None:
        """
            Выполняет поиск записей в книге по идентификатору.
            :param keyword: Ключевое слово для поиска
            :param option: опциональный параметр, не используется в этом методе
            :return: None
        """
        for entry in self.__book_data:
            entry = json.loads(entry.strip(',\n'))
            if entry['id'] == int(keyword):
                self.__show_entry(entry)
                return
        print('\nThere is no entry with this id')

    def __search_by_one_parameter(self, keyword: str, option: str) -> None:
        result_list: List[Any] = []
        for entry in self.__book_data:
            entry = json.loads(entry.strip(',\n'))
            if keyword.lower() in entry['data'][option].lower():
                result_list.append(entry)
        if result_list:
            for entry in result_list:
                self.__show_entry(entry)
        else:
            print('\nNothing found')

    def __search_by_all_parameters(self, keyword: str, option: Optional[str] = None) -> None:
        """
            Выполняет поиск записей в книге по одному параметру.
            :param keyword: Ключевое слово для поиска
            :param option: параметр, по которому будет выполняться поиск
            :return: None
        """
        result_list: List[Any] = []
        search_parameters: List[str] = PARAMETERS
        for entry in self.__book_data:
            entry = json.loads(entry.strip(',\n'))
            if keyword.isdigit() and entry['id'] == int(keyword):
                result_list.append(entry)
                continue
            for parameter in search_parameters:
                if keyword.lower() in str(entry['data'][parameter]).lower():
                    result_list.append(entry)
                    break
        if result_list:
            for entry in result_list:
                self.__show_entry(entry)
        else:
            print('\nNothing found')

    def update_entry(self) -> None:
        """
            Обновляет запись в книге.
            :return: None
        """
        self.__book_data: List[str] = dao.get_data()
        entry_id: int = self.get_number('entry id', len(self.__book_data))
        parameter_name_number: int = self.get_number('parameter number', 6, PARAMETER_MESSAGE)
        parameter: str = PARAMETERS_NAMES[parameter_name_number]
        new_value: str = input(f'Enter new value of "{parameter}"\n--> ')

        update_list: List[Dict[str, Any]] = [json.loads(entry.strip(',\n')) for entry in self.__book_data]
        for entry in update_list:
            if entry['id'] == entry_id:
                entry['data'][parameter] = new_value
                break
        dao.write_all_data(update_list)
        print('\nEntry updated successfully!\n')

    @staticmethod
    def add_entry() -> None:
        """
            Добавляет новую запись в книгу.
            :return: None
        """
        entry_data: List[str] = []
        for parameter in PARAMETERS:
            parameter_value: str = input(f'\nEnter {parameter} --> ')
            while parameter_value is None:
                parameter_value = input(f'\nEnter {parameter} --> ')
            entry_data.append(parameter_value)
        entry: Entry = Entry(*entry_data)
        entry.write_to_file()

    @staticmethod
    def get_number(name: str, max_number: int, options: str = '') -> int:
        """
            Запрашивает у пользователя целое число в определенном диапазоне.
            :param name: Название числа для отображения в запросе
            :param max_number: максимальное допустимое значение числа
            :param options: опциональное сообщение для отображения перед запросом числа
            :return: введенное пользователем целое число
        """
        print(f'{options}\n')
        number: str = input(f'Enter {name} --> ')
        while not number.isdigit() or int(number) > max_number or int(number) <= 0:
            print(f'The {name} must be a number!\n'
                  f'Must be greater than zero!\n'
                  f'Nust be less than or equal {max_number}!\n{options}')
            number = input(f'Enter {name} --> ')
        return int(number)

    @staticmethod
    def __show_entry(entry: Any) -> None:
        """
            Выводит информацию о записи в консоль.
            :param entry: Информация о записи
            :return: None
        """
        entry_dict: dict = Entry.get_entry_by_data(json.dumps(entry))
        Entry.show_console_version(entry_dict)

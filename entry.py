import json
from typing import Dict, Union, Any

import dao


class Entry:
    def __init__(self, first_name: str, last_name: str, middle_name: str, organization: str, org_phone: str,
                 personal_phone: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.organization = organization
        self.org_phone = org_phone
        self.personal_phone = personal_phone

    def __repr__(self) -> str:
        """
            Возвращает строковое представление экземпляра класса Entry.
            :return: Строковое представление экземпляра класса Entry
        """
        return f'{__class__.__name__}(' \
               f'{self.first_name}, ' \
               f'{self.last_name}, ' \
               f'{self.middle_name}, ' \
               f'{self.organization}, ' \
               f'{self.org_phone}, ' \
               f'{self.personal_phone})'

    def write_to_file(self) -> None:
        """
            Записывает данные об экземпляре класса в файл и выводит сообщение об успешном добавлении.
            :return: None
        """
        entry_data = self.__serialize()
        dao.write_new_entry(entry_data)
        print('\nEntry added successfully!\n')

    def __serialize(self) -> str:
        """
            Сериализует данные экземпляра класса в формат JSON.
            :return: Строка с сериализованными данными
        """
        return json.dumps({
            'first_name': self.first_name,
            'last_name': self.last_name,
            'middle_name': self.middle_name,
            'organization': self.organization,
            'org_phone': self.org_phone,
            'personal_phone': self.personal_phone,
        })

    @classmethod
    def get_entry_by_data(cls, data: str) -> Dict[str, Union[str, 'Entry']]:
        """
            Создает экземпляр класса Entry из данных в формате JSON.
            :param data: Строка с данными в формате JSON
            :return: словарь с id и экземпляром класса Entry
        """
        entry_id = json.loads(data)['id']
        entry_data = json.loads(data)['data'].values()
        entry = Entry(*entry_data)
        return {'id': entry_id, 'entry': entry}

    @classmethod
    def show_console_version(cls, entry_dict: Dict[str, Any]) -> None:
        """
           Выводит информацию о записи в консоль в удобном формате.
           :param entry_dict: Словарь с информацией о записи
           :return: None
        """
        entry_id = entry_dict['id']
        entry = entry_dict['entry']
        print(f'\n-------------entry-№{entry_id}-------------\n'
              f'id: {entry_id}\n'
              f'first name: {entry.first_name}\n'
              f'last name: {entry.last_name}\n'
              f'middle name: {entry.middle_name}\n'
              f'organization: {entry.organization}\n'
              f'phone: {entry.org_phone}\n'
              f'personal phone: {entry.personal_phone}\n'
              f'')

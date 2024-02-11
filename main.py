from typing import Callable

from constants import START_SESSION_MESSAGE
from session import Session

current_session = Session()

ACTIONS: dict[int, Callable] = {1: current_session.show_page,
                                2: current_session.add_entry,
                                3: current_session.update_entry,
                                4: current_session.search_entry,
                                5: exit}


def start_session() -> None:
    """
        Начинает сеанс взаимодействия пользователя с приложением.
        :return: None
    """
    while True:
        action = current_session.get_number('action', 5, options=START_SESSION_MESSAGE)
        ACTIONS.get(action)()


if __name__ == '__main__':
    start_session()

from typing import List, Dict

PARAMETERS: List[str] = ['first_name', 'last_name', 'middle_name', 'organization', 'org_phone', 'personal_phone']

PARAMETERS_NAMES: Dict[int, str] = {1: 'first_name',
                                    2: 'last_name',
                                    3: 'middle_name',
                                    4: 'organization',
                                    5: 'org_phone',
                                    6: 'personal_phone'}

PARAMETER_MESSAGE: str = '\n---Select the parameter you want to change:---\n' \
                         '1. First name: press 1\n' \
                         '2. Last name: press 2\n' \
                         '3. Middle name: press 3\n' \
                         '4. Organization: press 4\n' \
                         '5. Phone: press 5\n' \
                         '6. Personal phone: press 6\n'

START_SESSION_MESSAGE: str = '\n-----Choose an action:-----\n' \
                             '1. Show entries: press 1\n' \
                             '2. Add new entry: press 2\n' \
                             '3. Update entry: press 3\n' \
                             '4. Search entry: press 4\n' \
                             '5. Exit: press 5\n' \

SEARCH_MESSAGE: str = '\n---Select a search option:---\n' \
                      '1. by id: press 1\n' \
                      '2. by first name: press 2\n' \
                      '3. by last name: press 3\n' \
                      '4. by middle name: press 4\n' \
                      '5. by organization: press 5\n' \
                      '6. by organization phone: press 6\n' \
                      '7. by personal phone: press 7\n' \
                      '8. search all fields: press 8\n'

SEARCH_OPTIONS: Dict[int, str] = {1: 'id',
                                  2: 'first_name',
                                  3: 'last_name',
                                  4: 'middle_name',
                                  5: 'organization',
                                  6: 'org_phone',
                                  7: 'personal_phone',
                                  8: 'all'}

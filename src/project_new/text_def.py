def login_check() -> tuple[str, str]:
    login = input(f'Введите логин администратора: ')
    password = input(f'Введите пароль администратора: ')

    return login, password

def choice_method() -> int:
    return int(input(f'Выберете метод:\n1. POST\n2. GET\n3. PUT\n4. PATCH\n5. DELETE\nВыбор: '))

def post_f() -> tuple[bool, str, str, bool | None]:
    fail = False
    title = input(f'Title: ')
    description = input(f'Description: ')
    completed = input(f'Completed (True\False): ')

    if completed.title() == 'True':
        completed = True
    elif completed.title() == 'False':
        completed = False
    else:
        fail = True
        completed = None

    return fail, title, description, completed

def put_f() -> tuple[int, str, str, bool | None, bool]:
    fail = False

    task_id = int(input('ID: '))
    title = input('Title: ')
    description = input('Description: ')
    completed = input('Completed (True\False): ')

    if completed.lower() == 'true':
        completed = True
    elif completed.lower() == 'false':
        completed = False
    else:
        fail = True
        completed = None

    return task_id, title, description, completed, fail

def patch_f() -> tuple[int, str | None, str | None, bool | None, bool]:
    fail = False

    task_id = int(input('ID: '))

    title = input('Title (Enter to skip): ')
    description = input('Description (Enter to skip): ')
    completed = input('Completed (True\\False, Enter to skip): ')

    title = title if title else None
    description = description if description else None

    if completed.lower() == 'true':
        completed = True
    elif completed.lower() == 'false':
        completed = False
    elif completed == '':
        completed = None
    else:
        fail = True
        completed = None

    return task_id, title, description, completed, fail

def delete_f() -> int:
    return int(input('ID: '))
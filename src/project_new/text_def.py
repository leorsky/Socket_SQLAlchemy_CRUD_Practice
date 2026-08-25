def login_check() -> tuple[str, str]:
    login = input(f'Введите логин администратора: ')
    password = input(f'Введите пароль администратора: ')

    return login, password

def choice_method() -> int:
    return int(input(f'Выберете метод:\n1. POST\n2. GET\n3. PUT\n4. PATCH\n5. DELETE\nВыбор: '))
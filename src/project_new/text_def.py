def login_check() -> tuple[str, str]:
    login = input(f'Введите логин администратора: ')
    password = input(f'Введите пароль администратора: ')

    return login, password
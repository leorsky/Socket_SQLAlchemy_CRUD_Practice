import json
import socket

from project_new.src.project_new.Сhecker import checker


HOST = 'localhost'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f'The server has started: {HOST}:{PORT}')


def main():
    while True:
        client_socket, addr = server_socket.accept()

        print(f'Client connected: {addr}')

        while True:
            request = client_socket.recv(1024).decode()

            if not request:
                break

            request_json = json.loads(request)

            try:
                if not checker.verify_login(request_json['login']):
                    raise ValueError('Логин неверный.')

                if not checker.verify_password(request_json['password']):
                    raise ValueError('Пароль неверный.')

                response = {
                    'fail': False,
                    'description': 'Авторизация успешна'
                }

                response_json = json.dumps(response)

                client_socket.sendall(response_json.encode())

            except ValueError as e:
                print(f'Ошибка: {e}')

                response = {
                    'fail': True,
                    'description': str(e)
                }

                response_json = json.dumps(response)

                client_socket.sendall(response_json.encode())
                continue

            except Exception as e:
                print(f'Ошибка: {e}')

                response = {
                    'fail': True,
                    'description': '500'
                }

                response_json = json.dumps(response)

                client_socket.sendall(response_json.encode())
                continue

if __name__ == '__main__':
    main()
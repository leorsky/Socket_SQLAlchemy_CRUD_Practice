import socket
import json
from project_new.src.project_new import text_def
from project_new.src.project_new.Сhecker import checker

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 8000
client_socket.connect((HOST, PORT))

while True:
    try:
        login, password = text_def.login_check()

        request = {'login': login, 'password': password}
        request_json = json.dumps(request)

        client_socket.sendall(request_json.encode())

        response = client_socket.recv(1024).decode()

        if not response:
            break

        response_json = json.loads(response)

        if response_json['fail']:
            raise Exception(response_json['description'])

        else:
            choice = text_def.choice_method()
            method, fail = checker.check_method(choice)

            if fail:
                raise Exception(method)
            else:
                pass

    except ConnectionResetError:
        print('Connection reset error')
        break

    except Exception as e:
        print(f'Error: {e}')
        continue

client_socket.close()
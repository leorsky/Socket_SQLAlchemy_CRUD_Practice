import socket



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



if __name__ == '__main__':
    main()
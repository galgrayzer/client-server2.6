from socket import *
from datetime import datetime
from random import randrange
from os import system as s


def main():
    s('cls')
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind(("0.0.0.0", 11111))
        server.listen()
        client_socket, client_adress = server.accept()
        print(f'new connection from {client_adress}')
        while True:
            data = client_socket.recv(1024).decode()
            if data == 'TIME':
                client_socket.send(datetime.now().strftime(
                    '%H : %M : %S, The year is - %Y').encode())
            elif data == 'WHORU':
                client_socket.send(gethostname().encode())
            elif data == 'RAND':
                client_socket.send(str(randrange(1, 11)).encode())
            elif data == 'EXIT':
                client_socket.send('socket-closed'.encode())
                client_socket.close()
                break
            else:
                client_socket.send('INVAILD COMMAND'.encode())


if __name__ == '__main__':
    main()

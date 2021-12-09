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
                send_message(client_socket, datetime.now().strftime(
                    '%H : %M : %S -> the year is: %Y'))
            elif data == 'NAME':
                send_message(client_socket, gethostbyname())
            elif data == 'RAND':
                send_message(client_socket, str(randrange(1, 11)))
            elif data == 'EXIT':
                send_message(client_socket, 'socket-closed')
                client_socket.close()
                break
            else:
                send_message(client_socket, 'INVAILD COMMAND')


def send_message(client_socket, messege):
    client_socket.send(str(len(messege)).encode())
    client_socket.send(messege.encode())


if __name__ == '__main__':
    main()

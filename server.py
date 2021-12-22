from socket import *
from datetime import datetime
from random import randrange
from os import system as s


MAX_BYTES = 5


def send_message(socket, messege):
    length = len(messege)
    socket.send(
        f"{'O' * (MAX_BYTES - len(str(length)))}{length}".encode())
    socket.send(messege.encode())


def recive_message(my_socket):
    try:
        data_length = int(my_socket.recv(
            MAX_BYTES).decode().replace('O', ''))
        return my_socket.recv(data_length).decode()
    except:
        return 'ERROR'


def main():
    s('cls')
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind(("0.0.0.0", 11111))
        print('server is up and running')
        server.listen()
        client_socket, client_adress = server.accept()
        print(f'new connection from {client_adress}')
        while True:
            data = recive_message(client_socket)
            print(data)
            if data == 'TIME':
                send_message(client_socket, datetime.now().strftime(
                    '%H : %M : %S -> the year is: %Y'))
            elif data == 'WHORU':
                send_message(client_socket, gethostname())
            elif data == 'RAND':
                send_message(client_socket, str(randrange(1, 11)))
            elif data == 'EXIT':
                send_message(client_socket, 'socket-closed')
                client_socket.close()
                break
            else:
                send_message(client_socket, 'INVAILD COMMAND')


if __name__ == '__main__':
    main()

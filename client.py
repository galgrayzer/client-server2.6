from socket import *
from os import system as s


MAX_BYTES = 1024
LENGTH_FOR_MESSAGE = len(str(MAX_BYTES))


def send_message(socket, messege):
    length = len(messege)
    socket.send(
        f"{'O' * (LENGTH_FOR_MESSAGE - len(str(length)))}{length}".encode())
    socket.send(messege.encode())


def recive_message(my_socket):
    data_length = int(my_socket.recv(
        LENGTH_FOR_MESSAGE).decode().replace('O', ''))
    return my_socket.recv(data_length).decode()


def main():
    s('cls')
    my_socket = socket(AF_INET, SOCK_STREAM)
    my_socket.connect(("localhost", 11111))
    while True:
        send_message(my_socket, input('Enter: '))
        data_from_server = recive_message(my_socket)
        print(data_from_server)
        if data_from_server == 'socket-closed':
            my_socket.close()
            break


if __name__ == '__main__':
    main()

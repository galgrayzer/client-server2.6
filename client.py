from socket import *
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
            MAX_BYTES).decode().replace('0', ''))
        return my_socket.recv(data_length).decode()
    except:
        return 'ERROR'


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

from socket import *
from os import system as s


def main():
    s('cls')
    my_socket = socket(AF_INET, SOCK_STREAM)
    my_socket.connect(("localhost", 11111))
    while True:
        my_socket.send(input('Enter: ').encode())
        data_from_server = my_socket.recv(1024).decode()
        print(data_from_server)
        if data_from_server == 'socket-closed':
            my_socket.close()
            break


if __name__ == '__main__':
    main()

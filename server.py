from socket import *
from datetime import datetime
from random import randrange


def main():
    with socket(AF_INET, SOCK_STREAM) as server:
        server.bind("0.0.0.0", 11111)
        server.listen()
        client_socket, client_adress = server.accept()
        print(f'new connection from {client_adress}')
        while True:
            data = server.recv(1024)
            if data == 'TIME':
                server.send(datetime.now().strftime(
                    '%H : %M : %S, The year is - %Y').encode())
            elif data == 'NAME':
                server.send(gethostname().encode())
            elif data == 'RAND':
                server.send(str(randrange(1, 11)).encode())
            elif data == 'EXIT':
                server.send('socket-closed'.encode())
                client_socket.close()
                break


if __name__ == '__main__':
    main()

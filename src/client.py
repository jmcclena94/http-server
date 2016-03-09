# coding=utf-8
import socket
import sys


def client(message):
    client_socket = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in client_socket if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf-8'))

    buffer_length = 4096
    reply_complete = False
    while not reply_complete:
        part = client.recv(buffer_length)
        print(part.decode('utf-8'))
        if len(part) < buffer_length:
            reply_complete = True
    client.close()


if __name__ == "__main__":
    message = sys.argv[1]
    client(message)

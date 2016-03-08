# coding=utf-8
import socket
import sys


def client(message):
    client_socket = socket.getaddrinfo('127.0.0.1', 6000)
    stream_info = [i for i in client_socket if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])


if __name__ == "__main__":
    sys.argv[1] = message
    client(message)

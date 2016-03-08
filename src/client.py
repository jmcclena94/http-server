# coding=utf-8
import socket
import sys
import server


def client(message):
    server()
    client_socket = socket.getaddrinfo('127.0.0.1', 6000)
    stream_info = [i for i in client_socket if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    client.sendall(message.encode('utf-8'))


if __name__ == "__main__":
    message = sys.argv[1]
    client(message)

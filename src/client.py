# coding=utf-8
import socket
import sys


def client(message):
    client_socket = socket.getaddrinfo('127.0.0.1', 5000)
    stream_info = [i for i in client_socket if i[1] == socket.SOCK_STREAM][0]
    client = socket.socket(*stream_info[:3])
    client.connect(stream_info[-1])
    if message.encode('utf-8'):
        client.sendall(message.encode('utf-8'))
        client.shutdown(socket.SHUT_WR)
    else:
        print('Bad message')
        return ''

    buffer_length = 8
    reply_complete = False
    return_message = ''
    while not reply_complete:
        part = client.recv(buffer_length)
        if len(part) < buffer_length:
            reply_complete = True
        return_message += part.decode('utf-8')
    print(return_message)
    # client.shutdown(socket.SHUT_RD)
    client.close()
    return return_message


if __name__ == "__main__":
    message = sys.argv[1]
    client(message)

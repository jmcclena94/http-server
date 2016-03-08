# coding=utf-8
import socket


def server():
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 6000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()

    buffer_length = 4096
    message_complete = False
    return_message = ''
    while not message_complete:
        part = conn.recv(buffer_length)
        return_message = return_message + part
        print(part.decode('utf-8'))
        if len(part) < buffer_length:
            message_complete = True

    conn.sendall(return_message.encode('utf-8'))

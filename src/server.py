# coding=utf-8
import socket
# import pdb


def server():
    # pdb.set_trace()
    server = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM,
                           socket.IPPROTO_TCP)
    address = ('127.0.0.1', 5000)
    server.bind(address)
    server.listen(1)
    conn, addr = server.accept()

    buffer_length = 4096
    message_complete = False
    return_message = ''
    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf-8'))
        if len(part) < buffer_length:
            message_complete = True
            server.close()
        return_message += part.decode('utf-8')
    print(return_message)
    conn.sendall(return_message.encode('utf-8'))
    conn.close()

server()

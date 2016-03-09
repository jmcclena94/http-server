# coding=utf-8
import socket


def server():
    """Run Server."""
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_TCP)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('127.0.0.1', 5000)
    server_socket.bind(address)
    server_socket.listen(1)
    conn, addr = server_socket.accept()

    buffer_length = 8
    message_complete = False
    return_message = ''
    while not message_complete:
        part = conn.recv(buffer_length)
        if len(part) < buffer_length:
            message_complete = True
            server_socket.close()
        return_message += part.decode('utf-8')
    print(return_message)
    conn.sendall(return_message.encode('utf-8'))
    conn.close()
    server_socket.close()
    server()


if __name__ == "__main__":
    try:
        server()
    except KeyboardInterrupt:
        print('\nClosed')

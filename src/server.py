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
    ok_200 = response_ok()
    # conn.sendall(return_message.encode('utf-8'))
    conn.sendall(ok_200.encode('utf-8'))
    conn.close()
    server_socket.close()
    server()


def response_ok():
    """Return a 200 OK response."""
    ok_200 = 'HTTP/1.1 200 OK\r\n\r\n'
    return ok_200


def response_error():
    """Return a 500 Error response."""
    no_500 = 'HTTP/1.1 500 Internal Server Error.'
    return no_500


if __name__ == "__main__":
    try:
        server()
    except KeyboardInterrupt:
        print('\nClosed')

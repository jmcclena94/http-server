# coding=utf-8
import socket
import io
import os


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
    try:
        parse_request(return_message)
        reply = response_ok()
    except NotImplementedError:
        reply = response_error()
    # ok_200 = response_ok()
    # conn.sendall(return_message.encode('utf-8'))
    conn.sendall(reply.encode('utf-8'))
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


def parse_request(request):
    """Parse request and return reponse or error."""
    parsed = request.split()
    print(parsed)
    if len(parsed) != 5:
        raise NotImplementedError
    elif parsed[0] != 'GET':
        raise NotImplementedError
    elif parsed[2] != 'HTTP/1.1':
        raise NotImplementedError
    elif parsed[3] != 'Host:':
        raise NotImplementedError
    else:
        return parsed[1]


def resolve_uri(uri):
    root_dir = '../webroot/'
    filename, file_extension = os.path.splitext(uri)
    if file_extension is not '':
        path = root_dir + filename + file_extension
        try:
            open_file = io.open(path, 'rb')
            body = open_file.read()
            content_type = b'text/plain'
            return (body, content_type)
        except FileNotFoundError:
            raise FileNotFoundError
            body = b'404 File Not Found'
            return (body, b'text/html')


if __name__ == "__main__":
    try:
        server()
    except KeyboardInterrupt:
        print('\nClosed')

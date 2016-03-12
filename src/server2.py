# coding=utf-8
from server import response_ok, response_error, parse_request, resolve_uri


def echo(socket, address):
    """Run Server."""

    buffer_length = 8
    message_complete = False
    return_message = ''
    while not message_complete:
        part = socket.recv(buffer_length)
        if len(part) < buffer_length:
            message_complete = True
        return_message += part.decode('utf-8')
    print('Return Message: ' + return_message)
    try:
        uri = parse_request(return_message)
        content = resolve_uri(uri)
        reply_ok = response_ok()
        content_type = b'Content Type: ' + content[1] + b'\r\n'
        content_length = str(len(content[0])).encode('utf-8')
        content_length = b'Content-Length: ' + content_length + b'\r\n\r\n'
        reply = reply_ok + content_type + content_length + content[0]
        print(reply)
    except NotImplementedError:
        reply = response_error()
    except OSError:
        reply = response_error()
    socket.sendall(reply)
    socket.close()


if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10000), echo)
    print('Starting echo server on port 10000')
    server.serve_forever()

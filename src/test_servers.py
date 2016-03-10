# coding=utf-8
import pytest


GOOD = [
    ('GET somepath HTTP/1.1 Host: www.somuchfun.com', 'somepath'),
]

OK_RESPONSE = [
    ('fart', 'HTTP/1.1 200 OK\r\n\r\n'),
    ('Hello World', 'HTTP/1.1 200 OK\r\n\r\n'),
    ('11111111', 'HTTP/1.1 200 OK\r\n\r\n'),
]


def test_parse_request_success():
    """Test if parse request sends the right errors."""
    from server import parse_request
    assert parse_request('GET somepath HTTP/1.1 Host: www.somuchfun.com') == 'somepath'


def test_parse_request():
    """Test if parse request sends the right errors."""
    from server import parse_request
    with pytest.raises(NotImplementedError):
        parse_request('GET somechickens HTTP/1.0 Host: www.thisiswrong.com')


def test_response_ok():
    """Test if the response is ok."""
    from server import response_ok
    assert response_ok() == 'HTTP/1.1 200 OK\r\n\r\n'

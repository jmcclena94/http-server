# coding=utf-8
import pytest

# MESSAGE_TABLE = [
#     ('Hello World', 'Hello World'),
#     ('', ''),
#     ('This message is longer than multiple buffer lengths', 'This message is l'
#      'onger than multiple buffer lengths'),
#     ('11111111', '11111111'),
#     ('111111', '111111'),
#     ('£', '£')
# ]

RESPONSES = [
    ('GET', '200 OK'),
    ('HTTP/1.1', '500'),
    ('NOT THERE', '404 Not Found'),
]


# OK_RESPONSE = [
#     ('fart', 'HTTP/1.1 200 OK\r\n\r\n'),
#     ('Hello World', 'HTTP/1.1 200 OK\r\n\r\n'),
#     ('11111111', 'HTTP/1.1 200 OK\r\n\r\n'),
# ]

@pytest.mark.parametrize('request, response', RESPONSES)
def test_parse_request(request, response):
    """Test if parse request sends the right errors."""
    from server import parse_request
    assert parse_request(request) == response


# def test_parse_request():
#     """Test if parse request sends the right errors."""
#     from server import parse_request
#     with pytest.raises(NotImplementedError) as request
    
#     assert parse_request(request) == response



def test_response_ok():
    from server import response_ok
    assert response_ok() == 'HTTP/1.1 200 OK\r\n\r\n'

# @pytest.mark.parametrize('message, reply', MESSAGE_TABLE)
# def test_client(message, reply):
#     from client import client
#     assert client(message) == reply


# @pytest.mark.parametrize('request, response', OK_RESPONSE)
# def test_response_ok(request, response):
#     from client import client
#     assert client(request) == response

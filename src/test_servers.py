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


# OK_RESPONSE = [
#     ('fart', 'HTTP/1.1 200 OK\r\n\r\n'),
#     ('Hello World', 'HTTP/1.1 200 OK\r\n\r\n'),
#     ('11111111', 'HTTP/1.1 200 OK\r\n\r\n'),
# ]


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

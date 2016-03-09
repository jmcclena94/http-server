# coding=utf-8
import pytest

MESSAGE_TABLE = [
    ('Hello World', 'Hello World'),
    ('', ''),
    ('This message is longer than multiple buffer lengths', 'This message is l'
     'onger than multiple buffer lengths'),
    ('11111111', '11111111'),
    ('111111', '111111'),
    ('£', '£')
]


@pytest.mark.parametrize('message, reply', MESSAGE_TABLE)
def test_client(message, reply):
    from client import client
    assert client(message) == reply

# coding=utf-8
import pytest

MESSAGE_TABLE = [
    ('Hello World', 'Hello World'),
    ('', '')
]


@pytest.mark.parametrize('message, reply', MESSAGE_TABLE)
def test_client(message, reply):
    from client import client
    assert client(message) == reply

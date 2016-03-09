# coding=utf-8
import pytest

MESSAGE_TABLE = [
    ('Hello World', 'Hello World')
]

@pytest.mark.parametrize('message, reply')

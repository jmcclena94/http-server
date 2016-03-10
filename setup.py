# coding=utf-8
from setuptools import setup

setup(
    name='http-server',
    description='http-server',
    version=0.1,
    author='Joe McClenahan and Jared Scarr',
    author_email='jmcclena94@gmail.com jaredscarr@gmail.com',
    license='MIT',
    py_modules=['client'],
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)

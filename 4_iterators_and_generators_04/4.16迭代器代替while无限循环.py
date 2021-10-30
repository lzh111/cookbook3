# -*- coding: utf-8 -*-

CHUNKSIZE = 8192


def process_data(data):
    pass


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process_data(data)


import sys

with open('4.8.txt', 'r') as f:
    # lambda创建了一个无参的callable对象
    for chunk in iter(lambda: f.read(10), ''):
        n = sys.stdout.write(chunk)

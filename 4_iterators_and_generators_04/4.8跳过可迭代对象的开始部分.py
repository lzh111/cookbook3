#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/10/19 上午10:57
#   @Author : liuzh
#   @desc :
from itertools import dropwhile

# 跳过开始地方的注释行
with open('4.8.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# 如果已知跳过的行号[3:]
from itertools import islice

items = ['a', 'b', 'c', 1, 4, 10, 15]
# 相当于：[3:]
for x in islice(items, 3, None):
    print(x)

# 如果互换None和3的位置：[:3]
for x in islice(items, None, 3):
    print(x)

# 原来写法
with open('4.8.txt') as f:
    # Skip over initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)

# 更新后：这样跳过的是文中所有的注释行
with open('4.8.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

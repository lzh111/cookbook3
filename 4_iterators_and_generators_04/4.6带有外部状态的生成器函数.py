#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   @Time : 2021/10/19 上午9:09
#   @Author : liuzh
#   @desc :

"""
问题：你想定义一个生成器函数，但是它会调用某个你想暴露给用户使用的外部状态值。
"""

from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        # 堆的深度
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        # 将行号和内容填充到堆中
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        # 清空
        self.history.clear()


with open('test_file.txt') as f:
    lines = linehistory(f)
    for line in lines:
        for lineno, hline in lines.history:
            print('{}:{}'.format(lineno, hline), end='')

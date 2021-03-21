#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/20 14:50 
# @Author : 刘子豪 
# @desc :在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

"""
问题：在迭代操作或者其他操作的时候，怎样只保留最后有限几个元素的历史记录？

解决：collections.deque
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    # with open(r'somefile.txt') as f:
    #     # 保留最后八个元素
    #     for line, prevlines in search(f, 'python', 7):
    #         for pline in prevlines:
    #             print(pline, end='')
    #         print(line, end='')
    #         print('-' * 20)

    # 使用deque(maxlen=N)会构造一个固定大小的队列，队列满时，新加入的对象会把老的对象顶出去
    # 在队列两端插入删除元素时间复杂度为O(1),列表在开头插入或删除时间复杂度为O(n)
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    # 左侧插入
    q.appendleft(11)
    print(q)
    # 左侧弹出
    q.popleft()
    print(q)
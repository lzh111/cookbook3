#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 8:56 
# @Author : 刘子豪 
# @desc :
from collections import Iterable

"""
问题：遍历一个可迭代对象中的所有元素，但是却不想使用for循环

解决：为了手动的遍历可迭代对象，使用 next() 函数并在代码中捕获 StopIteration 异常
"""


# 手动读取一个文件
def manual_iter():
    with open('test_file.txt') as f:
        try:
            while True:
                line = next(f)
                print(line, end='')
        except StopAsyncIteration:
            pass


# 返回指定值，标记结尾
def manual_iter01():
    with open('test_file.txt') as f:
        # 方法1
        # while True:
        #     line = next(f, None)
        #     if line is None:
        #         break
        #     print(line, end='')
        # 方法2
        for i in iter(lambda: next(f), b''):
            print(i)


def test_iter():
    """迭代器细节"""
    items = [1, 2, 3]
    # 判断是不是可迭代的, 可迭代的可以直接用作for循环对象
    if isinstance(items, Iterable):
        print("列表是可迭代的")
    # 创建迭代器对象
    x = iter(items)
    print('-' * 10)
    print(next(x))  # next()返回迭代器的下一个项目，通常要和iter()配套使用
    print(next(x))
    print(next(x))
    print(next(x))  # 容器中没有元素 再执行next()会报StopIteration错误


test_iter()
manual_iter01()
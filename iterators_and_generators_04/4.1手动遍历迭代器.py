#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 8:56 
# @Author : 刘子豪 
# @desc :

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
        while True:
            line = next(f, None)
            if line is None:
                break
            print(line, end='')


def test_iter():
    """迭代器细节"""
    items = [1, 2, 3]
    # 生成迭代器
    x = iter(items)
    print()
    print('-' * 10)
    print(next(x))  # next()返回迭代器的下一个项目，通常要和iter()配套使用
    print(next(x))
    print(next(x))
    print(next(x))  # 容器中没有元素 再执行next()会报StopIteration错误


manual_iter01()
test_iter()

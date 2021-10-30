#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/21 19:17 
# @Author : 刘子豪 
# @desc :

"""问题1：列表翻转"""
l = [1, 2, 3, 4]
# 方法一
print(list(reversed(l)))

# 方法二
print(l[::-1])

"""
小结：
1. 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。 如果两者都不符合，那你必须先将对象转换为一个列表才行
2. 要注意的是如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存。
3. 定义一个反向迭代器可以使得代码非常的高效， 因为它不再需要将数据填充到一个列表中然后再去反向迭代这个列表。
"""


# 例：在自定义类上实现 __reversed__() 方法来实现反向迭代
class CutDown:
    def __init__(self, data):
        self.data = data

    def __reversed__(self):
        data = self.data
        while data > 0:
            data -= 1
            yield data

    def __iter__(self):
        data = 0
        while data < self.data:
            yield data
            data += 1


c = CutDown(10)
for i in c:
    print(i)

print('-' * 20)
for i in reversed(c):
    print(i)

import itertools

x = [1, 2, 3]

combin_1 = itertools.permutations(x, 1)  # 取1个数进行组合，生成的时一个迭代器
combin_2 = itertools.permutations(x, 2)  # 取2个数进行组合，生成的是一个迭代器

print('combin_1:', list(combin_1))  # 将迭代器转为列表并打印

print('\ncombin_1、combin_2的数据类型：', type(combin_1))

print('\n输出迭代器每次迭代内容:')
for i in combin_2:
    print(i)

"""
结果：
combin_1: [(1,), (2,), (3,)]

combin_1、combin_2的数据类型： <class 'itertools.permutations'>

输出迭代器每次迭代内容:
(1, 2)
(1, 3)
(2, 1)
(2, 3)
(3, 1)
(3, 2)
"""

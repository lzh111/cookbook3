# -*- coding: utf-8 -*-

# 同时迭代多个序列，其中迭代长度跟参数中最短序列长度一致
xpts = [1, 5, 4, 2, 10, 7, 8]
ypts = [101, 78, 37, 15, 62, 99, 9, 9]
for x, y in zip(xpts, ypts):
    print(x, y)

# 迭代长度和最长序列长度一致， 如果短的那个序列没有，会展示None
from itertools import zip_longest

for x, y in zip_longest(xpts, ypts):
    print(x, y)

# 将两个序列打包成一个字典, 键值对数量和最短的序列一致
headers = ['name', 'shares', 'price', "haha"]
values = ['ACME', 100, 490.1]

s = dict(zip(headers, values))
print(s)

# 解压多个序列：元组中元素个数跟输入序列个数一样
a = [1, 2, 3]
b = [10, 11, 12]
c = ['x', 'y', 'z']
for i in zip(a, b, c):
    print(i)

# zip() 会创建一个迭代器来作为结果返回。 如果你需要将结对的值存储在列表中，要使用 list() 函数
l = zip(a, b ,c)
print(l)
l = list(l)
print(l)
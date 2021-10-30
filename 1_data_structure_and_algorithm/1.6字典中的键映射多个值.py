#!/usr/bin/env python3.7
# _*_ coding: utf-8 _*_
# @Time : 2021/3/20 22:40 
# @Author : 刘子豪 
# @desc :

from collections import defaultdict

"""
问题：怎样实现一个键对应多个值的字典（也叫 multidict）

解决:一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，
那么你就需要将这多个值放到另外的容器中， 比如列表或者集合里面

选择列表：保持元素的插入顺序
选择集合：去重

注意：defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体。
如果你并不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替。
"""




d_list = defaultdict(list)
d_list['a'].append(2)
d_list['a'].append(4)
d_list['a'].append(3)
d_list['a'].append(1)

print(dict(d_list))

d_set = defaultdict(set)
d_set['a'].add(1)
d_set['a'].add(1)
d_set['a'].add(2)
d_set['a'].add(2)
d_set['a'].add(3)
d_set['a'].add(3)
print(dict(d_set))

pairs = {
    'a': 1,
    'b': 2,
    'c': 3
}
# 自己实现
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
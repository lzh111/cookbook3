# -*- coding: utf-8 -*-
import os
import fnmatch
import gzip
import bz2
import re

# 假如文件目录如下
"""
foo/
    access-log-012007.gz
    access-log-022007.gz
    access-log-032007.gz
    ...
    access-log-012008
bar/
    access-log-092007.bz2
    ...
    access-log-022008
"""


def gen_find(filepat, top):
    """ 在目录树中查找与shell通配符模式匹配的所有文件名
    """
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """ 一次打开一系列文件名，生成一个文件对象。在进行下一次迭代时，文件将立即关闭。
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, 'rt')
        yield f
        f.close()


def gen_concatenate(iterators):
    """ 将迭代器序列链接到一个序列中。
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """ 在一系列行中查找正则表达式模式
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line



# lognames = gen_find('access-log*', 'www')
# files = gen_opener(lognames)
# lines = gen_concatenate(files)
# pylines = gen_grep('(?i)python', lines)
# for line in pylines:
#     print(line)

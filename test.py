# -*-coding:utf-8-*-

"""
Author: Anger36
Date: 19-5-4
"""

import copy

a = [3, 2, 5, ['2', 'a'], 6]
b = a
print(id(a), id(b))
print(id(a[3]), id(b[3]))
b = copy.copy(a)
print(id(a), id(b))
print(id(a[3]), id(b[3]))
print(u"浅拷贝, 原始对象{0}".format(a))
print(u"浅拷贝, 拷贝对象{0}".format(b))

a.append('12')
print(u"浅拷贝, 原始对象{0}".format(a))
print(u"浅拷贝, 拷贝对象{0}".format(b))


a[3].append("c")
print(u"浅拷贝, 原始对象{0}".format(a))
print(u"浅拷贝, 拷贝对象{0}".format(b))


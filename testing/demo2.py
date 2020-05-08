# -*- coding:utf-8 -*-
# @Time : 2020/5/8 4:39 下午
# @Author : winnie


# __all__定义一个列表，提供对外公开的变量，方法，类，模块(可以在__init__.py里使用__all__)；
# 常与from testing.demo2 import * 搭配使用
# 如果不使用，这个模块则完全开放
__all__ = ['hello']

# 定义一个变量
hello = 'hello demo2'


# 定义一个方法
def f():
    print("demo2.py f()")


# 定义一个类
class Demo2:
    pass

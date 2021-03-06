#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
/**
 *
 *   █████▒█    ██  ▄████▄   ██ ▄█▀       ██████╗ ██╗   ██╗ ██████╗
 * ▓██   ▒ ██  ▓██▒▒██▀ ▀█   ██▄█▒        ██╔══██╗██║   ██║██╔════╝
 * ▒████ ░▓██  ▒██░▒▓█    ▄ ▓███▄░        ██████╔╝██║   ██║██║  ███╗
 * ░▓█▒  ░▓▓█  ░██░▒▓▓▄ ▄██▒▓██ █▄        ██╔══██╗██║   ██║██║   ██║
 * ░▒█░   ▒▒█████▓ ▒ ▓███▀ ░▒██▒ █▄       ██████╔╝╚██████╔╝╚██████╔╝
 *  ▒ ░   ░▒▓▒ ▒ ▒ ░ ░▒ ▒  ░▒ ▒▒ ▓▒       ╚═════╝  ╚═════╝  ╚═════╝
 *  ░     ░░▒░ ░ ░   ░  ▒   ░ ░▒ ▒░
 *  ░ ░    ░░░ ░ ░ ░        ░ ░░ ░
 *           ░     ░ ░      ░  ░
 */            
'''


# 输入
# input()

# r'' 字符串不转义
# print(r'')

# '''...'''的格式表示多行内容
# print('''xxx''')


#and 与
#or  或
#not 非
#None 空值

# / 除   // 整除  % 余数

# ord()
# chr()
# b'...' 字节

#utf-8 ascii
# encode() decode()

# len() 字符串长度

#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序 Windows系统会忽略这个注释
#!/usr/bin/env python3

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，
#否则，你在源代码中写的中文输出可能会有乱码
# -*- coding: utf-8 -*-


#格式化

# %s 字符串
# %d 整数
# %f 浮点数
# %x 十六进制整数  
# format()

# list  有序的集合 列表(数组)  可以添加和删除元素  list = ['1', '2', '3']  就是数组
# tuple 有序的列表 元组 一旦初始化就不能修改  tuple = ('Tom', 'Jack', 'Alice')
# dict  全称dictionary 字典 key-value dict = {'Tom': 10, 'Jack': 20, 'Alice': 30}
# set   和dict类似 也是一组key的集合，但不存储value key不能重复 set = set([1, 2, 3])
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
# set的原理和dict一样，所以，同样不可以放入可变对象(list)

# 和list比较，dict有以下几个特点：
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。

# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# 所以，dict是用空间来换取时间的一种方法。


# 条件判断
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# if x:
# 	print('Ture')

# 循环
# for val in list:
# 	pass
# range(5)  [0, 1, 2, 3, 4]

# while x:
# 	pass

# continue 跳过这次循环
# break    结束循环


# 函数

def function():
	pass

# isinstance() 数据类型检查

# *numbers 把这个list的所有元素作为可变参数传进去
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
'''
 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
 这5种参数都可以组合使用。但是请注意，
 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

'''
Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
'''

# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# L[:3]

# 迭代

'''
d = {'a': 1, 'b': 2, 'c': 3}

for k,v in d.items():
	print(k, v)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
print(isinstance(d, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身
for k,v in enumerate(d):
	print(k,'----',v)

'''

# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator

# list、tuple、dict、set、str、generator、包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 可以使用isinstance()判断一个对象是否是Iterable对象
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：

# 高阶函数

'''
 map()函数接收两个参数，一个是函数，一个是Iterable(可迭代)，
 map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator(迭代器)返回。
'''
# map()

'''
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
# reduce()

# lambda 匿名函数

'''
可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
注意到filter()函数返回的是一个Iterator，
也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
'''
# filter()

# 可以对list进行排序
# sorted()

# 返回函数
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

# 匿名函数
# 关键字 lambda

# 裝飾器
# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# functools模块

# 偏函數（Partial function）
# functools.partial


# 模块
# import xxx
# 作用域
# _xxx private
# xxx public

# 安装第三方模块
# pip install xxx
# https://pypi.org/

# 面向对象编程
# 面向对象编程——Object Oriented Programming，简称OOP，是一种"程序设计思想"。
# OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# __name _name _Student__name

# type()
# isinstance()
# dir() 获得一个对象的所有属性和方法

# __slots__
# MethodType()
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：

# @property

# 多重继承

# 定制类
# __init__
# __str__
# __repr__
# __iter__ 该方法返回一个迭代对象
# __getitem__ 要表现得像list那样按照下标取出元素
# __getattr__ 动态返回一个属性
# __call__
# callable() 需要判断一个对象是否能被调用

# 使用枚举类
# Enum(xxx, (xxx...))

# 使用元类
# type(1, 2, 3)
'''
1. class的名称；
2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''
# metaclass 元类
# __new__(1, 2, 3, 4)
# 
'''
1. 当前准备创建的类的对象；

2. 类的名字；

3. 类继承的父类集合；

4. 类的方法集合。
'''
# metaclass是Python中非常具有魔术性的对象，
# 它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

# 错误处理
'''
	try:
		pass
	except Exception as e:
		raise
	else:
		pass
	finally:
		pass
'''

# Python所有的错误都是从BaseException类派生的
# Python内置的logging模块可以非常容易地记录错误信息

# 调试
# print()
# 断言 assert assert n != 0, 'n is zero!'
# logging 它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
# pdb
# pdb.set_trace()
# IDE

# TDD 单元测试

# 文档测试

# 三目运算符
'''
x = 0
y = x if x>0 else 'not zero'
print(y)
'''

# IO

# 文件读写
# open()
# file-like Object
# StringIO
# BytesIO

# 操作文件和目录
# os.name
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# os.environ
# os.path.abspath('.')
# os.path.join(root, 'testdir')
# os.mkdir(testdir)
# os.rmdir(testdir)
# os.path.splitext()可以直接让你得到文件扩展名

# 序列化
# pickle.dumps(x)
# pickle.loads(x)
# json.dumps(x)
# json.loads(x)

# 进程和线程
# os.getpid()
# os.fork()
# multiprocessing
# Pool 进程池
# 子进程
# 进程间通信

# 多线程
# lock
# ThreadLocal
# 分布式进程
# 在Thread和Process中，应当优选Process，因为Process更稳定，
# 而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。

# 正则

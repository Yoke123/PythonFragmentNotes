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
from datetime import datetime
from collections import namedtuple, deque, defaultdict, OrderedDict
import base64

print('------内建模块------')

print('------datetime------')

now = datetime.now()
print(now, type(now))

dt = datetime(2017, 5, 3, 9, 45)
print(dt.timestamp())

dt2 = dt.timestamp()
print(datetime.fromtimestamp(dt2))
print(datetime.utcfromtimestamp(dt2))

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)

print(datetime.now().strftime('%a, %b %d %H:%M'))


print('-------collections-------')

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(type(p))

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key2'])

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)

print(base64.b64encode(b'aaaaa'))
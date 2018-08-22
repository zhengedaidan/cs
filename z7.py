# -*- coding:utf-8 -*-
# class A(object):
#     has_new=False
#     def __new__(cls, *args, **kwargs):
#         if not cls.has_new:
#             cls.has_new=super(A, cls).__new__(cls,*args, **kwargs)
#         return cls.has_new
# a=A()
# print(round(2.666,1))
# print(float("%.2f" % 2.6))


# logging.basicConfig(level=logging.DEBUG,
#                     format='等级:[%(levelname)s]<>'
#                            '%(threadName)s线程 >> %(filename)s文件>> %(lineno)d行>> %(message)s信息'
#                            ' >>时间:%(asctime)s', datefmt='%Y/%m/%d %H:%M:%S',
#                     filename='./log.log')
# logger = logging.getLogger(__name__)
# try:
#     1/0
# except Exception as e:
#     logger.debug(e)
#
# scrapy :
# LOG_LEVEL = "WARNING"
# LOG_FILE = "./log.log"
#
# logger = logging.getLogger(__name__)
# logger.warning()


# import logging
# logging.basicConfig(level=logging.DEBUG,
#                     format='等级:[%(levelname)s]<>'
#                            '%(threadName)s线程 >> %(filename)s文件>> %(lineno)d行>> %(message)s信息'
#                            ' >>时间:%(asctime)s',
#                     datefmt='%Y/%m/%d %H:%M:%S',
#                     filename='./log.log')
#
# logger=logging.getLogger(__name__)
# try:
#     1/0
# except Exception as e:
#     logger.debug(e)

# from init.i1 import *
# print(i1.i)
# import init

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
# f(2)
# f(3,[3,2,1])    #缺省参数若有实参,则重新初始化,再次缺省还是不重新初始化
# f(3)


# import sys
# print(sys.getdefaultencoding())


l=[1,2,3,4]
# l.append([5.6])
l.extend([5,6])
print(l)
98765478909-876
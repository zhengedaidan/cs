# -*- coding:utf-8 -*-
# class Sample:
#     def __enter__(self):
#         print(888)
#         return self
#     def __exit__(self,type,value, trace):
#         print(777)
#         # try:
#         #     print("type:",type)
#         # except Exception as value:
#         #     print("value:",value)
#         # print("trace:",trace)
#     def do_something(self):
#         print(666)
#         # bar=1/0
#         # return bar+10
# with Sample() as sample:
#     sample.do_something()import os,glob
# import os,glob
# for i in filter(os.path.isdir, glob.glob('foldercopy/*')):
#     print (i)   #文件夹（该路径）自己的路径
#     name = os.path.basename(i)
#     print (name)   #括号里路径(文件夹或文件）的名称
#     path=os.path.dirname(i)    #命令行启动该命令返回空，必须配合os.path.abspath(__file__)使用
#     print (path)   #括号里路径(文件夹或文件）所在路径
#     ab_path=os.path.abspath(i)
#     print (ab_path)      #绝对路径
#
# import sys
# print(sys.path)
class T:
    def __init__(self):
        self.name="wang"
    a=1
    def run(self):
        pass
    @classmethod
    def cls1(cls):
        pass
print(T.__dict__)
print(dir(T))
print(100*"*")
t=T()
print(t.__dict__)
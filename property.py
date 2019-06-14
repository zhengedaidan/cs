# -*- coding:utf-8 -*-
class A(object):
    # def __init__(self):
    #     self.pwd=123
    @property
    def getpwd(self):
        return self.pwd
    @getpwd.setter
    def getpwd(self,values):
        print(666)
        self.pwd=234
        return self.pwd
a=A()
a.getpwd=123
# print(A().getpwd)


# class A:
#     @property
#     def eat(self):
#         return self.name
#     @eat.setter
#     def eat(self,val):
#         self.name = val
# a =A()
# a.eat="香蕉"
# print(a.eat)
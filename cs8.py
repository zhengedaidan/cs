# -*- coding:utf-8 -*-
class A:
    def show(self):
        print("a")
class B(A):
    def show(self):
        print("b")
obj=B()
print(obj.__class__)
obj.__class__=A
obj.show()
print(obj)

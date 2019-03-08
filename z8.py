from collections import Iterable
import sys
class Stu:
    def __init__(self):
        self.item = [1,3,5]
    def __iter__(self):
        iter = Iter(self.item)
        return iter

class Iter:
    def __init__(self,*args):
        self.diedai = args[0]
        self.current_index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current_index < len(self.diedai):
            self.current_index += 1
            return self.diedai[self.current_index-1]
        else:
            print("迭代完成")
            raise StopIteration


# stu = Stu()
# print(iter(stu))
# iter函数函数 调用可迭代对象的__iter__方法 接收到迭代器

# for i in stu:
#     print(i)
# 遍历可迭代对象  本质是先取迭代器 在用迭代器取一次取值
# 需要在__next__抛出停止迭代异常遍历完成之后才会停止

# sit = Iter(stu.item)
# print(sit)
# 实例化迭代器  实例时需要接受迭代对象的可遍历属性  而不是迭代对象

# print(next(sit))
# print(next(sit))
# next函数调用迭代器对象的__next__方法 返回可迭代对象属性的第一条数据及下一条数据
# while True:
#     try:
#         print(next(sit))
#     except StopIteration as e:
#         break
# 结束时需捕获异常

# li = [1,2,3,4,5,6,7]
# my_iter = iter(li)
# print(my_iter)

class St:
    def __iter__(self):
        return Itor()
class Te:
    def __iter__(self):
        return Itor()

class Itor():
    def __iter__(self):
        return self
    def __next__(self):
        print("sadf"[0])
st = St()
te = Te()
li = [1,3,5]

it = Itor()
print(it,id(it))
print(iter(st),id(iter(st)))
print(iter(te),id(iter(te)))
print(iter(li),id(iter(li)))
# for i in it:
#     print(i)
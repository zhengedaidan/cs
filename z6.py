# -*- coding:utf-8 -*-
class People(dict):
    # __slots__ = ("name",)    #限制实例属性,子类不会继承
    def __init__(self, name):
        self.name = name
        # self.__store__={} # 可以简写为，类内不用定义__setattr__方法，在继承父类的该方法 object.__setattr__(self,"__store__",{})
        object.__setattr__(self,'__store__', {})
    def __getattr__(self, item):    #获取不在__dict__的对象时走  在__dict__里的不走
        #self.age   # 如果这样取不存在的属性会无限递归
        return "走__getattr",item
    def __setattr__(self, key, value):
        #self.name = value  # 如果还这样调用会出现无限递归的情况
        print("走__setattr")
        super(People, self).__setattr__(key,value)      #调用父类 把键值存在字典里,取值时才能取到，否则取不到会调用__get__
    def __delattr__(self, item):  #del 实例.属性   该属性没有也不报错
        print("走delattr")

    def __setitem__(self, key, value):#self[""]=""
        #self[""]="" 会无限递归
        print("走setitem")
        dd={}
        dd[key]=value   #这样没事  不是对象本身
        super(People, self).__setitem__(key, value)    #不继承父类self本身没有把键加到自己身上
    def __getitem__(self, item):       # 获取已有的键时也走
        print("走getitem")
    def __delitem__(self, key):    #del 实例[键]   该键没有也不报错
        print("走 delitem")
    def __del__(self):  #对象销毁走该方法
        pass


p=People("li")
print(p.name)
print(p.__store__)


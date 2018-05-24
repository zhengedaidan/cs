# from datetime import datetime,date,timedelta
# import time
# s="2018:08:08 08:08:08"
# t=datetime.strptime(s,"%Y:%m:%d %H:%M:%S")
# print(t)
#
# t1=t+timedelta(days=6)
# print(t1)
#
# tu=datetime.utcnow()
# print(tu)
#
# tc=time.strptime(s, "%Y:%m:%d %H:%M:%S")
# print(list(tc))
# print(type(tc))
# print(tc)
# print(100*"*")
import multiprocessing,threading,time
# def f1():
#     while True:
#         print(66)
# def f2():
#     while True:
#         print(77)
# li=[]
# for i in range(1):
#     p=multiprocessing.Process(target=f1)
#     p1=multiprocessing.Process(target=f2)
#     li.append(p)
#     li.append(p1)
# for j in li:
#     j.start()

def f1():
    while True:
        print(66)
def f2():
    while True:
        print(77)
# li=[]
# for i in range(2):
#     p=threading.Thread(target=f1)
#     p1=threading.Thread(target=f2)
#     li.append(p)
#     li.append(p1)
# for j in li:
#     j.start()

# p=threading.Thread(target=f1)
# p.start()
# p1=threading.Thread(target=f2)
# p1.start()

f2()
# import threading,time,multiprocessing
# def f1():
#     while True:
#         print(66)
#
# def f2():
#     for i in range(100):
#         print(9)
# t1=threading.Thread(target=f1)
# t2=threading.Thread(target=f2)
# t1.start()

# def f1():
#     while True:
#         print(66)
#         print(77)
#         t2.start()
# def f2():
#     for i in range(100):
#         print(9)
# t1=multiprocessing.Process(target=f1)
# t2=multiprocessing.Process(target=f2)
# t1.start()
li=["1","2","3","4"]

s="0"
for i in li:
   s+=i
   print(s)


# print(s)


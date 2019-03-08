# li = []
# for i in range(10):
#     li.append(lambda x=i: x)
#
# for i in li:
#     print(i())
#     print(i)

# squares = []
# for x in range(5):
#     squares.append(lambda i=x: i**2)
# print(squares[2](5))

# li = [lambda : x for x in range(10)]
# li1 = [i() for i in li]
# print(li1)
f_list = [lambda x, i=i: x**i for i in range(5)]
a = [f_list[j](10) for j in range(5)]

j_list = []
for i in range(5):
    j_list.append(lambda x,i=i: x**i)
b = [j_list[j](10) for j in range(5)]

g_list = []
for i in range(5):
    def la(x,i=i):
        return x**i
    g_list.append(la)
c = [j_list[j](10) for j in range(5)]
print(c)


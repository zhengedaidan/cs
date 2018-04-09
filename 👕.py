# -*- coding:utf-8 -*-
import datetime
a=datetime.datetime(2018,1,1)
str1="-2218-8-9"
import re
ret=re.search(r"([^-]+)([^-]+)([^-]+)",str1)
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))
# print(a+datetime.timedelta(days=31))
#
#
# b= datetime.datetime.strptime("2018-1-1","%Y-%m-%d")
# print(b.strftime("%Y:%m:%d"))
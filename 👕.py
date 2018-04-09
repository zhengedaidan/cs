# -*- coding:utf-8 -*-
import datetime
a=datetime.datetime(2018,1,1)
print(a+datetime.timedelta(days=1,hours=1))


b= datetime.datetime.strptime("2018-1-1","%Y-%m-%d")
print(b.strftime("%Y:%m:%d"))
from datetime import datetime,date,timedelta
import time
s="2018:08:08 08:08:08"
t=datetime.strptime(s,"%Y:%m:%d %H:%M:%S")
print(t)

t1=t+timedelta(days=6)
print(t1)

tu=datetime.utcnow()
print(tu)

tc=time.strptime(s, "%Y:%m:%d %H:%M:%S")
print(list(tc))
print(type(tc))
print(tc)
print(100*"*")

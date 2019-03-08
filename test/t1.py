from functools import wraps
import time


def limit_time(func):
    cache = {}
    key = func.__name__
    # 间隔1秒
    interval = 1
    # 次数10次
    times = 10

    @wraps(func)
    def inner(*args, **kwargs):
        if key in cache:
            called, update_time = cache[key]
            if time.time()-update_time <= interval:
                cache[key][0] += 1
            else:
                cache[key][0] = 1
        else:
            cache[key] = [1, time.time()]
        if cache[key][0] <= times:
            res = func(*args, **kwargs)
            cache[key][1] = time.time()
            return res
        else:
            print("limit/////////")
            return None
    return inner


@limit_time
def eat():
    print("eat")


for i in range(11):
    print(i)
    eat()




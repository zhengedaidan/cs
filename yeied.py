def fb_yeied(n):
    a,b=0,1
    while n>0:
        ret=yield b
        print(ret)
        a,b = b,a+b
        n -= 1

# li=list(fb_yeied(100))
gen=fb_yeied(100)
print(gen.send(None))
print(gen.send(10))
print(gen.send(22))



print(next(gen))
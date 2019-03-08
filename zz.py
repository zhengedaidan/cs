def warper1(f):
    print(f,"inner1")
    @warper2(f)
    def inner1():
        print("inner1")
    return inner1

def warper2(f):
    print(f, "inner2")
    def inner2():
        print("inner2")
    return inner2


@warper1
def cs():
    pass


cs()

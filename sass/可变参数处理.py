#测试可变参数的处理
def f1(a, b, *c):
    print(a, b, c)

f1(8, 9, 19, 20)


def f2(a, b, **c):
    print(a, b, c)

f2(8, 9, name = "tangzhanhao", age = 18)


def f3(a, b, *c, **d):
    print(a, b, c, d)

f3(8, 9, 20, 30, name = "tangzhanhao", age = 18)
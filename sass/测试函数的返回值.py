#测试函数的返回值
def add(a, b):
    print("计算两个数之和：{0},{1},{2}".format(a, b, (a+b)))
    return a+b
c = add(50,100)

print(c*10)
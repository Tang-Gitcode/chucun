#测试参数的传递
#传递可变参数

b = [10, 20]
def f2(m):
    print("m:", id(m))
    m.append(30)

f2(b)
print("b:", id(b))
print(b)
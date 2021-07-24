def func1():
    for i in range(11):
        print(f"北京打印第{i}次数据")
        yield


def func2():
    g = func1()
    next(g)
    for i in range(10):
        print(f"上海打印第{i}次数据")
        next(g)


if __name__ == "__main__":
    func2()

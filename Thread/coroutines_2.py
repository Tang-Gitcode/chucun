from time import time, sleep


def consumer(n):
    # while True:
    #     n = yield
    for i in range(n):
        sleep(1)
        print(f"生产了第{i}个产品")


def producter():
    consumer(5)
    # g = consumer()
    # next(g)
    for i in range(5):
        # g.send(i)
        print(f"消费了第{i}个商品")


if __name__ == "__main__":
    start = time()
    producter()
    end = time()

    print(end - start)

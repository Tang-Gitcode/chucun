"""商品上架进程"""

import threading as t
import os

def fun1():
    os.system("python ./功能自动化/TestCase/helixinxuan.py")

def fun2():
    os.system("python ./功能自动化/TestCase/helixinxuan_shop.py")

thread = []
t1 = t.Thread(target=fun1)
t2 = t.Thread(target=fun2)
t1.start()
t2.start()
thread.append(t1)
thread.append(t2)

if __name__ == "__main__":
    for i in thread:
        t.Thread.join(i)
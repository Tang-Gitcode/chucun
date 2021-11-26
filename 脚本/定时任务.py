# python的定时任务

import time
from datetime import datetime

def func():
    # 定时任务，自动化方法
    pass


def main():
    while True:
        # 获取当前时间
        now = datetime.now()
        # 小时等于xx,分钟等于xx
        if now.hour == 15 and now.minute == 28:
            print("任务开始执行")
            func()
        # 等待60秒
        time.sleep(60)


# 测试
if __name__ == "__main__":
    main()
# 测试_greenlet的使用

from greenlet import greenlet
# pip istall greenlet


def gf(name):
    print(f"{name}:我想买包包包！！")
    g2.switch("吕布")
    print(f"{name}:我想学编程！！！")
    g2.switch()


def bf(name):
    print(f"{name}:买！买！买！！！")
    g1.switch()
    print(f"{name}:一定去尚学堂学！！！")


if __name__ == '__main__':
    g1 = greenlet(gf)
    g2 = greenlet(bf)

    # 切换任务
    g1.switch("貂蝉")



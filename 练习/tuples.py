# 测试元组的使用
length = [50, 20]
print(length[0])        # 通过索引查看元素
print(length[1])


# 尝试修改元组中的元素(发现不可以，所以不能给元组的元素赋值)
# length[0] = 250
# print(length)

# 元组用，号标识，只定义一个元素时，后面一定要跟上一个，
n = (3, )


# 遍历元组中的所有值
length = [50, 20]
for i in length:
    print(i)


# 修改元组变量
length = [50, 20]
for i in length:
    print(i)

length = [100, 40]
for i in length:
    print(i)

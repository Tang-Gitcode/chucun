# 测试创建数字列表

# 打印数字
for i in range(1, 5):
    print(i)

for i in range(1, 6):
    print(i)


# 使用range创建数字列表
num = list(range(1, 6))
print(num)


# 指定步长
num = list(range(0, 6, 2))
print(num)


# 使用range()函数进行乘方运算
sums = []    # 定义一个空列表
for i in range(1, 11):      # 遍历i十遍
    num = i ** 2    # 定义一个临时变量
    sums.append(num)     # 将值添加到列表末尾
print(sums)      # 打印列表

sums = []
for i in range(1, 11):
    sums.append(i ** 2)
print(sums)



# 对数字列表执行简单的统计计算
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(nums))    # 打印列表的最小值
print(max(nums))    # 打印列表的最大值
print(sum(nums))    # 打印列表值的相加和



# 列表解析
sums = [num ** 2 for num in range(1, 11)]
print(sums)


# 测试对一个列表进行排序
cars = ["宝马", "奔驰", "特斯拉", "本田", "比亚迪"]

# 反向打印列表(永久性的修改列表元素的排列方式，但可以随时恢复，只需再次调用reverse()即可)
cars.reverse()
print(cars)

# sort()对元素的排列时永久性的
cars.sort()     # 按照正序排列
print(cars)


cars.sort(reverse=True)     # 按照倒序排列
print(cars)


# sorted()对元素的排序时临时的
cars = ["宝马", "奔驰", "特斯拉", "本田", "比亚迪"]
# 原始排序
print(cars)

# 临时排序
print(sorted(cars))

# 再次查看排序
print(cars)         # 还是原来的排序，并没有发生改变

# 使用倒序的方式进行临时排序
print(sorted(cars, reverse=True))

# 查看列表长度
print(len(cars))

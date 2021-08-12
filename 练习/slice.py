# 测试切片的使用
names = ["tang", "zhan", "hao", "tao", "can"]
print(names[0:3])
print(names[1:4])
print(names[:4])
print(names[2:])
print(names[-3:])   # 负数代表反向切片
print(names[-1:-6:-2])    # 第三个值代表步长，表示每隔多长取一个值


# 遍历切片
names = ["tang", "zhan", "hao", "tao", "can"]
for name in names[:3]:
    print(name.title())


# 复制列表
names = ["tang", "zhan", "hao", "tao", "can"]
friend_names = names[:]
print(names)
print(friend_names)

# 验证确实是两个列表
names.append("feng")
friend_names.append("haha")
print(names)
print(friend_names)


# 不使用切片进行赋值
names = ["tang", "zhan", "hao", "tao", "can"]
friend_names = names
names.append("feng")
friend_names.append("haha")
print(names)
print(friend_names)




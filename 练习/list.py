# 修改、添加和伤处元素

# 添加元素
name = ["hao", "tao", "can"]
print(name)
name.append("feng")
print(name)

name = []
name.append("hao")
name.append("tao")
name.append("can")
print(name)

# 插入元素
name = ["hao", "tao", "can"]
name.insert(0, "feng")
print(name)


# 删除元素  使用del方法
name = ["hao", "tao", "can"]
del name[0]
print(name)
del name[1]
print(name)


# 使用pop()方法删除元素
name = ["hao", "tao", "can"]
print(name)

names = name.pop()
print(name)
print(names)


name = ["hao", "tao", "can"]
last_name = name.pop()
print(f"最新购买的是:{last_name.title()}")


name = ["hao", "tao", "can"]
last_name = name.pop(0)
print(f"最新购买的是：{last_name.title()}")    # title()输出文本并将首字母大写

# 使用remove()方法删除元素

name = ["hao", "tao", "can"]
name.remove("tao")
print(name)


name = ["hao", "tao", "can"]
list_name = "tao"
name.remove("tao")
print(list_name)
print(f"\n{list_name.title()}对我来说太贵了！")






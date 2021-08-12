# 对切片进行练习

"""
切片
选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
"""

# 打印消息“The first three items in the list are:”，再使用切片 来打印列表的前三个元素。
name = ["tang", "zhan", "hao", "wo", "shi"]
print(name[0:3])

# 打印消息“Three items from the middle of the list are:”，再使 用切片来打印列表的中间三个元素。
name = ["tang", "zhan", "hao", "wo", "shi"]
print(name[1:4])

# 打印消息“The last three items in the list are:”，再使用切片 来打印列表的末尾三个元素。
name = ["tang", "zhan", "hao", "wo", "shi"]
print(name[-3:])

"""
你的比萨，我的比萨 
在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其赋给变量friend_pizzas ，再完成如下任务。
"""
pizzas = ["榴莲披萨", "虾仁披萨", "香辣披萨"]
friend_pizzas = pizzas[:]


# 在原来的比萨列表中添加一种比萨。
pizzas.append("蛋黄披萨")


# 在列表friend_pizzas 中添加另一种比萨。
friend_pizzas.append("草莓披萨")


# 核实有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；
# 打印消息“My friend's favorite pizzas are:”，再使用一个for 循环来打印第二个列表。核实新增的比萨被添加到了正确 的列表中。
print(pizzas)
print(friend_pizzas)
for i in pizzas:
    print(i)

for j in friend_pizzas:
    print(j)



"""
使用多个循环 
在本节中，为节省篇幅，程序 foods.py的每个版本都没有使用for循环来打印列表。
请选择一个版本的foods.py，在其中编写两个for循环，将各个食品列表打印出来
"""
names = ["tang", "zhan", "hao", "wo", "shi"]
names_copy = names[:]
print(names)
print(names_copy)

names_copy.append("feng")
print(names_copy)
names.append("haha")
print(names)

for i in names:
    print(i)

for j in names_copy:
    print(j)

# 测试对列表进行循环遍历

"""
比萨
想出至少三种你喜欢的比萨，将其名称存储 在一个列表中，再使用for 循环将每种比萨的名称打印出来。
"""
pizzas = ["榴莲披萨", "虾仁披萨", "香辣披萨"]
for pizza in pizzas:
    print(pizza)

# 修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，下面是一个例子。 I like pepperoni pizza.
for pizza in pizzas:
    print(f"我喜欢吃{pizza.title()}")

# 在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个 总结性句子，下面是一个例子。 I really love pizza!
for pizza in pizzas:
    print(f"我喜欢吃{pizza.title()}")
print("我超级喜欢吃披萨")




"""
动物 
想出至少三种有共同特征的动物，将其名称 存储在一个列表中，再使用for 循环将每种动物的名称打印出来。
"""

animals = ["猫", "老虎", "狮子"]
for animal in animals:
    print(animal)

# 修改这个程序，使其针对每种动物都打印一个句子，下面 是一个例子。 A dog would make a great pet.
for animal in animals:
    print(f"{animal.title()}会是很好的宠物")

# 在程序末尾添加一行代码，指出这些动物的共同之处，如 打印下面这样的句子。 Any of these animals would make a great pet!
for animal in animals:
    print(f"{animal.title()}会是很好的宠物")
print("这些动物都可以做宠物!")

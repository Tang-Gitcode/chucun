# 测试while循环的使用

# 测试从1数到5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 让用户选择何时退出
prompt = "\n告诉我点什么，我再重复给你听："
prompt += "\n输入'quit'结束程序"
message = ""
while prompt != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)


# 使用标志
prompt = "\n告诉我点什么，我再重复给你听："
prompt += "\n输入'quit'结束程序"
active = True
while active:
    message = input(prompt)
    if message == "quit":
        active = False
    else:
        print(message)


# 使用break结束循环
prompt = "\n告诉我点什么，我再重复给你听："
prompt += "\n输入'quit'结束程序"
while True:
    city = input(prompt)
    if city == "quit":
        break
    else:
        print(f"我很想去{city.title()}")


# 在循环中使用continue
# 从1数到10但是只打印奇数
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)



# 避免无限循环
x = 1
while x < 5:
    print(x)
    x += 1

# 练习： 披萨配料
pisiz = "\n请输入要加入的配料："
pisiz += "\n按'quit'结束程序"
while True:
    pisizs = input(pisiz)
    if pisizs == "quit":
        break
    else:
        print(f"\n我们将加入{pisizs}")

# 电影票
age = "\n请输入你的年龄："
while True:
    ages = int(input(age))
    if ages < 3:
        print("您的票价是0元")
    elif ages < 12:
        print("您的票价是10美元")
    else:
        print("您的票价是15美元")


# 三种出路
pisiz = "\n请输入要加入的配料："
pisiz += "\n按'quit'结束程序"
active = True
while active:
    pisizs = input(pisiz)
    if pisizs == "quit":
        active = False
    else:
        print(f"\n我们将加入{pisizs}")



"""使用while循环处理列表和字典"""
# 在列表之间移动元素
# 创建一个用于储存未验证用户的列表和一个用于储存已验证用户的空列表
unconfirmed_users = ["tang", "zhan", "hao"]  # 待验证用户
confirmed_users = []    # 已验证用户


# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print(f"验证用户：{current_users.title()}")
    confirmed_users.append(current_users)

# 显示所有已验证用户
print("\n以下用户已确认：")
# 遍历打印已验证用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 删除为特定值的元素
pets = ["dog", "cat", "mom", "cat", "key", "cat"]
print(pets)

# 循环删除指定值，知道列表中没有该值为止
while "cat" in pets:
    pets.remove("cat")
print(pets)


# 使用用户输入来填充字典
responses = {}

# 设置一个标志，支持调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\n你的名字是：")
    response = input("你想去爬哪座山:")

    # 将回答储存在字典中
    responses[name] = response

    # 看看是否还有人要参加调查
    repeat = input("还有人要参加调查吗（y/n）")
    if repeat == "n":
        polling_active = False

# 调查结束，显示结果
print("\n--- 调查结果 ---")
for name, response in responses.items():
    print(f"{name}喜欢爬{response}")


# 练习：熟食店
# 创建一个三明治名称列表
sandwich_orders = ["tang", "zhan", "hao"]
# 再创建一个已经做出来的三明治空列表
finished_sandwiches = []

# 循环列表，做出一个三明治就删除原列表添加到新列表
while sandwich_orders:
    current_orders = sandwich_orders.pop()
    finished_sandwiches.append(current_orders)

# 遍历新列表打印出做出来的所有的三明治
for finished_sandwiche in finished_sandwiches:
    print(f"我给你做了{finished_sandwiche}三明治")


# 五香烟熏牛肉卖完了
print("熟食店的五香烟熏牛肉（pastrami）卖完了")
sandwich_orders = ["tang", "pastrami", "zhan", "pastrami", "hao", "pastrami"]

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)

# 梦想的度假圣地
# 创建一个用来填充内容的空字典
responses = {}

# 调查是否还有人又要去的地方
polling_active = True

while polling_active:
    # 你的名字
    name = input("\n你的名字是：")
    response = input("如果说一个你梦想中的度假圣地，你想去哪：")

    # 将回答储存到字典中
    responses[name] = response

    # 看看是否还有人要说明
    repeat = input("\n还有人要参加调查吗？（y/n）")
    if repeat == "n":
        polling_active = False

print("--- 调查结果 ---")
for name, response in responses.items():
    print(f"{name}想去{response}")

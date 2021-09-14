# 定义函数
def greeter_user():
    """显示简单的问候语"""
    print("hello")


greeter_user()


# 向函数传递信息
def greeter_user(username):
    print(f"hello, {username.title()}")


greeter_user("tang")


# 练习
def display_message():
    print("我在本章学习了函数！")


display_message()


def favorite_book(title):
    print(f"我最喜欢的书之一是{title}")


favorite_book("<<西游记>>")

"""传递实参"""


# 位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print(f"\n我有一个{animal_type}")
    print(f"{animal_type}的名字是{pet_name}")


describe_pet("宠物", "tang")
describe_pet("dog", "monky")


# 关键字实参
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print(f"\n我有一个{animal_type}")
    print(f"{animal_type}的名字是{pet_name}")


describe_pet(animal_type="狗", pet_name="tang")
describe_pet(pet_name="tang", animal_type="狗")


# 默认值
def describe_pet(pet_name, animal_type="狗"):
    """显示宠物信息"""
    print(f"\n我有一个{animal_type}")
    print(f"{animal_type}的名字是{pet_name}")


describe_pet(pet_name="tang")


# 等效的函数调用
def describe_pet(pet_name, animal_type="狗"):
    """显示宠物信息"""
    print(f"\n我有一个{animal_type}")
    print(f"{animal_type}的名字是{pet_name}")


describe_pet("tang")
describe_pet(pet_name="tang")
describe_pet(pet_name="tang", animal_type="狗")
describe_pet(animal_type="tang", pet_name="狗")
describe_pet("狗", "tang")


# 练习
def make_shirt(size, name):
    """显示T恂信息"""
    print(f"\nT恤的名字是{name}")
    print(f"{name}T恤的尺码是{size}")


# 使用位置实参
make_shirt("175", "贵人鸟")
# 使用关键字实参
make_shirt(size=175, name="贵人鸟")


def make_shirt(size, name="i love you"):
    """显示T恂参数"""
    print(f"\nT恤上的字样是{name}")
    print(f"{name}T恤的尺码是{size}")


make_shirt("大号")
make_shirt("中号")
make_shirt("大号", name="其他字样")


def describe_city(name, countries):
    """显示城市信息"""
    print(f"\n城市名字为：{name}")
    print(f"{name}属于{countries}")


describe_city("巴黎", "法国")


def describe_city(name, countries="中国"):
    """显示城市信息"""
    print(f"\n城市名字为：{name}")
    print(f"{name}属于{countries}")


describe_city("上海")
describe_city("北京")
describe_city("巴黎", countries="法国")


"""返回值"""


# 返回简单值
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("tang", "zhanhao")
print(musician)


# 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("tang", "zhan", "hao")
print(musician)


# 设置中间值默认为空
def get_formatted_name(first_name, middle_name, last_name=""):
    """返回整洁的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


# 中间值不管有没有都能正常运行
musician = get_formatted_name("tang", "tao")
print(musician)


musician = get_formatted_name("tang", "zhan", "hao")
print(musician)


# 返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first" : first_name, "last": last_name}
    return person


# 这样直接返回了一个字典
musician = build_person("jimi", "hendrix")
print(musician)


# 增加可选形参age
def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", age=21)
print(musician)


# # 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# # 这是一个无限循环
# while True:
#     print("\n请告诉我你的名字: ")
#     f_name = input("first name：")
#     l_name = input("last name: ")
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nhello, {formatted_name}!")


# # 增加退出循环的方式
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:
#     print("\n请告诉我你的名字: ")
#     print("输入'q'退出")
#     f_name = input("first name：")
#     if f_name == "q":
#         break
#     l_name = input("last name: ")
#     if f_name == "q":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nhello, {formatted_name}!")
#

# 练习
def city_country(name, countries):
    full_name = f"{name}, {countries}"
    return full_name.title()


musician = city_country("shanghai", "china")
print(musician)

musician = city_country(name="beijing", countries="china")
print(musician)

musician = city_country("杭州", countries="china")
print(musician)


"""
先写一个循环，随机生成100个数的数组，放入数组 再写一个循环，计算这个数组中所有奇数的和，并输出再写一个循环，
计算下标（索引）为奇数的数和，并输出
"""
import random
# 定义一个用来装100个随机数的空列表
a = []
# 定义累加和的初始值
sum = 0
# 遍历循环100次，得出一百个随机数
for i in range(100):
    a.append(random.randint(0, 100))        # 将100个随机数逐个添加到a列表的末尾

# 打印列表
print(a)


# 遍历a列表
for j in a:
    # 判断j是否为奇数
    if j % 2 == 1:
        sum += j
# 求和
print(sum)

# 下标为奇数的累加和
num = 0
c = a[1::2]     # 从下标1开始，每隔两个下标获取
print(c)

for k in c:
    num += k

print(f"累加和：{num}")



# 练习
def make_album(name, album, number=None):
    full_name = f"{name} {album} {number}"
    return full_name.title()

album_name = make_album("zhang", "yueliang")
print(album_name)

album_name = make_album(name="zhou", album="gaobai")
print(album_name)

album_name = make_album("xu", album="suyan")
print(album_name)

album_name = make_album("tang", album="zhanhao", number=5)
print(album_name)

# 练习 用户的专辑
def make_album(name, album, number=None):
    full_name = f"{name} {album} {number}"
    return full_name.title()

while True:
    print("\n请输入专辑信息！")
    print("输入Q退出")
    f_name = input("请输入歌手的名称：")
    if f_name == "Q":
        break
    l_album = input("请输入专辑名称：")
    if l_album == "Q":
        break
    # t_num = input("请输入专辑数量：")
    # if t_num == "Q":
    #     break

    information = make_album(f_name, l_album)
    print(f"\n{information}")

"""传递任意数量的实参"""


# *表示创建一个名为topppings的空元组，并将所有的值都封装到这个元组中
def make_pizza(*toppings):
    # 打印顾客点的所有配料
    print(toppings)


make_pizza("意大利辣香肠")
make_pizza("蘑菇", "青椒", "额外的奶酪")


# 将print()替换为循环
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\n做一个带有以下配料的比萨：")
    for topping in toppings:
        print(f"配料有：{topping}")


make_pizza("意大利辣香肠")
make_pizza("蘑菇", "青椒", "额外的奶酪")


"""结合使用位置实参和任意数量实参"""


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\n做一个带有以下配料的比萨：")
    for topping in toppings:
        print(f"{size}寸的比萨，配料中包含：{topping}")


make_pizza(5, "意大利辣香肠")
make_pizza(16, "蘑菇", "青椒", "额外的奶酪")


"""使用任意数量的关键字实参"""


def bulid_profile(first, last, **user_info):
    """创建一个字典，里面包含我们知道的有关用户的一切。"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = bulid_profile("albert", "einstein", lacation="princeton", field="physics")
print(user_profile)


# 练习  三明治
def sandwich(*toppings):
    """接受顾客在三明治中添加的一系列食材"""
    print("\n做一个带有以下配料的三明治：")
    for topping in toppings:
        print(f"配料包括：{topping}")


sandwich("香肠")
sandwich("香菇", "青椒")
sandwich("洋葱", "韭菜", "葱")


# 练习  用户简介
def bulid_profile(first, last, **user_info):
    """创建一个字典，里面包含我们知道的有关用户的一切。"""
    user_info["first_name"] = first
    print(f"姓名：{first}")
    user_info["last_name"] = last
    print(f"性别：{last}")
    return user_info


user_profile = bulid_profile(first="唐展豪", last="男", lacation="princeton", field="physics", third="zhan")
print(user_profile)


# 练习    汽车
def make_car(model, manufacturers, **keyword):
    """接受汽车的一切信息"""
    keyword["number"] = model
    keyword["make"] = manufacturers
    return keyword


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(1))
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

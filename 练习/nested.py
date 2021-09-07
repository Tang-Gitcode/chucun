# 测试嵌套的使用
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# 创建一个储存外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)


# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print(f"外星人总数：{len(aliens)}")


"""创建外星人"""
# 创建一个储存外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

# 修改前3个外星人的颜色以及速度和分值
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print(f"外星人总数：{len(aliens)}")


"""在字典中储存列表"""
# 储存所点披萨的信息
pizza = {
    "面包皮": "厚",
    "配料": ["蘑菇", "奶酪"],
}

# 概述所点的披萨
print(f"您点了一份{pizza['面包皮']}的披萨,上面的配料如下：")

for topping in pizza['配料']:
    print(topping)

"""查看所有人喜欢的语言是什么"""
# 添加一个字典，包含所有人喜欢的语言
favorite_languages = {
    "tang": ["python", "ruby"],
    "zhan": "c",
    "hao": ["c", "ruby"],
    "tao": ["python", "haskell"],
}

# 遍历字典中的人名
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}最喜欢的语言是：")
    # 再次遍历字典中的语言
    for language in languages:
        print(f"\t{language.title()}")

favorite_languages = {
    "tang": ["python", "ruby"],
    "zhan": "c",
    "hao": ["c", "ruby"],
    "tao": ["python", "haskell"],
}


# 在字典中储存字典
users = {
    "tang": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
        },
    "zhan": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
        },
    }

for username, user_info in users.items():
    print(f"\n名称是：{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info["location"]

    print(f"\t全名是：{full_name.title()}")
    print(f"\t地点是：{location.title()}")


# 练习  人们
#     people_0 = {"name": "tang", "age": 18}
#     people_1 = {"name": "tang", "age": 19}
#     people_2 = {"name": "tang", "age": 20}
# people = [people_0, people_1, people_2]
#
# for username in people:
#     print(username)


# 宠物
pet_0 = {"name": "tang", "type": "teddy"}
pet_1 = {"name": "zhan", "type": "labrador"}
pet_2 = {"name": "hao", "type": "Second"}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    print(pet)


# 喜欢的地方
favorite_places = {
    "tang": {"大理", "洱海", "芜湖"},
    "zhan": {"雪山", "大明湖畔", "西湖"},
    "hao": {"武当山", "泰山", "九龙洞"}
    }

for name, value in favorite_places.items():
    print(f"{name}喜欢的地方是：{value}")


# 喜欢的数2

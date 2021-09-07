# 测试字典的使用
alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
new_alien = alien_0["points"]
print(f"你获得了{new_alien}分")


# 添加键值对
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)


# 先创建一个空字典
alien_0 = {}
alien_0["color"] = "green"
alien_0["points"] = "5"
print(alien_0)


# 修改字典中的值
alien_0 = {"color": "green"}
print(f"外星人颜色是：{alien_0['color']}")

alien_0["color"] = "yellow"
print(f"新外星人的颜色是：{alien_0['color']}")


"""计算外星人移动的距离"""
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"最初的位置：{alien_0['x_position']}")
# 向右移动外星人
# 根据当前速度计算外星人向右移动多远
if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3

# 新位置为旧位置加上移动距离
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"新位置：{alien_0['x_position']}")


# 删除键值对
# del彻底删除键值对
alien_0 = {"color": "green", "points": 5}
print(alien_0)

del alien_0["points"]
print(alien_0)

# 由类似对象组成的字典
sn_peoples = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }
language = sn_peoples["tang"].title()
print(f"tang最喜欢的语言是{language}")


# 使用git()来访问值
alien_0 = {"color": "green", "speed": "slow"}
point_value = alien_0.get("points", "没有该值")
print(point_value)
# print(alien_0["points"])

# 练习
peoples = {"first_name": "zhanhao", "last_name": "tang", "age": "20", "city": "shanghai"}
print(peoples)

# 最喜欢的数字
nums = {
    "tang": 1,
    "zhan": 2,
    "hao": 3,
    "tao": 4,
    "feng": 5
    }
print(nums)
num = nums["tang"]
print(f"tang最喜欢的数字是：{num}")

# 词汇表
vocabularys = {
    "if": "判断语句",
    "for": "循环",
    "title": "首字母大写",
    "list": "列表",
    "tuples": "元组"
    }
for vocabulary in vocabularys:
    # print(f"{vocabulary}的含义是\n{vocabularys[vocabulary]}")
    print(f"{vocabulary}的含义是:{vocabularys[vocabulary]}")


# 遍历字典
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
    }
for key, value in user_0.items():
    print(f"\nkey:{key}")
    print(f"\nvalue:{value}")


sn_peoples = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }
for name, language in sn_peoples.items():
    print(f"\n{name}最喜欢的语言是：{language}")

# 遍历字典中的所有键
sn_peoples = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }
for name in sn_peoples.keys():
    print(name.title())


favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }
friends = ["zhan", "tao"]
for name in favorite_languages:
    print(f"你好{name}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, 你喜欢的语言是：{language}!")


favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }

if "erin" not in favorite_languages.keys():
    print("erin, 请帮我们投票")


favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, 谢谢你帮我们投票")


favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "ruby",
    "tao": "java"
    }
print("已经提到了以下几种语言：")
for name in favorite_languages.values():
    print(name.title())

favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "java",
    "tao": "java"
    }

print("已经提到了以下几种语言：")
for name in set(favorite_languages.values()):
    print(name.title())

languages = {"java", "c", "python", "ruby"}
print(languages)


# 练习
favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "java",
    "tao": "java"
    }
for name in favorite_languages:
    print(f"{name.title()}喜欢的语言是{favorite_languages[name]}")

# 河流，用字典表示
rivers = {
    "nlie": "egypt",
    "Yellow River": "china",
    "Mississippi River": "America"
    }

# 遍历循环
for name in rivers:
    print(f"{name.title()}流经{rivers[name].title()}")

# 打印河流名字
for name in rivers.keys():
    print(name.title())

# 打印国家名字
for name in rivers.values():
    print(name.title())


favorite_languages = {
    "tang": "python",
    "zhan": "C",
    "hao": "java",
    "tao": "java"
    }
for name in favorite_languages:
    print(f"{name.title()}， 谢谢你帮我们投票")
if "nali" not in favorite_languages:
    print("nali请你帮我们投票")

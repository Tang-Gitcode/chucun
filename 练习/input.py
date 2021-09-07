# 测试用户输入与while循环

message = input("请输入一个数字：")
print(f"你输入的数字是:{message}")



# 编写清晰的程序
name = input("请输入你的名字：")
print(f"\nhello, {name}!")

# 提示超过一行
prompt = "如果你告诉我们你是谁，我们可以个性化你看到的信息"
prompt += "\n告诉我你是谁？"

name = input(prompt)
print(f"\nhello, {name}!")


# 使用int()获取数值输入
age = input("你多大了？")
age = int(age)      # 将输入的字符转为int()类型
print(age)
print(age >= 18)


height = input("你身高多少厘米？")
height = int(height)
if height >= 48:
    print("\n你够高了，可以骑马了")
else:
    print("\n你再大一点就可以骑马了")


# 求模运算符
number = input("输入一个数字，我会告诉你它是偶数还是奇数")
number = int(number)

if number % 2 == 0:
    print(f"\n{number} 是偶数")
else:
    print(f"\n{number} 是奇数")



# 练习： 汽车租凭
car = input("请输入你要租的汽车型号:")
print(f"\n你要租的汽车是：{car}")

# 餐馆订位
people = input("欢迎光临，请问几位？")
people = int(people)

if people > 8:
    print("不好意思，没有空位了")
else:
    print("你好，还有空桌，请跟我来")

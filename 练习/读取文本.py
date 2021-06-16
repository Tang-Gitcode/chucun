# coding = utf-8

# txt = open(r"score.txt", encoding="utf-8")
# num1 = float(input("请输入第一门成绩："))
# num2 = float(input("请输入第二门成绩："))
# num3 = float(input("请输入第三门成绩："))
# sum = str((num1+num2+num3)/3)
# print("平均分为："+sum)
#
# for i in txt:
#     print(i)


import re

with open('./score.txt', 'r', encoding='utf-8') as f:
    content_list = f.readlines()

new_dict = dict()
for i in range(len(content_list)):
    new_dict[i] = content_list[i]

print(new_dict)

dict2 = dict()
for index, content in enumerate(content_list):
    nums = re.findall(r'\d+', content)
    num_list = list()
    for num in nums:
        num_list.append(int(num))
    dict2[index] = sum(num_list) / 3
    print("平均分为："+str(dict2[index]))


new_list = list()



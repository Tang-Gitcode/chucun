import random
name = ['jian', 'hao', 'wei', 'feng', 'can', 'jun']
# del name[2: 6]
# for i in name:
#     print(f"{i.title()}先生/女士，很抱歉，无法邀请您来共进晚餐。")
# print(name)


for i in name[2:6]:
    list_name = name.pop()
    print(f"{i.title()}先生/女士，很抱歉，无法邀请您来共进晚餐。")

for j in name:
    print(f"{j.title()}先生/女士，你依旧在我的受邀之列。")

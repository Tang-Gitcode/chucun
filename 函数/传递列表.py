"""传递列表"""

def greet_users(names):
    """向列表中的每位用户发出简单的问候"""
    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)


usernames = ["tang", "zhan", "hao"]
greet_users(usernames)


"""在函数中修改列表"""
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()    # 逐个删除列表中末尾的元素
    print(f"打印设计:{current_design}")
    completed_models.append(current_design)  # 将暂存的元素一个一个加入该列表末尾

# 显示打印好的所有模型
print("\n以下型号已打印出来：")
for completed_model in completed_models:
    print(completed_model)



"""使用函数表示"""
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"打印设计：{current_design}")
        completed_models.append(current_design)

def show_complted_models(completed_models):
    """显示打印好的模型"""
    print("\n以下型号已打印出来：")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

# [:]表示创建列表的副本
print_models(unprinted_designs[:], completed_models)
show_complted_models(completed_models)
# print(unprinted_designs)


"""练习"""
# 消息
def show_messages(texts):
   for text in texts:
       msg = f"\nhello, {text}"
       print(msg)

texts = ["tang", "zhan", "hao"]
show_messages(texts)


# 发送消息
def show_messages(texts, sent_messages):
    """列表中的数据删除存入空列表"""
    while texts:
        current_text= texts.pop()
        print(f"打印消息：{current_text}")
        sent_messages.append(current_text)


def send_messages(sent_messages):
    """显示打印好的消息"""
    print("\n下列消息已打印：")
    for sent_message in sent_messages:
        print(sent_message)


texts = ["tang", "zhan", "hao"]
sent_messages = []

show_messages(texts, sent_messages)
send_messages(sent_messages)
print(texts)
print(sent_messages)


# 消息归档
texts = ["tang", "zhan", "hao"]
sent_messages = []

# 创建副本列表并传值给函数
show_messages(texts[:], sent_messages)
send_messages(sent_messages)
print(texts)
print(sent_messages)


#测试定义类
class Student:
    def __init__(self, name, score):    #self必须位于第一个参数
        self.name = name
        self.score = score


    def say_Score(self):
        print("{0}的分数是：{1}分".format(self.name, self.score))


s1 = Student("唐展豪", 60)
s1.say_Score()
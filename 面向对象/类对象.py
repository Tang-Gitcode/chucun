#测试类对象的生成
'''
class Student:
    pass    #空语句

print(type(Student))
print(id(Student))

Stu2 = Student
s1 = Stu2()
print(s1)

'''



class Student:
    def __init__(self, name, score):    #self必须位于第一个参数
        self.name = name
        self.score = score


    def say_score(self):
        print("{0}的分数是：{1}分".format(self.name, self.score))

Stu2 = Student

s1 = Student("唐展豪", 60)
s2 = Stu2("唐小豪", 100)

s1.say_score()
s2.say_score()
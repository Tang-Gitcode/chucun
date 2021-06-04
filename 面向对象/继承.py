#测试继承的基本使用

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age        #私有属性

    def say_age(self):
        print("名字我也不知道呢")

class Student(Person):


    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score



print(Student.mro())


s = Student("唐展豪", 18, 60)
s.say_age()
print(s.name)
#print(s.age)
print(dir(s))
print(s._Person__age)
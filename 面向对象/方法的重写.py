#测试方法的重写

class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age


    def say_age(self):
        print("我的年龄是：", self.__age)


    def say_name(self):
        print("我的名字是：{0}".format(self.name))



class Student(Person):


    def __init__(self, name, age, score):
        Person.__init__(self, name, age)
        self.score = score



s = Student("唐展豪", 18, 80)
s.say_age()
s.say_name()

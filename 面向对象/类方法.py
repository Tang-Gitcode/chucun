#测试使用类方法
from BaseClass import BaseClass

class Student:
    company = "SXT"         #类属性

    @classmethod
    def printCompany(cls):
        print(cls.company)


Student.printCompany()



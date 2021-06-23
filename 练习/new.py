# 测试输入月薪，计算年薪

salary = input("请输入月薪：")


class SalaryAccount:
    '''工资计算类'''
    def __call__(self, salary):

        print("算工资啦......")
        yearSalary = salary*12
        daySalary = salary // 24
        hourSalary = daySalary // 8
        return dict("年薪为："+yearSalary, "月薪为："+salary, "日薪为："+daySalary, "时薪为："+hourSalary)


print(salary)

# import xlrd
# from xlrd import sheet
# data = xlrd.open_workbook("C:/Users/administered/Desktop/goods.xls")
# sheet = data.sheet_by_index(0)
# # 获取行数
# sheet_nrows = sheet.nrows
# # 获取列数
# sheet_ncols = sheet.ncols
# # for j in range(1, sheet_nrows):
# #     for i in range(0, sheet_ncols):
# #         list = sheet.cell_value(j, i)
# #         print(list)
# #     continue

# j = 1
# i = 0
# while j < sheet_nrows:
#     while i < sheet_ncols:
#         list = sheet.cell_value(j, i)
#         print(list)

# import pandas as pd
# df = pd.read_excel('C:/Users/administered/Desktop/goods.xls')
# data = df.values


# print(data[0][0])

class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性，私有属性在类外部无法直接进行访问
    _weight = 0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print("%s 说:我%d岁。" %(self.name,self.age))
p = people('runnob', 10, 30)
p.speak()
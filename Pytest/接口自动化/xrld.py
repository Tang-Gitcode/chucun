# 加载读取excel文档的模块
import xlrd

excel = xlrd.open_workbook(u"C:/Users/administered/Desktop/login.xls")

# 获取索引为0的工作表
table = excel.sheets()[0]
print(table)


# 获取总共有多少行
nrows = table.nrows
print("总行数：", nrows)
print("该文档有%i行" %nrows)


# 获取总列数
nlows = table.ncols
print("总列数：", nlows)
print("该文档有%i列" %nlows)


# 获取第一行数据
row_values = table.row_values(0)
print(row_values)

# 获取第一列的内容
col_values = table.col_values(0)
print(col_values)


# # 获取指定单元格
# data = table.cell(3,0).value
# print(data)


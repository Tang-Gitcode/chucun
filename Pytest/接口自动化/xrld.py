# 加载读取excel文档的模块
import xlrd

xl = xlrd.open_workbook(r"C:\Users\administered\Desktop\测试用例\全局设置.xls")

# 获取索引为0的工作表
table = xl.sheets()[0]
print(table)

# 获取总共有多少行
rows = table.nrows
print(rows)

# 获取第一行数据
row = table.values()
print(row)

# 获取第一列的内容
col = table.col_values(0)
print(col)

# 获取指定单元格
data = table.cell(3,0).value
print(data)


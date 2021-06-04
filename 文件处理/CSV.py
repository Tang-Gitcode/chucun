#测试CSV文件的读取与写入
import csv
with open(r"a.csv", "r", encoding = "GBK") as f:
    a_csv = csv.reader(f)
#    print(a_csv)
    for row in a_csv:
        print(row)
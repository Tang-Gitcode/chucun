import pymysql
from pymysql import cursors


# 定义连接方法
def get_object():
    # 获取连接对象，建立数据库连接（host：地址，port:接口，user:账号，passwd:密码，db：数据库名）
    obj = pymysql.connect(host="rm-uf67h55frc456p9ij5o.mysql.rds.aliyuncs.com", port=3306, user="tst_sass", passwd="sass#123123", db="sass")
    return obj


"""单表查询"""
# 定义查询方法
def select(sql, args):
    obj = get_object()
    cur = obj.cursor()
    cur.execute(sql, args)
    results = cur.fetchall()

    # 查看数据类型
    # print(type(results))

    
    # 遍历results
    for row in results:
        # 打印查询数据
        print(row)
        # admin_id = row[0]
        # account = row[1]
        # name = row[2]
        
        # print("admin_id"+str(admin_id) + "account"+str(account) + "name"+str(name))

    # 提交
    # obj.commit()
    # 关闭
    # cur.close()
    # obj.close()
        


if __name__ == "__main__":
    # 查询表
    sql = "SELECT * FROM `sass`.`admin` LIMIT 0, 1000"
    # sql = "SELECT * FROM `sass`.`shop_goods` WHERE `shop_id` = '437' AND `is_sale` = '1' AND `goods_sn` LIKE '%J%' LIMIT 0, 1000"
    select(sql, None)
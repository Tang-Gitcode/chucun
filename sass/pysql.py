import pymysql

db = pymysql.connect(
    host='rm-uf67h55frc456p9ij5o.mysql.rds.aliyuncs.com',
    port = 3306,
    user="tst_sass",
    passwd="sass#123123",
    db="sass",
    charset="utf8",
)

w = db.cursor()
w.execute("select * from admin where admin_id = 101")

print(w.fetchall())
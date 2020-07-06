import pymysql

class mysql_data():
    def sql_data(self,sql_input):
        # 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
        db = pymysql.connect("192.168.1.2", "root", "pirate@625")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # SQL 查询语句
        sql = sql_input

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            return results

        except:
            print("Error: unable to fecth data")

        # 关闭数据库连接
        db.close()


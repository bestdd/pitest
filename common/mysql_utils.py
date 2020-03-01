import MySQLdb


def query(sql):
    db = MySQLdb.connect("localhost", "root", "root", "itest", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    return len(results)

if __name__ == '__main__':
    print(query('SELECT * FROM test_table where order_no=222888000 and state=1;'))
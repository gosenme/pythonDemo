from pymysql import *
import json


def connectDb():
    db = connect(host="172.18.80.58", port=3307, user="seewo_remote", passwd="seewo_remote@cvte",
                 db="seewo_iot_app_ucp", charset='utf8')
    return db


db = connectDb()


# 创建表
def crate_table(db):
    cursors = db.cursor()
    sql = '''CREATE TABLE persons
            (id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            age INT NOT NULL,
            address CHAR(50),
            salary REAL);
        '''
    try:
        cursors.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
        return False


def insert_records(db):
    cursors = db.cursor()
    try:
        cursors.execute("DELETE FROM persons")
        cursors.execute(
            "INSERT INTO persons (id,name,age,address,salary) VALUES (1,\'WGX1\',30,\'california1\',10000)");
        cursors.execute(
            "INSERT INTO persons (id,name,age,address,salary) VALUES (2,\'WGX2\',30,\'california2\',20000)");
        cursors.execute(
            "INSERT INTO persons (id,name,age,address,salary) VALUES (3,\'WGX3\',30,\'california3\',30000)");
        db.commit()
        return True
    except Exception as e:
        print(e)
        db.rollback()
        return False


def select_records(db):
    cursors = db.cursor()
    sql = 'SELECT name,age,salary FROM persons ORDER BY age DESC'
    cursors.execute(sql)
    results = cursors.fetchall()
    print(results)
    fields = ['name', 'age', 'salary']
    records = []
    for row in results:
        records.append(dict(zip(fields, row)))
    return json.dumps(records)


if crate_table(db):
    print('成功创建person表')
else:
    print("person表已经存在")

if insert_records(db):
    print("成功新增记录")
else:
    print("插入记录失败")

print(select_records(db))
db.close()

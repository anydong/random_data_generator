import pymysql
import threading
from generator import address

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='test')


def insert():
    cursor = connect.cursor()
    sql_str = "INSERT INTO account (user_name, email) VALUES (%s,%s)"
    values = []
    for i in range(100):
        values.append((address.address(), 'email'))
    cursor.executemany(sql_str, values)
    connect.commit()


for num in range(1000):
    t = threading.Thread(target=insert, name='ccc')
    t.start()
    t.join()
    print(num)

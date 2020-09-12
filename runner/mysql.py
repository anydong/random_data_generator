import pymysql
import threading
from generator import address

connect = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='test')


def insert():
    cursor = connect.cursor()
    sql_str = "INSERT INTO account (user_name, email) VALUES ('%s','%s')" % (address.address(), 'file_md5')
    cursor.execute(sql_str)
    connect.commit()


for num in range(2000000):
    t = threading.Thread(target=insert, name='ccc')
    t.start()
    t.join()

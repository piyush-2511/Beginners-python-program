#MYSQL - PYTHON CONNECTOR

import mysql.connector as c
con = c.connect(host='localhost',user='root',passwd='123456',database='customers')

if con.is_connected():
    print('successfull')


cursor=con.cursor()


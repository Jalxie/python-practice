# coding:utf-8
import random
import string
import os
import mysql.connector
import sys


# Connect to DB
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="x0x9q8..",
  database="pythonquestion",
  ##specify it, not use default
  auth_plugin ='mysql_native_password'
)

print(mydb)
mycursor = mydb.cursor()

#create a database

# mycursor.execute("CREATE DATABASE pythonquestion")

#check if it exists
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

#create table
# mycursor.execute("""CREATE TABLE promcode(
#    id INT AUTO_INCREMENT,
#    code VARCHAR(10),
#    register_date DATETIME,
#    PRIMARY KEY(id)
# );""")



# 激活码生成
def activation_code(count, length):    
    # count 数量    
    # length 长度    
    base = string.ascii_uppercase + string.ascii_lowercase + string.digits    # 生成激活码可能包含的字符集（大写字母、小写字母、数字）
    return [''.join(random.sample(base, length)) for i in range(count)]


promotioncode = activation_code(200, 16)
# activation_code(200, 16)   # 获取10个长度为16个字符的激活码
print(promotioncode[1])

for n in promotioncode:
	sql = "INSERT INTO promcode (code) VALUES (%s)",promotioncode
	mycursor.execute(sql)
	mydb.commit()





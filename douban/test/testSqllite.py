# -*- codeing = utf-8 -*-
# @Time : 2021/6/23 19:50
# @Auther :  zhangtao
# @File  : testSqllite.py
# @Software  : PyCharm


import sqlite3
# 创建数据库

# conn = sqlite3.connect("test.db")
#
# print("成功打开数据库")
#
# c = conn.cursor()   # 获取游标
#
# sql = '''
#     create table company
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real);
#
# '''
#
# c.execute(sql)  # 执行sql语句
# conn.commit()   # 提交数据库操作
# conn.close()
# print("成功建表")

# 插入数据
# conn = sqlite3.connect("test.db")
# c = conn.cursor()   # 获取游标
#
# sql1 = '''
#     insert into company (id,name,age,address,salary)
#     values (1,'张三',32,"成都",8000)
# '''
#
# sql2 = '''
#     insert into company (id,name,age,address,salary)
#     values (2,'李四',30,"广西",15000)
# '''
#
# c.execute(sql1)  # 执行sql语句
# c.execute(sql2)  # 执行sql语句
# conn.commit()   # 提交数据库操作
# conn.close()
# print("成功建表")
# 查询数据
conn = sqlite3.connect("test.db")
c = conn.cursor()   # 获取游标

sql = "select id,name,address,salary from company"
cursor = c.execute(sql)  # 执行sql语句

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3])
conn.close()
print("查询完毕")
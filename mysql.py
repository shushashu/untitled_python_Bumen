#!/usr/bin/python
# -*- coding:utf-8 -*-
# 用于处理mysql数据存储相关内容

import pymysql

# connect = pymysql.Connect(
#     host='localhost',
#     port=3310,
#     user='woider',
#     passwd='3243',
#     db='python',
#     charset='utf8'
# )
#
# # 获取游标
# cursor = connect.cursor()
#
# # 插入数据
# sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
# data = ('雷军', '13512345678', 10000)
# cursor.execute(sql % data)
# connect.commit()
# print('成功插入', cursor.rowcount, '条数据')


class mysql (object):
    __connect= {
        "host":'localhost',
        "port":3306,
        "user":'root',
        "passwd":'root',
        "db":'bumen',
        "charset":'utf8',
        # "cursorclass":pymysql.cursors.DictCursor,
    }

    def __init__(self,sql,data):
        self.sql=sql
        self.data=data
        self.connect=pymysql.connect(**self.__connect)
        self.cursor = self.connect.cursor()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def __sql(self):
        self.cursor.execute(self.sql,self.data)
        self.connect.commit()
        return self.cursor.rowcount

    def select(self):
        return self.__sql()

    def insert(self):
        return self.__sql()

    def update(self):
        return self.__sql()

# sql = "INSERT INTO userinfo (nickname, password, trade_no, bubi_address,myset,username,statu) VALUES ( %s, %s, %s,%s,%s, %s,%s)"
# data=(
# 	"nickname",
# 	"""userdata["password"]""",
# 	"""userdata["trade_no"]""",
# 	"""a[0]["data"]["bubi_address"]""",
# 	"""userdata["metadata"]""",
# 	"""userdata["username"]""",
# 	1
# )
# i = mysql(sql,data)
# a=i.insert()
# print(a)
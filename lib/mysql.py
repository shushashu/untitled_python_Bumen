#!/usr/bin/python
# -*- coding:utf-8 -*-
# 用于处理mysql数据存储相关内容

import pymysql


class mysql(object):
    __connect = {
        "host": 'localhost',
        "port": 3306,
        "user": 'root',
        "passwd": 'root',
        "db": 'bumen',
        "charset": 'utf8',
        # "cursorclass":pymysql.cursors.DictCursor,
    }

    def __init__(self, sql):
        self.sql = sql
        self.connect = pymysql.connect(**self.__connect)
        self.cursor = self.connect.cursor()

    def __del__(self):
        self.cursor.close()
        self.connect.close()

    def __sql(self):
        self.cursor.execute(self.sql)
        self.connect.commit()
        return self.cursor.rowcount

    def select(self):
        return self.sql()

    def insert(self):
        return self.__sql()

    def update(self):
        return self.__sql()

    def delete(self):
        return self.__sql()

class select(mysql):

    def __init__(self,sql):
        mysql.__init__(self,sql)

    def __del__(self):
        self.cursor.close()
        self.connect.close()


    def select(self):
        self.cursor.execute(self.sql)
        return self.cursor.fetchall()
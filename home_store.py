# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql


def home_store():
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ['id', 'company_name', 'company_address' , 'main_product']

        # 查询条件
        condition = {}

        # 生成SQL语句
        query = sql.select("vendor", key, condition, 0)

        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            data = cursor.fetchall()

            result = []
            for row in data:
                dict_commo = dict()
                dict_commo["id"] = row[0]
                dict_commo["name"] = row[1]
                dict_commo["address"] = row[2]
                dict_commo["star"] = row[3]

                result.append(dict_commo)

            # 关闭数据库连接
            db.close()

            return True, "获取入驻商家成功", result

        else:
            return False, "查询失败", "null"


    except:
        return False, "无法连接数据库" , "null"

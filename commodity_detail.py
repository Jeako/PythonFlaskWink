# !/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = "Jeako_Wu"
import sql
import pymysql

from db_link import company_name2vendor_id
from db_link import commodity_id2company_name

def commodity_detail(id):
    try:
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "wujiahao.", "flaskTest",charset='utf8')

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 查询字段
        key = ['id', 'name', 'info', 'ingredient', 'feature', 'manufacture', 'average_price']

        # 查询条件
        condition = {}
        condition['id'] = id

        # 生成SQL语句
        query = sql.select("commodity", key, condition, 0)
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        if cursor.execute(query):
            # 获取结果
            data = cursor.fetchone()

            dict_commo = {}
            dict_commo["id"] = data[0]
            dict_commo["name"] = data[1]
            dict_commo["info"] = data[2]
            dict_commo["ingredient"] = data[3]
            dict_commo["feature"] = data[4]
            dict_commo["manufacture"] = data[5]
            dict_commo["average_price"] = data[6]

            stores = []

            store_names = commodity_id2company_name(id)
            for row in store_names:
                store_dict = company_name2vendor_id(row)
                stores.append(store_dict)

            dict_commo["stores"] = stores
            # 关闭数据库连接
            db.close()

            return True, "获取商品信息成功" ,dict_commo

        else:
            return False, "获取商品信息失败", "null"


    except:
        return "无法连接数据库"

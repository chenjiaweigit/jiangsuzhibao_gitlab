#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
import pymysql
from common.yaml_util1 import load_ini

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = load_ini(data_file_path)["mysql"]

# DB_CONF = {
#     "host": data["MYSQL_HOST"],
#     "port": int(data["MYSQL_PORT"]),
#     "username": data["MYSQL_USER"],
#     "password": data["MYSQL_PASSWD"],
#     "database": data["MYSQL_DB"]
# }
host = data["MYSQL_HOST"]
port = int(data["MYSQL_PORT"])
username = data["MYSQL_USER"]
password = data["MYSQL_PASSWD"]
database = data["MYSQL_DB"]

mydb = pymysql.connect(
    host=host,
    port=port,
    user=username,
    passwd=password,
    db=database,
    charset='utf8'
)
mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
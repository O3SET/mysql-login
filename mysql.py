import mysql.connector
import os

# MySQL连接信息
host = 'localhost'
user = 'root'
password = 'password'

# 遍历文件
filename = '3306.txt'
with open(filename, 'r') as f:
    for line in f:
        # 读取每行的IP、用户名、密码
        ip, username, pwd = line.strip().split(' ')
        try:
            # 尝试连接MySQL数据库
            cnx = mysql.connector.connect(host=ip, user=username, password=pwd)
            print(f"成功连接到MySQL数据库，IP: {ip}, 用户名: {username}, 密码: {pwd}")
            cnx.close()
        except mysql.connector.Error as err:
            # 连接失败，打印错误信息
            print(f"连接MySQL数据库失败，IP: {ip}, 用户名: {username}, 密码: {pwd}, 错误信息: {err}")

import mysql.connector
import os
import signal

# MySQL连接信息
host = 'localhost'
user = 'root'
password = 'password'

# 信号处理函数
def handler(signum, frame):
    print("查询超时，终止查询操作")
    cursor.cancel()
    result = None

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

            # 执行status命令
            cursor = cnx.cursor()
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(10)  # 设置超时时间为10秒
            cursor.execute("status")
            signal.alarm(0)  # 取消超时时间
            result = cursor.fetchone()

            if result is not None:
                print(f"status命令执行结果：{result}")
            else:
                print("查询超时，继续下一个查询")

            cnx.close()
        except mysql.connector.Error as err:
            # 连接失败，打印错误信息
            print(f"连接MySQL数据库失败，IP: {ip}, 用户名: {username}, 密码: {pwd}, 错误信息: {err}")

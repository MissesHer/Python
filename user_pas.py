#!/usr/bin/env python
# _*_ coding:utf-8 _*_
user = 'root'
passwd = '123.com'
user_to = ''
passwd_to = ''
i = 0
import getpass
import time
import os
os.system("clear")
while True:
    user_to = input("请输入你的用户名：")
    passwd_to = getpass.getpass("请输入你的密码：")
    i += 1
    if user == user_to and passwd == passwd_to:
        os.system("clear")
        print("登录%s账户成功！！" %(user))
        break
    elif i < 3:
        os.system("clear")
        print("密码输入错误%d次" %(i))
    elif i == 3:
        os.system("clear")
        print("密码输入错误已到达3次，账户已被锁定3秒。")
        time.sleep(3)
        continue


import os
import sys
import json
import hashlib
import time
import re

def time_limit(t=0):
    last_call=0
    def admin(f):
        def inner(*args,**kwargs):
            nonlocal last_call
            if status==True or f.__name__ in ("login","register"):
                if time.time()-last_call<10:
                    print("操作太频繁，请稍后重试！")
                else:
                    ret=f(*args,**kwargs)
                    last_call=time.time()
                    return ret
        return inner
    return admin

@time_limit(3)
def login():
    global status
    if status==False:
        print("欢迎来到登录页面")
        with open("管理员信息表.txt",encoding="utf-8",mode="r") as f:
            while True:
                usr=input("请输入用户名(q退出)>>> ")
                if usr.upper()=="Q":
                    break
                pwd = input("请输入密码>>> ")
                md5 = hashlib.md5()
                md5.update(pwd.encode("utf-8"))
                t = json.dumps(usr+"|"+md5.hexdigest(),ensure_ascii=False)
                f.seek(0,2)
                ret = f.tell()
                f.seek(0)  # json读数据的话，是全部读取的。。。。
                while ret:
                    k = f.readline().strip()
                    if k:
                        # t = json.loads(t)
                        # test= usr + "|" + t
                        # t2=json.loads(k)
                        if t==k:
                            status=True
                            break
                    else:
                        break
                if status:
                    print(f"登陆成功,欢迎您{usr}")
                    break
                else:
                    print("账号或密码错误，请重试！")
    else:print("您已登录！")
@time_limit()
def register():
    if status==False:
        print("欢迎来到注册页面：")
        Exist_Ststus=False
        with open("管理员信息表.txt",encoding='utf-8',mode='r+') as f:
            while True:
                usr=input("请输入用户名(q退出)>>>")
                if usr.upper() == "Q":
                    break
                pwd = input("请输入密码>>> ")
                md5 = hashlib.md5()
                md5.update(pwd.encode("utf-8"))
                f.seek(0,2)
                ret = f.tell()
                f.seek(0)
                while ret:
                    try:
                        re=json.load(f)
                        if usr==re.strip().split("|")[0]:
                            Exist_Ststus=True
                            break
                    except json.JSONDecodeError: break   #原来json格式的错误需要用这个。。。。
                if Exist_Ststus:
                    print("用户名已存在，请重试！")
                    break
                else:
                    if ret:
                        f.write("\n")
                    json.dump(usr + "|" + md5.hexdigest(), f,ensure_ascii=False)
                    print("注册成功！")
                    return
    else:print("您已登录,请退出后重试")

def staff():  #  cd  "D:\Code Files\Python\Python-Learning\Day10-99\DAY 15 函数部分总结\函数大作业"
    S=False
    while True:
        with open("员工信息表.txt",encoding='utf-8',mode="r+") as f:
            print("script name:",sys.argv[0])
            f.seek(0)
            line1=f.readline().strip().split("，")
            if sys.argv[1]:
                for i in ["select","del","set"]:
                    if sys.argv[1]==i:S=True
            if S:  # select name,age,job where name='alex'
                # select *  模糊查询
                dic={}
                if sys.argv[2] == "*": pass
                else:
                    l=sys.argv[2].split(",")
                if sys.argv[3] == "where":
                    if sys.argv[4] in line1:pass
                    elif sys.argv[4] == "*":pass
                print("看看是不是对了",l)
                break
            elif sys.argv[1]=='Q':break
            else:print("关键词错误，请重试")

def run():
    global status
    status = False
    choice = [login,register,staff]
    ch = ["登录","注册","员工信息管理"]
    while True:
        for i,j in enumerate(ch,1):
            print(i,j)
        select = input("请输入你的选择(输入q退出)>>> ")
        if select.isdecimal():
            select = int(select)
            if select in range(1,len(choice)+1):
                if select!=3 or status==True:choice[select-1]()
                else:print("请登陆后操作！")
            else:
                print("输入错误，请重新输入")
        elif select.upper()=="Q":
            status=False
            break
        else:
            print("输入错误，请重新输入")

run()

import re
from 函数大作业.函数大作业代码 import *
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
                    if sys.argv[4] in line1:
                        for j in sys.argv[4].split(","): # 先制作一个筛选条件的
                            if "=" in j:
                                [condition,value]= j.split("=")
                                for line in f:
                                    res = line.strip().split(",")
                                    if res[pos]==int(value):
                                        pass
                            if ">" in j:
                                [condition,value] = j.split(">")
                                for line in f:
                                    res = line.strip().split(",")
                                    if value.isdecimal():
                                        if int(res[pos])>int(value):
                                            pass
                            if "<" in j:
                                [condition,value]= j.split("<")
                                for line in f:
                                    res = line.strip().split(",")
                                    if value.isdecimal():
                                        if int(res[pos])<int(value):
                                            pass
                            pos=line1.index(condition)

                    elif sys.argv[4] == "*":pass
                print("看看是不是对了",l)
                break
            elif sys.argv[1]=='Q':break
            else:print("关键词错误，请重试")

l=[1,2,'3l','sdlgfhao']
print(l.index(2))
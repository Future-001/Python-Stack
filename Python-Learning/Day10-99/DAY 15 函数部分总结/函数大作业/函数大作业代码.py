import os

usr_name = input("请输入用户名>>> ")
pwd = input("请输入密码>>> ")
f = open("管理员信息表.txt",encoding="utf-8")
# info = usr_name+'|'+pwd
# ret = hashlib.md5()
# ret.update(info.encode("utf-8"))
# f.write(str(ret))
# print(ret.digest())
# f.close()
c=False
while 1:
    for i in f:
        info=usr_name+'|'+pwd
        ret = hashlib.md5()
        if str(ret.update(info.encode("utf-8"))) == i:
            c=True
    if c==True:
        print("登录成功!")
        break
    else:
        print("账号或密码错误")
def admin(f):
    def inner(*args,**kwargs):
        # if flag==False:
            ret = f(*args,**kwargs)
            return ret
    return inner

@admin
def login(flag):
    usrname = input("请输入用户名")
    u_pwd = input("请输入密码")
    count=3
    while count:
        with open("管理员信息表.txt",encoding="utf-8",mode="r") as f:
            f.seek(0)
            for i in f:
                i=i.strip().hexdigest()
                name,pwd=i.split("|")
                if name==usrname:
                    if pwd==u_pwd:
                        print("登陆成功!")
                        flag = True
                        return  flag
            if flag==False:
                count-=1
                print("账号或密码错误,请重试")
@admin
def register():pass

def run():
    choice=[login,register]
    # choice=["login","register"]
    flag = True
    while flag:
        for i,j in enumerate(choice,1):
            print(i,j)
        select=input("请输入你想进行的操作(输入q退出)>>> ")
        if select.isdecimal():
            if int(select) in (1,2):
                choice[int(select)-1](flag)
            else:
                print("输入错误，请重新输入!")
        elif select.upper()=="Q":flag=False
        else:print("输入错误，请重新输入!")
run()

# while True:
#     choice = [login,register,]
#     opt = input("请输入你要进行的操作>>>")

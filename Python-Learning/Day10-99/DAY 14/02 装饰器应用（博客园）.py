# 模拟博客园的登录
# 此时我们要利用这个装饰器完成一个需求：简单版模拟博客园登录。 此时带着学生们看一下博客园，说一下需求：
# 博客园登陆之后有几个页面，diary，comment，home，如果我要访问这几个页面，必须验证我是否已登录。
# 如果已经成功登录，那么这几个页面我都可以无阻力访问。如果没有登录，任何一个页面都不可以访问，
# 我必须先登录，登录成功之后，才可以访问这个页面。我们用成功执行函数模拟作为成功访问这个页面，现在写三个函数，写一个装饰器，实现上述功能。


# 请实现一个装饰器，每次调用函数时，将函数名以及调用此函数的时间节点写入文件中。
# 这里不写入函数名了，直接写入时间，每次登录都查询一下上次登录时间是多久，距离现在多长时间

# 可用代码：
# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
#
# def wrapper():
#     pass
# def func1(f):
#     print(f.__name__)
# func1(wrapper)
# 函数名通过： 函数名.__name__获取。


#  缺点： 没有进行优化，只是对函数做了简单的写，没有更改每次登陆的时间，，，，
import time
import os
Status=False
def auth(f):
    def inner(*args, **kwargs):
        # 这里有两种想啊法，一种就是不将登录写为装饰器函数，但是我觉得好像一般，这里我用 f.__name__=='login'就可以直接查看了
        if f.__name__ in ('login','register')  or Status :
            ret = f(*args, **kwargs)
            return ret
        else:
            print(f'请先进行登录操作！')
    return inner

@auth
def login():
    global Status,user
    print('欢迎来到登录页面 ：')
    count=3
    while 1:
        if count>0:
            user_name=input(f'请输入用户名(输入N退出登录)>>> ')
            if user_name=='N':
                return
            elif Status:
                print(f'您已登录')
                return
            else:
                passoprt=input(f'请输入密码 >>> ')
                with open('博客园.txt',encoding='utf-8') as f,\
                        open('博客园登录副本.txt',encoding='utf-8',mode='w') as f1:
                    f.seek(0)
                    for j in f:
                        k=j.strip()
                        user,pwd,last_log_time=k.split('|')
                        login_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        if user==user_name and pwd == passoprt:
                                print(f'登录成功，{user_name}，欢迎登录博客园！')
                                print(f'{user_name},你的注册时间： {last_log_time}')
                                login_information = user+'|'+pwd+'|'+login_time
                                if j[-1]!='\n':
                                    f1.write(login_information)
                                else:
                                    f1.write(login_information+'\n')
                                Status=True
                        else:
                            f1.write(j)
                if Status:
                    os.remove('博客园.txt')
                    os.rename('博客园登录副本.txt', '博客园.txt')
                    return
                count=count-1
                print('登陆失败，用户名或密码错误，请重试！')
                print(f'你还有 {count}次机会 ')
        else:
            print('错误次数过多，请稍后再试')
            return

@auth
def register():
    print('欢迎来到博客园注册界面：')
    while 1:
        user_name = input(f'请输入注册用户名>>> ')
        passport = input(f'请输入注册密码 >>> ')
        with open('博客园.txt', encoding='utf-8',mode='r+') as f,\
            open('博客园副本.txt',encoding='utf-8',mode='w') as f1:
            f.seek(0)
            for j in f:
                k = j.strip()
                user, pwd,tim = k.split('|')
                if user!=user_name:
                    existent = False
                    f1.write(j)
                else:
                    existent = True
                    print('用户已存在，请重新输入！')
                    f1.seek(0)
                    break
            if not existent:
                login_time=time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
                f.write('\n'+user_name+'|'+passport+'|'+login_time)
                print('注册成功')
                time.sleep(0.8)
                break
        os.remove('博客园.txt')
        os.rename('博客园副本.txt','博客园.txt')
        return login()
@auth
def home():
    if Status==True:
        print(f'{user},欢迎访问文章页面!')

@auth
def dairy():
    if Status == True:
        print(f'{user},欢迎访问日志页面')

@auth
def comment():
    if Status == True:
        print(f'{user},欢迎访问评论页面')

def run():
    clog=[login,register,home,dairy,comment]
    print('欢迎来到博客园主页，请选择你要进行的操作: ')
    while 1:
        choice = input(f'(1 :登录\n2注册 \n3：访问主页 \n4：访问日志 \n5：查看评论 \nq:退出）\t>>> ')
        if choice.upper()=='Q':
            return
        elif choice.isdecimal():
            choice=int(choice)
            if choice in range(1,len(clog)+1):
                clog[choice-1]()
            else:
                print("没有该选项")
        else:
            print(f'输入错误，请重新输入！')


if __name__=='__main__':
    run()
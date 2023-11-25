# 编写装饰器完成下列需求:
# 用户有两套账号密码,一套为京东账号密码，一套为淘宝账号密码分别保存在两个文件中。
# 设置四个函数，分别代表 京东首页，京东超市，淘宝首页，淘宝超市。
# 启动程序后,呈现用户的选项为:
#  1.txt,京东首页
#  2,京东超市
#  3,淘宝首页
#  4,淘宝超市
#  5,退出程序
#
# 四个函数都加上认证功能，用户可任意选择,用户选择京东超市或者京东首页,只要输入一次京东账号和密码并成功,
# 则这两个函数都可以任意访问;用户选择淘宝超市或者淘宝首页,只要输入一次淘宝账号和密码并成功,则这两个函数都可以任意访问.
#
# 相关提示：用带参数的装饰器。装饰器内部加入判断，验证不同的账户密码。
#  这里想想，带参数，那么是不是可以传递 status_jd 和 status_tb的数值呢？

def wrapper(f):
    def inner(*args,**kwargs):
        status = [status_jd,status_tb]
        if any(status):
            ret=f(*args,**kwargs)
            return ret
        else:
            print('请先进行登录操作！')
    return inner

def login():
    with open('京东.txt',encoding = 'utf-8',mode = 'r') as f,\
        open('淘宝.txt',encoding = 'utf-8',mode = 'r') as f1:
        global status_jd,status_tb
        count = 3
        print('欢迎来到登录页面：')
        while 1:
            if count>0:
                usr_name = input('请输入用户名 >>> ')
                pwd = input('请输入密码 >>> ')
                f.seek(0)
                f1.seek(0)
                for i,j in zip(f , f1):
                    i = i.strip()
                    j = j.strip()
                    print(i, j)
                    jd_name, jd_passport = i.split('|')
                    tb_name, tb_passport = j.split('|')
                    if jd_name == usr_name and jd_passport == pwd:
                        status_jd = True
                        print('欢迎登录京东账号')
                        return
                    elif tb_name == usr_name and tb_passport == pwd:
                        status_tb = True
                        print('欢迎登录淘宝账号')
                        return
                if status_jd == False and status_tb== False:
                    print('账号或密码错误，请重试！')
                count = count -1
            else:
                print('错误次数过多，请稍后再试')
                import time
                time.sleep(5)
                break
@wrapper
def jd_home():
    if status_jd:
        print('欢迎来到京东首页')
    else:
        print('请登陆京东账号后操作')
@wrapper
def jd_supermaket():
    if status_jd:
        print('欢迎来到京东超市')
    else:
        print('请登陆淘宝账号后操作')
@wrapper
def tb_home():
    if status_tb:
        print('欢迎来到淘宝首页')
    else:
        print('请登陆淘宝账号后操作')
@wrapper
def tb_supermaket():
    if status_tb:
        print('欢迎来到天猫超市')
    else:
        print('请登陆后操作')

status_jd,status_tb = False,False
def run():
    func_list = [login,jd_home,jd_supermaket,tb_home,tb_supermaket]
    print("""0,登录
1.txt,京东首页
2,京东超市
3,淘宝首页
4,淘宝超市
5,退出程序""")
    while 1:
        choice = input('请输入你的选择 >>> ')
        if choice.isdecimal() and int(choice) in range(6):
            choice = int(choice)
            if choice==5:
                return
            else:
                func_list[choice]()   # 或者我将 status 传递进去？
        else:
            print('输入非法，请重新输入！')
run()

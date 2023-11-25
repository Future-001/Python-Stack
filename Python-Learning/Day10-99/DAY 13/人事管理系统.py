# 写一个函数完成三次登陆功能：
# 用户的用户名密码从一个文件register中取出。
# register文件包含多个用户名，密码，用户名密码通过|隔开，每个人的用户名密码占用文件中一行。
# 完成三次验证，三次验证不成功则登录失败，登录失败返回False。
# 登陆成功返回True。
print()
def sign_in():
    with open(os.path.dirname(__file__)+'/register.txt',encoding='utf-8') as f:
    # with open('register.txt',encoding='utf-8') as f:
        count = 3
        while 1:
            if count>0:
                user_name = input('请输入用户名>>> ')
                passport = input('请输入密码>>> ')
                count = count - 1
                f.seek(0)
                for j in f:
                    j = j.strip()

                    user,pwd=j.split('|')
                    if user_name==user and pwd==passport:
                        print('登录成功')
                        return True
            else:
                break
            print(f'登录错误，你还有{count}次机会')

# 再写一个函数完成注册功能：
# 用户输入用户名密码注册。
# 注册时要验证（文件regsiter中）用户名是否存在，如果存在则让其重新输入用户名，如果不存在，则注册成功。
# 注册成功后，将注册成功的用户名，密码写入regsiter文件，并以 | 隔开。
# 注册成功后，返回True,否则返回False。
import os
def sign_up1(user_name,pwd):
    # with open('register.txt',encoding='utf-8',mode='r+') as f1:  稍微改一下，以便能调用函数
    with open(os.path.dirname(__file__)+'/register.txt',encoding='utf-8',mode='r+') as f1:
        while 1:
            for j in f1:
                j=j.strip()
                user,p=j.split('|')
                if user_name==user:
                    print('用户名已存在，请重试')
                    return False
            s = '\n'+user_name + '|' + pwd
            f1.write(s)
            print(f'注册成功！')
            return True

def _admin():
    while 1:
        select = input(f'请先进行管理员登录或注册：1: 登录，2: 注册 q:退出>>> ')
        if select == str(1):
            sign_in()
            break
        elif select == str(2):
            print(f'必须由已有管理员才能增加管理员，请进行登录已有管理员账户进行操作')
            sign_in()
            print('请开始创建管理员：')
            admin = input(f'请输入注册管理员用户名 >>> ')
            _pwd_ = input(f'请输入密码 >>> ')
            ret=sign_up1(admin, _pwd_)
            if ret==True:
                return True
        elif select=='q':
            return  False
        else:
            print(f'输入有误，请重试！')

"""
问题总结，之前为什么做错了呢? 首先，写注册的时候，记事本里面多了两个空行，
将空行识别为了数据，导致数据不符合了，无法拆包
其次，在写入数据时候，记住，读取到文件最后一行不会进行换行操作，所以会出现错误，在写入数据时先进行换行操作，同时写入时也要注意，末尾不能多空行
"""


# 用完成一个员工信息表的增删功能（选做题，有时间做，没时间周末做）。
#id，name，age，phone，job
# 1.txt,Alex,22,13651054608,IT
# 2,太白,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT   注意文件中间的标点符号

# 现在要让你实现两个功能：
# 第一个功能是实现给文件增加数据，用户通过输入姓名，年龄，电话，工作，
# 给原文件增加数据（增加的数据默认追加到原数据最后一行的下一行），但id要实现自增（id自增有些难度，id是不需要用户输入的但是必须按照顺序增加）。
# 第二个功能是实现给原文件删除数据，用户只需输入id，则将原文件对应的这一条数据删除
# （删除后下面的id不变，比如此时你输入1，则将第一条数据删除，但是下面所有数据的id值不变 太白，nezha的 id不变）。
import os
def staff(c):
    # with open('员工信息表.txt',encoding='utf-8',mode='r') as f,\
    #      open('员工信息更新表.txt', encoding='utf-8', mode='w') as f1:  os.path.dirname(__file__)+
    with open(os.path.dirname(__file__)+'\员工信息表.txt', encoding='utf-8', mode='r') as f, \
            open(os.path.dirname(__file__)+'\员工信息更新表.txt', encoding='utf-8', mode='w') as f1:
        if c == 1:
            while 1:
                name = input(f'请输入姓名：')
                age = input(f'请输入年龄： ')
                tele = input(f'请输入电话： ')
                work = input(f'请输入工作职业： ')
                f.seek(0)
                line1 = f.readline()
                f1.write(line1.strip())  # 为了应对原始数据为空
                if age.isdecimal() and tele.isdecimal() :
                    for j in f:
                        f1.write(j)
                        j = j.strip()
                        id, n, a, p, j = j.split(',')  # 但是注意，下面用到的 id 就要改了，如果原始数据没有 id
                    information ='\n'+str(int(id) + 1) + ',' + name + ',' + age + ',' + tele + ',' + work
                    f1.write(information)
                    print(f'增加成功！')
                    break
                else:
                    print(f'增加失败，输入的年龄或电话格式不符,请重新输入')
        if c == 2:
            for i in f:
                print(i,end='')
            delete = input("\n请输入你想删除的成员id>>> ")
            f.seek(0)
            line1=f.readline()
            f1.write(line1.strip())
            for k in f:
                j=k.strip()
                id, n, a, p, job = j.split(',')
                if id!=delete:
                    j='\n'+j
                    f1.write(j)    # 解决一个问题，删除之后，最后一行是不是又多了一空行呢？服了
                    # 还是为什么呢？(如果删除中间的行，也就是最后面还有元素的行，不会产生空行）
                    # 可能是因为倒数第二行有一个换行符，然后进行读取的时候 f1 中的行也将 f中倒数第二行的换行符读取过来了，（通常最后一行没有换行符）？
                    # 怎么解决这个空行呢？
            print('删除成功')
    os.remove('员工信息表.txt')
    os.rename('员工信息更新表.txt', '员工信息表.txt')

def personnel():
    print(f'=============================欢迎来到人事管理系统===============================')
    ret=_admin()
    while ret:
        choice=input(f"***管理员你好，请输入你想进行的操作：（1: 增加员工信息 ; 2: 删除员工信息 q:退出) >>> ")
        if choice==str(1):
            staff(int(choice))
        elif choice==str(2):
            staff(int(choice))
        elif choice=='q':
            return
        else:
            print(f'输入有误，请重试！')


if __name__=='__main__':
    personnel()

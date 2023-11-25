# 请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先输入"before"，然后再执行func函数内部代码。
# 请为func函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出"after"
def wrapper1(f):
    def inner(*args,**kwargs):
        i1=input('请输入 before: ')
        if i1=='before':
            ret=f(*args,**kwargs)
            print('after')
            print(ret)
        else:
            print('输入错误')
    return inner
@wrapper1
def func():
    return 100 + 200
func()


print()
# 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出 "after"
def wrapper2(f):
    def inner(*args,**kwargs):
        ret=f(*args,**kwargs)
        print('after')
        return ret
    return inner
@wrapper2
def func(a1):
    return a1 + "傻叉"
@wrapper2
def base(a1, a2):
    return a1 + a2 + '傻缺'
r1=base('zhangsan','lisi')
print(r1)

@wrapper2
def base(a1, a2, a3, a4):
    return a1 + a2 + a3 + a4 + '傻蛋'
print(func('zxy'))
print(base('ll','sg','234','xiaom'))

print()
# 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。
#
import random
def wrapper3(f):
    l1=[]
    def inner(*args,**kwargs):
        count=5
        while count>0:
            ret=f(*args,**kwargs)
            l1.append(ret)
            count=count-1
        return l1
    return inner
@wrapper3
def func():
    return random.randint(1, 4)
print(func())


# 请为以下函数编写一个装饰器，添加上装饰器后可以实现：执行read_userinfo函时，先检查文件路径是否存在，如果存在则执行后，
# 如果不存在则输出文件路径不存在，并且不再执行read_userinfo函数体中的内容，再讲content变量赋值给None。
import os
def wrapper4(f):
    def inner(*args,**kwargs):
        # try:
        #     exist=open(*args)
        #     exist.close()
        #     ret = f(*args, **kwargs)
        #     return ret
        # except  FileNotFoundError:
        #     print('文件路径不存在')
        #     return  None
        if os.path.exists(*args):
            ret = f(*args, **kwargs)
            return ret
        else:
            print('文件路径不存在')
            return None
    return inner
@wrapper4
def read_userinfo(path):
    file_obj = open(path, mode='r', encoding='utf-8')
    data = file_obj.read()
    file_obj.close()
    return data
content = read_userinfo('/usr/bin/xxx/xxx')
print(content)
#
# """
# 温馨提示：如何查看一个路径是否存在？
# import os
# result = os.path.exists('路径地址')
#
# # result为True，则表示路径存在。
# # result为False，则表示路径不存在。
# """



print()
# 请为以下user_list函数编写一个装饰器，校验用户是否已经登录，登录后可以访问，未登录则提示：请登录后再进行查看，然后再给用户提示：
# 系统管理平台【1.txt.查看用户列表】【2.登录】并选择序号。

# # 此变量用于标记，用户是否经登录。
# #    True,已登录。
# #    False,未登录(默认)
CURRENT_USER_STATUS = False
def wrapper5(f):
    def inner(*args,**kwargs):
        if CURRENT_USER_STATUS or f.__name__=='login':
            ret=f(*args,**kwargs)
        else:
            print('请先进行登录后查询')

        return
    return inner
@wrapper5
def user_list():
    """查看用户列表"""
    for i in range(1, 100):
        temp = "ID:%s 用户名：老男孩-%s" % (i, i,)
        print(temp)

@wrapper5
def login():
    """登录"""
    global CURRENT_USER_STATUS
    print('欢迎登录')
    while True:
        username = input('请输入用户名（输入N退出）：')
        if username == 'N':
            print('退出登录')
            CURRENT_USER_STATUS=False
            return
        elif CURRENT_USER_STATUS:
            print(f'您已登录，无需重复登陆')
            return
        else:
            password = input('请输入密码：')
            if username == 'alex' and password == '123':
                CURRENT_USER_STATUS = True
                print('登录成功')
                return
            print('用户名或密码错误，请重新登录。')

def run():
    func_list = [user_list, login]
    while True:
        print("""系统管理平台 1.txt.查看用户列表；2.登录 """)
        index = int(input('请选择：'))
        if index in range(1,len(func_list)+1) :
            func_list[index - 1]()
        else:
            print('序号不存在，请重新选择。')

run()




# 看代码写结果
#
v = [lambda: x for x in range(10)]
print(v)
print(v[0])
print(v[0]())
print(v[9]())

# 一句话函数，我被搞惨了，v 里面是地址，第二个输出的是地址，然后一旦调用，输出都是9

# 看代码写结果
#
v = [i for i in range(10, 0, -1) if i > 5]  # 这里还是地址吗？哦列表推导式 v=[10,9,8,7,6]

# 看代码写结果
data = [lambda x: x * i for i in range(10)]  # 新浪微博面试题
print(data)  # 里面全都是地址，而且不一样
print(data[0](2))   # 这里面的是 18
print(data[0](2) == data[8](2))  # 这里虽然两个内容一样，但是根据同一代码块的缓存机制。可变的数据类型，地址不太一样，但是数值一样 True
#
# 请用列表推导式实现，踢出列表中的字符串，然后再将每个数字加100，最终生成一个新的列表保存。
#
data_list = [11, 22, 33, "alex", 455, 'eirc']
new_data_list = [i+100 for i in data_list if repr(i).isdecimal()]  # 请在[]中补充代码实现。
print(new_data_list)


# 请使用字典推导式实现，将如下列表构造成指定格式字典.
data_list = [
    (1, 'alex', 19),
    (2, '老男', 84),
    (3, '老女', 73)
]
dict_data={k[1]:k[2] for k in data_list }


# # 请使用推导式将data_list构造生如下格式：
info_list = {
    1: ('alex', 19),
    2: ('老男', 84),
    3: ('老女', 73)
}
data_dict={k[0]:(k[1],k[2]) for k in data_list}



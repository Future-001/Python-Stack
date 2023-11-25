# 写函数，函数可以支持接收任意数字（位置传参）并将所有数据相加并返回。
#
# 看代码写结果
def func():
    return 1, 2, 3
val = func()
print(type(val) == tuple)   # True
print(type(val) == list)     # FALSE


# 看代码写结果

def func(*args, **kwargs):
    print(args,'\n',kwargs)

# # a. 请将执行函数，并实现让args的值为 (1.txt,2,3,4)
func(*[1,2,3,4])
# # b. 请将执行函数，并实现让args的值为 ([1.txt,2,3,4],[11,22,33])
func([1,2,3,4],[11,22,33])
# # c. 请将执行函数，并实现让args的值为 ([11,22],33) 且 kwargs的值为{'k1':'v1','k2':'v2'}
func([11,22],33,k1='v1',k2='v2')
# # d. 如执行 func(*{'武沛齐','金鑫','女神'})，请问 args和kwargs的值分别是？
func(*{'武沛齐','金鑫','女神'})      # 结果是 （吴佩琦，金鑫，女神）
# # e. 如执行 func({'武沛齐','金鑫','女神'},[11,22,33])，请问 args和kwargs的值分别是？
func({'武沛齐','金鑫','女神'},[11,22,33])   # （{'武沛齐','金鑫','女神'},[11,22,33]）
# # f. 如执行 func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})，请问 args和kwargs的值分别是？
func('武沛齐','金鑫','女神',[11,22,33],**{'k1':'栈'})  # 结果是 （'武沛齐','金鑫','女神',[11,22,33]）  {k1:'栈’}
print()

# 看代码写结果

def func(name, age=19, email='123@qq.com'):
    print(name,age,email)

# # a. 执行 func('alex') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
func('alex')                        # 可以执行，一个位置参数，其余默认参数
# # b. 执行 func('alex',20) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
func('alex', 20)                        # 位置参数，可以执行，年龄被覆盖
# # c. 执行 func('alex',20,30) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
func('alex', 20, 30)                    #  可以执行，但是数值被覆盖
# # d. 执行 func('alex',email='x@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？
func('alex', email='x@qq.com')                               # alex 19 x@qq.com
# # e. 执行 func('alex',email='x@qq.com',age=99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
func('alex',email='x@qq.com',age=99)             # alex 99 x@qq.com
# # f. 执行 func(name='alex',99) ,判断是否可执行，如可以请问 name、age、email 的值分别是？
# func(name='alex',99)                        # 不可以，位置参数一定要在关键字之前
# # g. 执行 func(name='alex',99,'111@qq.com') ,判断是否可执行，如可以请问 name、age、email 的值分别是？  不可以


# 看代码写结果
print()
def func(users, name):
    users.append(name)
    return users
result = func(['武沛齐', '李杰'], 'alex')          # 实现的功能是，位置参数，没有关键字参数。  输出了 一个列表
print(result)

print()
# 看代码写结果
def func(v1):
    return v1 * 2

def bar(arg):
    return "%s 是什么玩意？" % (arg,)

val = func('你')   #  赋值了两遍， ‘你你'
data = bar(val)     # 输出了 你你 是什么玩意？
print(data)


# 看代码写结果
def func(v1):
    return v1 * 2

def bar(arg):
    msg = "%s 是什么玩意？" % (arg,)
    print(msg)

val = func('你')
data = bar(val)      # 打印了  你你 是什么玩意？
print(data)         # None


# 看代码写结果
v1 = '武沛齐'
def func():
    print(v1)
func()  #  打印  武沛齐
v1 = '老男人'
func()    #   老男人 就近原则


# 看代码写结果
print()
v1 = '武沛齐'
def func():
    v1 = '景女神'
    def inner():
        print(v1)

    v1 = '肖大侠'
    inner()    #  萧大侠
func()
v1 = '老男人'     # 还是打印上面的结果捏。
func()        # 就近原则，一定要注意了哈

# 看代码写结果【可选】
print()
def func():
    data = 2 * 2
    return data
new_name = func  # 返回函数的 内存地址。。。。
print(new_name)
val = new_name()
print(val)        # 输出 4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。

# 看代码写结果【可选】
print()
def func():
    data = 2 * 2
    return data
data_list = [func, func, func]   # 都是内存地址啊
for item in data_list:
    v = item()
    print(v)   #   输出了三个4
#
# # 注意：函数类似于变量，func代指一块代码的内存地址。


# 看代码写结果（函数可以做参数进行传递）【可选】
print()
def func(arg):
    arg()
def show():
    print('show函数')
func(show)  # dayin  show函数
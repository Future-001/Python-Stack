"""
========================================= 昨日回顾 =========================================
匿名函数： 一句话函数 多和内置函数、列表推导式结合  lambda 参数: 返回值
内置函数：   min  max  sorted map reduce filter
闭包： 内层函数 对 外层函数 非全局变量的使用
        只存在于嵌套函数中
    优点： 确保数据安全，自由变量不会在内存消失，而且全局还引用不到
作业讲解：  28 '
=========================================  今日大纲 =========================================
装饰器：
    什么是开放封闭原则？
    我们的软件一旦上线之后（比如你的软件主要是多个函数组成的）,那么这个软件对功能的扩展应该是开放的，比如你的游戏一直在迭代更新，
    推出新的玩法，新功能。但是对于源代码的 修改 是封闭的。你就拿函数举例，如果你的游戏源代码中有一个函数是闪躲的功能，
    那么你这个函数肯定是被多个地方调用的，比如对方扔雷，对方开枪，对方用刀，你都会调用你的闪躲功能，
    那么如果你的闪躲功能源码改变了，或者调用方式改变了，当对方发起相应的动作，你在调用你的闪躲功能，就会发生问题。所以，开放封闭原则具体具体定义是这样：
    1.对扩展是开放的
        我们说，任何一个程序，不可能在设计之初就已经想好了所有的功能并且未来不做任何更新和修改。所以我们必须允许代码扩展、添加新功能。
    2.对修改是封闭的
        就像我们刚刚提到的，因为我们写的一个函数，很有可能已经交付给其他人使用了，如果这个时候我们对函数内部进行修改，
        或者修改了函数的调用方式，很有可能影响其他已经在使用该函数的用户。OK，理解了开封封闭原则之后，我们聊聊装饰器。

装饰器：
      是以功能为导向的，就是一个函数。
     被装饰的对象其实也是一个函数。

    完美定义：在不改变 原 被装饰函数 原代码 及其 调用方式的前提下，为其增加新的功能。
    装饰器 就是 一个函数！！！！！  是闭包 ！！！！！！！！
    装饰器 完全遵守 开放封闭原则

关于装饰器的嵌套。建议看看DAY 14 难题错题
如果将装饰器写在一个函数中， 相当于  test = 函数1 (参数) (test)  第二个括号里面传递的是函数名

import time
time.time()  格林威治时间

time.sleep(time)  模拟一下网络延迟


#  终极大招: 标准版的装饰器
def wrapper(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret
    return inner


装饰器的应用:
            这周的周末作业: 模拟博客园的登录, 必须要用装饰器


# 温馨提示：如何查看一个路径是否存在？
# import os
# result = os.path.exists('路径地址')

# 函数名通过： 函数名.__name__获取。


博客园作业，好好看一下

# import time
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S",struct_time)) # 当前时间节点
"""

#  初识装饰器
#
# 需求介绍：你现在xx科技有限公司的开发部分任职，领导给你一个业务需求让你完成：让你写代码测试小明同学写的函数的执行效率。

# 版本一
import time
start_time = time.time()
def diary():
    """很多代码...."""
    print('欢迎登陆博客园日记首页')
diary()
time.sleep(1)
print("小张")
end_time=time.time()
print(end_time-start_time)    # 格林威治时间

#  需求分析：你要想测试此函数的执行效率，你应该怎么做？
#  应该在此函数执行前记录一个时间， 执行完毕之后记录一个时间，
#  这个时间差就是具体此函数的执行效率。那么执行时间如何获取呢？ 可以利用time模块，有一个time.time()功能。

# 但是让你测试一下别的模块呢的是不是全得复制呢？

start_time = time.time()
def index():
    print('欢迎登陆博客园日记首页')
index()
time.sleep(1)
print('小李，这也太麻烦了，一次次复制')
end_time=time.time()
print(end_time-start_time)    # 格林威治时间


#  版本2： 版本一 重复率太高了，版本二 解决代码的重复使用问题
print()
print('版本2: 函数的调用 ')
def timer1(f):
    """很多代码...."""
    time.sleep(1)
    f()                      # 如果采用： 一个个函数调用，timer() 函数里面 每次都写原函数() ,是不是太 low 了？
start_time = time.time()
timer1(index)          # 动态传参解君愁  # 但是不满足 开放封闭原则，原函数的 调用方式被改变了
end_time=time.time()
print(f'原函数的执行效率是： {end_time-start_time}')


# 版本3：   用到了闭包  不能改变函数的调用方式   这就是 装饰器了
# 但是我觉得还是太麻烦了，
def timer3(f):
    def inner():
        start_time=time.time()
        f()
        end_time=time.time()
        print(f'原函数的执行效率是： {end_time-start_time}')
    return inner
ret = timer3(index)
ret()  # inner()  这样的话调用方式还是变了，不符合开放封闭原则 再改
# 再次修改一下：
index = timer3(index)      # 先执行 等号右边 将 index 传给 f , 全局作用域变量 index 不会影响 内部的 局部变量 f 的数值
index()  # 等价于 inner()  没有改变原函数的 调用方式。
diary = timer3(diary)
diary()


#  版本 4   对装饰器进行改进   python 提出了一个语法糖
# 每次都得  index = timer3(index)  太麻烦了，每次都得改
print()
print('版本5 ，装饰器写在最上面')
def timer4(f):
    def inner():
        start_time=time.time()
        f()
        end_time=time.time()
        print(f'原函数的执行效率是： {end_time-start_time}')
    return inner
# 在 需要加入 装饰器的函数前面，加入一个 @timer4
@timer4  # index=timer4(index)  index4 = timert4(index4)
def index4():
    print(f'我测试一下 语法糖 @timer4  ,一定要在需要执行的函数之前')
    return 666
index4()

# 还是不完美 ： 如果函数有返回值呢？？？？那不是出问题了吗？返回值都不见了啊  因为执行 @timer4 之后，
#                                   index 就是代表 inner 函数的地址了，
# 原来的函数 test（） 的返回值就不见了
ret = index4()
print(ret)
# 所以 谁是 index4 真正的执行者?  装饰器里面的 f 是他真正的执行者。 所以666返回给了 f()

# 版本5 ： 被装饰函数带返回值
def timer5(f):
    def inner():
        start_time=time.time()
        f()        # f 是 index真正的执行者，index1函数的返回值给了他 不信看一下
        r = f()   # 我们要解决的 就是将 r 返回给 inner的返回值
        end_time=time.time()
        print(f'原函数的执行效率是： {end_time-start_time}')
        return r
    return inner
@timer5   # index5 = timer5(index5)
def index5():
    print('特来一试')
    return 666
# index5('kevin')   # 这样会错，因为 index5 代表的是 inner的地址 传参无法直接传给 index5
index5()
ret = index5()
print(ret)

# 版本6  传参数的 装饰器
def timer6(f):
    def inner(*args,**kwargs):  # 此时我们的 index5 代表的是 Inner的地址,那么传递参数,肯定也要传给 inner
        #  在函数的定义时,*代表聚合
        start_time=time.time()
       # 在函数调用时: * 代表打散
        r = f(*args,**kwargs)     # 同理,接收到的参数也要传过来
        end_time=time.time()
        print(f'原函数的执行效率是： {end_time-start_time}')
        return r
    return inner
@timer6  # index6=timer(index6)
def index6(name,age):
    print(f'我叫{name},今年我 {age}岁啦 我又回来啦! 你们是打不败我的')
    return 888
index6('Kevin',18)
print(index6('sungt',23))




"""
===================================== ++++++++++++++++++++++++++++++++++================================
"""

#  终极大招: 标准版的装饰器
def wrapper(f):
    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret

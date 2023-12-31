""""
======================================== 昨日回顾 =================================================
函数是以功能为导向的，一个函数一个功能，减少重复代码，提高代码的可读性
函数的结构 def fc_name():
            函数体
函数的调用：函数名直接调用
函数的返回值：  return
                    停止函数，返回值，单个多个
函数的参数：
        盘活函数
        实参：
            位置，关键字，混合参数（位置一定在关键字之前）
        形参：
            位置，默认参数（小心覆盖的问题，一定要对应好）

==============================================  今日大纲 ===================================================
形参角度：
        万能参数:
                留有余地，方便后面改进功能。急需一种形参，能够接收所有的实参

                 形参 前面加上  *  就可以成为万能参数。 *args  否则只是一个简单的位置参数
                 将所有的位置参数，聚合成为一个 元组 ，赋值给了 args

                 **kwargs  接收所有的关键字参数，将其聚合成一个字典，关键字作为 键  数据作为 值

        仅限关键字参数：
                    只能接受关键字参数， 放在 *args 和 **kwargs中间，一定只能是 关键字参数。
                            一定要给他赋值，不然会报错。

        形参的最终顺序：
                    * args 的位置，一定放在 位置参数后面  但是一定也要注意，默认参数的覆盖问题。
                                默认参数一定要放在最后。
                    **kwargs  的位置，一定放在关键字参数后面

         *（**）的魔术用法:
                    在函数定义时，代表聚合 聚合为 元组或者字典
                    在函数调用时，代表打散。可迭代对象，都是一样的打散，无非是将参数传给了 args 还是 kwargs

名称空间角度：
                    在python解释器开始执行之后, 就会在内存中开辟一个空间, 每当遇到一个 变量 的时候,
                     就把变量名和值之间的关系记录下来, 但是当遇到 函数定义 的时候,
                     解释器只是把 函数名 读入内存,(函数名与内存地址的对应关系）
                    表示这个函数存在了, 至于函数内部的变量和逻辑, 解释器是不关心的. 也就是说一开始的时候函数只是加载进来,
                    仅此而已, 只有当函数被调用和访问的时候, 解释器才会根据函数内部声明的变量来进行开辟变量的内部空间.
                    函数中的变量只能在函数内部使用，随着函数执行完毕, 这些函数内部变量占用的空间也会随着函数执行完毕而被清空.

                    我们给这个‘存放名字与值的关系’的空间起了一个名字-------命名空间。
                    代码在运行伊始，创建的存储“变量名与值的关系”的空间叫做全局命名空间；
                    在函数的运行中开辟的临时的空间叫做局部命名空间也叫做临时名称空间。

        全局名称空间，局部:

        内置空间：
                    python源码提供的一些内置的函数。
        加载顺序，取值顺序：
                    内置名称空间 ————> 全局名称空间(变量和数值对应关系，函数和地址对应关系) ------->  局部名称空间（ 函数调用是开辟）
                    取值顺序： 就近原则   看是从哪里开始找
                                从函数开始时，从局部找时  局部 ---> 全局---> 内置
                                从全局开始时，  全局---> 内置   因为局部已经被释放了

        作用域：
                    全局作用域：  内置名称空间+全局名称空间
                    局部作用域：  局部名称空间（可以从全局作用域引用变量，但无法修改，但是全局不能引用局部变量，因为被释放了）
                    无法修改的原因： 局部空间名称的只是 局部变量，只是在函数内部起作用解释器只是价格你这个同名变量认为是新定义的局部变量

函数的嵌套（高阶函数）：

内置函数 globals() local()：
                        print(globals())     返回的是字典，全局作用域内的内容
                        print(locals())        返回的是字典，当前作用域内的内容。

关键字： nonlocal global

函数类似于变量，func代指一块代码的内存地址。  直接写函数名，就是代表他的内存地址呢
"""

#  万能参数
def eat(*args):
    print(args,type(args))
    print('我请你吃 %s %s %s %s' % args)
    # print('我请你吃 %s' % args)  #  会出错，因为传入的是一个元组，数据类型不匹配
    print('我请你吃 {}' .format(args) )
eat('烧鸡','炸鸡','红烧鸡翅','我喜欢吃')

#  写一个函数，计算你传入函数的所有数字的和(传入的多少不确定)
def sum(*args):
    s=0
    for i in args:
        s+=i
    print(s)
sum(1,2,34,5,6,7)

# 聚合所有的关键字参数聚合到一个字典中，赋给 kwargs
def func(**kwargs):
    print(kwargs)
func(name='skg',sg='sgsa',asdf='sgso')
print()

# def order(a,b,sex='m',*args,age,**kwargs):  因为如果只用关键字参数，当你使用位置参数，
#                           没有写出关键字，那么会被覆盖了，，，，尽量放在 *args后面
def order(a,b,sex='m',*args,age,c,**kwargs):
    print(sex)
    print(a,b)
    print(args)
    print(kwargs)
order(1,2,3,4,5,6,name='sga',agsw='sdgo',age=18,c=99)  # 此时，默认参数被覆盖了。同时 不给age c赋值会报错，他们只接受关键字参数
# 梳理：  位置参数一定在关键字参数之前，args 只接受位置参数，所以，sex不可能位于args接收的参数之前，那么sex参数就被覆盖，但是，如果他放在之后，
# 会导致sex得到多个参数，也会报错。
# order(1,2,4,5,6,sex='F',name='sga',agsw='sdgo',age=18,c=99)       这样也会出错，因为 sex得到了多个参数

print()
def order(a,b,*args,sex='m',age,c,**kwargs):
    print(sex)
    print(a,b)
    print(args)
    print(kwargs)
order(1,2,3,4,5,6,sex='F',name='sga',agsw='sdgo',age=18,c=99)

print()
# * 在函数调用时，相当于打散 可迭代对象
def disperse(*args,**kwargs):
    print(args)
    print(kwargs)
disperse(*[1,2,3],*'askgosgssdg')

print()
# 名称空间角度 读取顺序，取值顺序（就近原则)
print(666)   # 内置空间
def name():   # 全局空间，内存地址
    input='alex'
    print(input)       # 从局部去找，然后全局，内置
name()                   # 局部空间
print(input)   # 从全局找时， 全局 --> 内置 因为局部（临时空间—）已经被释放了


# 作用域，变量的引用
print()      # 内置空间
time =34
def f1():   # 全局空间
    count=1       #
    print(time)
    def dinner():     # 局部空间1
        print(time,count)       # 可以引用，但是无法修改
    dinner()       # 局部空间2            一定要注意，看函数是不是定义了，然后执行了
    print('函数的嵌套：')
    name()
    print(locals())        # 返回值时字典，键值对是当前作用域的所有内容
f1()          # 局部空间1


#  内置函数 globals()  locals()
# print(globals())
# print(locals())
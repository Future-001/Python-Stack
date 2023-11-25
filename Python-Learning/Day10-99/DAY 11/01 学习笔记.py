"""
========================================= 昨日回顾 =========================================
函数的参数：
            实参： 位置，关键字，混合
            形参：  位置，默认，万能参数，仅限关键字参数
            形参角度的传参顺序： 位置  *args 默认 仅限关键字参数  **kwargs
            *（**）的魔性用法： 定义时聚合，调用时打散
            三个空间：内置名称空间，全局名称空间（变量和数值的对应关系，函数名和内存地址），局部名称空间（执行函数时开辟，结束释放）
            加载顺序： 内置  ---->  全局  ----->  局部
            作用域：   局部作用域只能引用全局作用域变量，不能修改，全局作用域不能引用局部     都是地址的问题
            取值顺序：就近原则  LEGB
            函数的嵌套： 一定要注意，只有调用时，才会运行。
            内置函数：  globals()  返回的是字典，全局作用域内的全部内容， locals()   当前作用域内的全部内容。

=========================================  今日大纲 =========================================
补坑：
    默认参数的陷阱：
                只针对默认参数是可变的数据类型：  例如， 形参中的默认参数 是列表 或者 字典等
                如果默认参数是可变的数据类型，那么无论调用多少次默认参数（没有给他传值 ，看例2），其都是同一个。 （指向的内存地址都是一个）
                但是，但是， 一旦给默认参数传递了数值，那么， 指向的就不再是原来的那个内存地址了
                同时，要注意一下：
                            如果 再次使用默认参数时， 那么， 指向的是原来的操作地址。。。。。所以，输入的是所有操作过后的，地址中的数值。（例3）
                def func(name,alise=[]):
                    alist.append(name)
                    return alist
                # print('alist')      # 不在全局也不再局部。。。。。
                ret = func('namelgos')
                print(ret,  id(ret))
                ret2 = func('张三是个十六分')
                print(ret2,  id(ret2))   # id 是同一个

    局部作用域的坑：
            在函数中，如果定义了一个变量，但是在定义这个变量之前，对其进行引用了，解释器认为是语法问题。
            你因该使用之前先定义的东西，，，，
            count = 1
            def func():
                count+=1   # 局部变量没有定义这个东西啊。 而且你也没有传递过来参数
                print(count)   # 只有这行，正确，因为用了全局的变量  变量的访问顺序。局部-> 全局 > 内置
                count =2    # 错了，不知道你用的是全局还是局部
            func()

关键字： global  nonlocal
        global :
                在局部作用域声明一个全局变量，使得局部变量能够在全局被找到
                （在局部作用域内）修改一个全局变量。。

        nonlocal:
                不允许操作全局变量（在局部作用域内 定义 nonlocal 全局变量 是错的，因为不允许操作全局变量）
                主要用于：  局部作用域内部：  内层函数 对外层函数 的局部变量进行修改


函数名的应用：
        函数名指向的是函数的 内存地址
        函数名+() 就可以执行函数【 也就是说  内存地址 +（） 执行函数 】
        函数名 就是变量   那么不就可以进行  对变量进行操作  例如赋值。。。
        函数名可以作为容器型数据类型的 元素
        函数名可以作为函数的参数。。。。。。 当然传递的是 地址。。。
        函数名可以作为函数的返回值, 抓住他是地址就可以了


格式化输出：
        %s  format
        但是都不好用：新增的：
        直接加上一个  f'  {} '
        结构更简单，可以结合表达式 ，函数，字典，列表等等使用
                    msg = f '我叫{name},今年 {age}'
                    dic = {name='alex',age=18}
                    asg = f"我叫 {dic['name'],今年{dic['age']}"
                    count = 7
                    print(f"最终结果是{count**2}")
                    l = [1.txt,2,3,4,5,6]
                    name = 'barry'
                    print(f'name is {name.upper} ')

                    # 结合函数
                    def _sum(a,b):
                        return a+b
                    print(f'最终求和得到 : {_sum(10,100)}')

可迭代对象：
        iterable
        python中： 一切皆对象  一个实实在在存在的数值： 对象
        可迭代：  更新迭代  重复的 循环的过程  更新迭代每次都有新的内容
        可以进行循环更新的一个实实在在的值
        专业角度： 可迭代对象：  内部还含有 ‘__iter__' 方法的对象， 两个 _
        目前学过的可迭代对象：  str list tuple dict set range 文件句柄

        获取一个对象的所有操作方法：      dir()  就是将元素的 所有的操作方法 以列表的方式 返回回来就可以了。
                    s = 'engo'
                    print(dir(s))  ['__add__', '__class__', '__contains__', '__delattr__',
                                         '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
                                         '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
                                          '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__',
                                           '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__',
                                            '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center',
                                            'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index',
                                            'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
                                             'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower',
                                              'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind',
                                               'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
                                                'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

                    print('_iter_' in dir(s))   # 判断对象是否是可迭代对象

                    优点：
                        存储的数据能直接显示，比较直观
                        拥有的方法多，操作方便
                    缺点：
                        很占内存
                        不能直接通过 循环 进行取值，例如列表 for 循环都不是可以直接取值（索引，key)的，是先将其转化为一个迭代器了


迭代器：
        定义： 更新迭代  可以更新迭代的工具
        专业： 内部含有'__iter__' 方法，同时含有 '__next__' 方法的对象，就是迭代器
        判断：   '__iter__ '   in dir() and '__next__' in dir()

        只有 文件句柄 是迭代器， 目前所学，（str int list dic set typle...)其余只是可迭代对象
                想想文件句柄  for  和  .readlines()
        可以直接进行取值

        #  可迭代对象转化为迭代器：
            iter(iterable)  f or  .__iter__()
            next(iterator)  对迭代器进行取值   .__next__()         一定不能多，多了出错

            优点：
                    节省内存
                    惰性机制： 一个 next 只能取一个值
             迭代是数据处理的基石，扫描内存中放不下的数据集时，我们要找到一种惰性获取数据项的方式，即按需一次获取一个数据项。
             缺点：
                   速度很慢，以时间换空间，
                   不走回头路，不能往回取数据，会记住上一个的位置。 ，具体见下面的例子

                   超出了 迭代范围时候    if StopIteration 停止
                        利用while  模拟 for 进行可迭代对象
                        while 1.txt:
                            try:
                                print(next(obj))
                            except StopIteration:
                                break


可迭代对象 和 迭代器：
        可迭代对象是一个操作方法 比较多， 比较直观存储数据相对少的 数据集 （不能直接取值）
                当你侧重于对数据进行灵活处理，内存空间多
        迭代器：非常节省内存，可以记录取值位置，通过循环 + next  方式取值，但是不直观， 操作方法比较单一
                        数据量大，内存不足。。。。
"""

# 默认参数的坑： 针对可变的数据类型的默认参数
def func(name, alist=[]):
    alist.append(name)
    return alist

# print('alist')      # alist 不在全局，也不再局部，特殊的空间。。
ret = func('namelgos')
print(ret, id(ret))
ret2 = func('张三是个十六分')
print(ret2, id(ret2))  # id 是同一个

#  例2  如果给默认参数传递了数值，那么，调用的默认参数不是原来的那个了
def func(name, l=[]):
    l.append(name)
    return l
# print('alist')      # alist 不在全局，也不再局部，特殊的空间。。
ret = func(10,)
print(ret, id(ret))
ret1 = func(10,[])
print(ret1, id(ret1))   # 可以看到，默认参数传递数值后，就不是原来的那个内存地址了，指向了不同的内存地址。
ret2 = func('张三是个十六分')
print(ret2, id(ret2))  # id 是同一个

print(ret)
print(ret1)
print(ret2)     # 两个的地址是一样的，同时改变了，，，，

print()
# count = 1.txt
#  def func():
#      count+=1.txt    # 局部变量没有定义这个东西啊。 而且你也没有传递过来参数
#      print(count)
#  func(count)

count = 1
def func():
     print(count)   # 这样又是对了，因为引用了全局的变量
     # count =1.txt  这样还是错了，因为不知道你用的是局部还是全局变量，，，，
func()

print()
"""============================  global  nonlocal ==========================="""
sex = 'N'
name = 'time'
def g():
    global name             #  局部作用域里面申明全局变量
    # nonlocal sex         # 不能操作全局变量
    name= 'kexin'
    count = 1
    def f():
        nonlocal count
        count = 'timeghjs'
    print(count)
    f()
    print('count : ',count)       #  一定要注意： 只能操作局部变量， 对局部变量进行修改。
    sex = 'nan '
    print(sex)
# print(name)       # 这里错了，因为函数还没运行,没有这个全局变量  必须要先声明，后引用
g()
print(sex)
print(name)
print(globals())     # 获取全局变量

print()

l = [ func,g]
for i in l:
    print(i)

def func():
    print('666')
def func1(x):
    x()
    print(x)
    return x
ret = func1(func)
ret()

print()
g = func

g()


"""===============================  另一个格式化输出=============================="""
name = 'zhangsan'
age = 19
msg =f'我叫{name},今年 {age}'
print(msg)
dic = dict(name = 'alex', age = 18)
asg = f"我叫 {dic['name']}, 今年{dic['age']}"
count = 7
print(f"最终结果是{count**2}")
l = [1, 2, 3, 4, 5, 6]
name = 'barry'
print(f'name is {name.upper} ')

# 结合函数
def _sum(a, b):
    return a + b
print(f'最终求和得到 : {_sum(10, 100)}')

print()
s = 'engo'
print(dir(s))
print('__iter__' in dir(s))      # 两个 _

with open('文件1' , encoding='utf-8',mode = 'w') as f :
    print('__iter__' in dir(f) and '__next__' in dir(f))

    """============================= 迭代器 ================================="""
print()
l1 = [11,22,33,44,55]
s1 = l1.__iter__()
s2 = iter(l1)
print(s1,s2)
print(next(s1))
print(s2.__next__())

print()
print('不走回头路啊')
li = [11,22,33,44,55,66,77,88]      # 这是可迭代对象
obj = li.__iter__()          #  迭代器
for i in range(3):
    print(next(obj))
print('记住了上一个位置了呢：  ')
print(next(obj))



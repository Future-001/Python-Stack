"""
========================================= 昨日回顾 =========================================
生成器：  就是迭代器，不过是自己用python代码构建的
            生成器函数
            生成器表达式
            python内部提供的
如何判断是函数还是生成器函数：
        yield return   yield from  (将一个可迭代对象变为生成器)
吃包子的例子
列表推导式，生成器表达式： 循环模式 ，筛选模式
内置函数：  eval exec  harsh callable help

一点疑问的解答：
def make_average():
    li = [1.txt,2,3,4]
    def average(new_values):
        print(locals())
        return new_values

    return average
avg = make_average()
print(avg(11))
print(globals())    # 没有继续使用 li 那么这个空间中就没有了 li 这个列表
print(avg(12))   正常来说，我们知道，函数执行完毕，会释放局部名称空间，但是如果函数是嵌套函数，你返回了 嵌套的内层函数的地址。
一旦调用了外层函数，那么在函数执行完毕之后，全局名称空间中已经有了 嵌套的 内层函数的地址， 此时他已经相当于一个全局名称空间去了
对于调用的函数中的一些变量，如果继续使用，形成闭包，不继续使用，那么，函数执行完毕，会被释放空间

下面的例子也能说明：
def make_average():
    li = [1.txt,2,3,4]
    def average(new_values):
        print(locals())
        return new_values
    average(18)
    return 'nice'
print(make_average())
print(globals())   函数执行完毕，没有返回继续使用的地址等，那么 全局名称空间中就没有了 average 函数的地址。不能继续使用了。

=========================================  今日大纲 =========================================

匿名函数：   一句话函数，直接用一行构建函数。     例一
            lambda (相当于 def 关键字) 形参 : 返回值
            func = lambda a,b:a+b

内置函数： int 取整
         float
         complex(实部，虚部)
         bin 十进制转化为二进制并返回：   **
         oct   十进制转换为 八进制并返回   **
         hex   十进制变为十六进制并返回   **
         divmod(除数，被除数)  得到商与余数  (商，余数)   **
         round(小数，小数位数)    保留小数位数   **
         pow(x,y,z)   表示 x**y  % z
         bytes(virables , encoding = 'utf-8')  转换数据的编码方式  ***
         ord(element)  输入字符寻找位置      chr 输入位置寻找字符
         repr : 返回一个对象的字符串形式   %r 就输出了字符串形式
         all(iterable)  :  可迭代对象中全是真才为真
         any(iterable)  :  可迭代对象中有一个真就是为真
         print(self, *args, sep=' ', end='\n', file=None)   spe 表示分隔符，end 表示结束符
         list: 创建方式：   l = []
                          l = list()  迭代
                          列表推导式
        dict :          dic = {'one':1.txt,'two':2}
                        dic = dict(one=1.txt,two=2)
                        fromkeys
                        字典推导式
                        update
        abs:  求绝对值
        sum :  求一个可迭代对象的和       sum(iterable,start value)
        reverse:  对原来的列表进行翻转
        reversed:   对原来的列表进行翻转，返回一个  迭代器，，，，取值：  list for next
        zip :  拉链法：*****
                 l1 = [1.txt,2,3,4]
                 tu = ('ke','an','try')
                 dic = dict(one=1.txt,two =2)
                 obj = zip(l1,tu,dic)

         min()   max()   :  返回最小值或者最大值   ******************
                        min()  取绝对值最小的数值：    min(iterable , key = 'NONE')
                        如果可以加入 key : 呢么将可迭代对象的元素按照顺序传输 key 对应的 函数中
                                    获取到返回值后，在进行比较
                        way 1.txt:
                                l1 = [1.txt,2,99,33,-4,-8,-1.txt]
                                for i in l1:
                                    l2.append(abs(i))
                                print(min(l2))
                        way2:
                                abss = lambda i:abs(i)
                                print(min(l1,key = abss))


                    #  练习题
                     dic = dict(a=5,b=2,c=3)
                     求出 值最小的键值对
                     print(min(dic,key = lambda a : dic[a]))

        sorted : 排序，  sort 对列表进行排序
                    这也是  排序，但是 他有 key,  返回列表   reverse 默认从低到高排序
                    reverse = True  从高到低

        filter :  过滤 筛选， 类似于列表推导式的筛选模式。
                    返回一个迭代器：  filter(lambda x:x>3,l1)  返回的 迭代器中的结果是满足条件的 x 具体看一下下面的例子代码理解一下
                    列表推导式 返回的是一个 列表。

        map :  列表推导式的 循环模式  返回的是一个迭代器。
                    map(lambda i:i**2,range(1.txt,6)  返回的迭代器中的结果 保存的是返回值

        reduce : 已经不是内置函数了  现在是  from functools import reduce
                reduce( 函数名 , iterable)  注意，函数名每一次都需要 传入 两个参数。


闭包：  保证数据的安全！！ 只能在 嵌套函数中存在
                            给大家提个需求，然后用函数去实现：完成一个计算不断增加的系列值的平均值的需求。
                            例如：整个历史中的某个商品的平均收盘价。什么叫平局收盘价呢？就是从这个商品一出现开始，
                            每天记录当天价格，然后计算他的平均值：平均值要考虑直至目前为止所有的价格。
                            比如大众推出了一款新车：小白轿车。
                            第一天价格为：100000元，平均收盘价：100000元
                            第二天价格为：110000元，平均收盘价：（100000 + 110000）/2 元
                            第三天价格为：120000元，平均收盘价：（100000 + 110000 + 120000）/3 元
                            代码 见 例子11

        内存函数 对外层函数  非全局变量的引用，就会形成 闭包。
          被引用的非全局变量 也称作 自由变量，这个自由变量会与 内层函数 产生一个绑定关系，自由变量不会再内存中消失

如何判断一个嵌套函数 是不是 闭包：
                            # 函数名.__code__.co_freevars 查看函数的自由变量
                                            print(avg.__code__.co_freevars)  # ('series',)
                            # 函数名.__code__.co_varnames 查看函数的局部变量
                                        print(avg.__code__.co_varnames)  # ('new_value', 'total')
                            # 函数名.__closure__ 获取具体的自由变量对象，也就是cell对象。
                                         # (<cell at 0x0000020070CB7618: int object at 0x000000005CA08090>,)
                            # cell_contents 自由变量具体的值
                                         print(avg.__closure__[0].cell_contents)  # []

# 例一：  是
def wrapper():
    a = 1.txt
    def inner():
        print(a)
    return inner
ret = wrapper()

# 例二： 不是
a = 2
def wrapper():
    def inner():
        print(a)
    return inner
ret = wrapper()

# 例三： 肯定是 ，，，，，，，

def wrapper(a,b):  # 相当于对内层韩式 创建了  两个变量。
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret = wrapper(a,b)

"""

#  例一  匿名函数 一句话函数 多与内置函数结合  lambda 数据：返回值
func = lambda a,b:a+b
print(func(1,2))

# 练习题1
#  接受可以切片索引的参数，返回索引 0 和2 对应的元素
func1 = lambda *args:args[:3:2]
print(func1(*[1,2,3,4,5]))

#  接受两个 int 类型的参数，返回较大的那个数值
func2 = lambda a,b:a if a>b else b
print(func2(2,3))

print(int(3.8))
print(float(2.4))

print()
# 数制转换
print(bin(10))
print(oct(10))
print(hex(20))

# divmod(除数，被除数)
print(divmod(6,4))

print(round(3.1415926,3))

print(pow(2,3,3))

s1 = '太白'
s1 = bytes(s1,encoding='utf-8')

print(ord('中'))
print(chr(20013))

print(s1)
print(repr(s1))

s2 = '李玉刚'
print(repr(s2))
print(f'我叫 %r' %(s2))

l = [1,2,3,'sadgk','']
print(all(l))
print(any(l))

print(l,3,4,sep='&&',end=' ')

print(abs(-2))
print(sum(l[:3],10))

obj = reversed(l)
print(i for i in obj)
# for i in obj:
#     print(i)
print(list(obj))

l1 = [1, 2, 3, 4]
tu = ('ke', 'an', 'try')
dic = dict(one=1, two=2)
obj = zip(l1, tu, dic)
print(type(obj),list(obj))

l1 = [1,2,99,33,-4,-8,-1]
l2 =[]
for i in l1:
    l2.append(abs(i))
print(min(l2))

abss = lambda i:abs(i)
print(min(l1,key = abss))

dic = dict(a=5,b=2,c=3)
# 求出 值最小的键值对
print(min(dic,key = lambda a : dic[a]))

l2 =[('kevin',18),('zhangsan',44),('as',66)]
print(min(l2))
print(min(l2,key=lambda x:x[1]))
print(min(l2,key=lambda x:x[1])[0])

print()
print(sorted(l2,key=lambda i:i[1]))

print(list(filter(lambda i:pow(i,3), range(4)) ))
# 筛选器，筛选器，筛选的是满足结果的 i ，所以最后得到的就是 i  所以最后输出 1.txt 2 3
print(list(filter(lambda i: sorted(l2,key = lambda i:i[1]), l2)))

print(map(lambda i : i**3,range(1,4)))
print(list(map(lambda i : i**3,range(1,4))))

from functools import reduce
print(reduce(lambda x,y:x**2+y,[1,2,3,4,5]))


# 例子11
# 方案一
l1 =[]
def make_average(values):
    l1.append(values)
    total = sum(l1)
    return total/len(l1)
print(make_average(100))
# 万一中间不小心输入了一个 L1 会导致计算结果出错了，所以不要放在 全部变量当中。 但是放在 临时名称空间 也会出错，所以不建议呢。
#  完成计算效果，又能
# 方案2
print()
def make_average(values):
    l1 =[]  #
    # 但是每一次会清空列表
    l1.append(values)
    total = sum(l1)
    return total/len(l1)

print(make_average(100))
print(make_average(10000))

"""        内存函数 对外层函数  非全局变量的引用，就会形成 闭包。
          被引用的非全局变量 也称作 自由变量，这个自由变量会与 内层函数 产生一个绑定关系，自由变量不会在内存中消失"""

# 方案三：
print()
def make_average():
    l1 = []   # 自由变量
    def average(new_values):
        l1.append(new_values)
        total = sum(l1)
        print(l1)
        return total/len(l1)
    return average
avg = make_average()
print(avg(1000))
print(avg(1020))
print(avg(1030))
print(avg(1040))

"""如何判断一个嵌套函数 是不是 闭包：
                            # 函数名.__code__.co_freevars 查看函数的自由变量 
                                            print(avg.__code__.co_freevars)  # ('series',)
                            # 函数名.__code__.co_varnames 查看函数的局部变量
                                        print(avg.__code__.co_varnames)  # ('new_value', 'total')
                            # 函数名.__closure__ 获取具体的自由变量对象，也就是cell对象。
                                         # (<cell at 0x0000020070CB7618: int object at 0x000000005CA08090>,)
                            # cell_contents 自由变量具体的值
                                         print(avg.__closure__[0].cell_contents)  # []"""

print()
print(avg.__code__.co_freevars)
print(avg.__code__.co_varnames)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)

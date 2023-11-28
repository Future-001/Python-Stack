"""
========================================= 昨日回顾 =========================================
可迭代对象：
        可以更新迭代的实实在在的值
        内部含有 '__iter__' 方法的
        str list tuple dict set range
        优点： 操作方法多，操作灵活，直观
        缺点： 占用内存

迭代器：
        可以更新迭代的一个工具（数据结构）
        内部含有 '__iter__'  '__next__' 方法
        文件句柄
        优点： 节省内存 惰性机制
        缺点： 不直观，速度相对慢，操作方法单一，不走回头路。。。。 stopinteration

格式化输出：
函数名的应用：
默认参数的坑，作用域的坑
global  nonlocal

=========================================  今日大纲 =========================================
迭代器：
        yield
        yield  return 对比
        yield  from
        生成器表达式：列表推导式
        内置函数①


生成器：
        生成器？： python社区：生成器与迭代器看成一种，生成器的本质就是迭代器
                唯一的区别：生成器是我们自己用python代码构建的数据结构，迭代器是内置提供的，或者转化得来的

                获取生成器的三种方式：
                        生成器函数
                        生成器表达式
                        python内部提供的一些：

                    生成器函数：
                            将函数里面的 return 改为 yield 就可以了，，，这样函数不会被执行，
                                ret = func1()         # <generator object func1 at 0x00000243A7F76F90>
                                生成器 相当于迭代器， 取值用迭代器的方法，  一个 next 对应一个  yield
                                但是； 如果 next多了，那么会出现 StopIteration
                            注意： 如果有多个 yield 那么，必须使用返回值，
                                        不然多个 func1().__next__() 是从头开始得，不是从上个next开始

                            return   yield 区别：
                                return ： 结束函数，返回值
                                yield ： 只要函数中有 yield 关键字， 那么就是生成器函数，不是函数，
                                        生成器中可以有多个yield 不会结束函数。

                    生成器的作用： 节省内存啊，因为迭代器只能 用已经 有的数据转化，但是，生成器，可以用来 节省内存
                                    用多少，开辟多少。相当于一个动态的集合。。。。。 具体看看例子2 就能清楚了。


                     yield from:  相当于将 原来的 可迭代对象 变成了 迭代器， 一次取值一个元素。可以看看例 3
                                    优化了内存循环，节省了内存
                                  l1 =[ 1,23,3,4,5]
                                  yield from l1   # 此时他是迭代器呢


        列表推导式：  用一行代码构建一个比较复杂的有规律的列表 （只针对 复杂，有规律）       例子4
                    循环模式 ：   [ virable for virable in iterable]

                                l1 = [i for i in range(1,11)]
                                print(l1)

                    筛选模式：   [ virable for virable in iterable if condition]

                            # 找到嵌套列表中，名字含有两个 'e' 的人名留下来
                            l1 = [['Tom','Billy','Jefferson','Andrew','Wesley','Stevfen','Joe'],
                                  ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
                            l2 = [j for i in l1  for j in i if j.count('e')>=2]
                            print(l2)

                    缺点： 超过三层循环才能构建的，不建议使用了
                          查找错误不行啊，只有一行代码呢。

         生成器表达式：
                       例子5 生成器表达式
                    # 与列表推导式的写法基本一致      []  --->  ()   也有筛选模式和 循环模式
                    很节省内存。

        列表推导式 与 生成器的区别：   [] ()   iterable  iterator 两个区别

        字典推导式， 集合推导式 ，都是一样的。
                    l1 = ['jay', 'jj', 'meet']
                    l2 = ['周杰伦', '林俊杰', '元宝']
                    dic = {i:j for i in l1 for j in l2}  # 这样就出错了，因为两层循环，每次结束之后都到了 元宝。所以错了
                    print(dic)
                    dic = {l1[i]:l2[i] for i in range(len(l1))}
                    print(dic)

        集合推导式：  一样的

        内置函数：   函数：实现某种功能
                68 个内置函数
                ，函数就是以功能为导向，一个函数封装一个功能，那么Python将一些常用的功能（比如len）给我们封装成了一个一个的函数，
                供我们使用，他们不仅效率高（底层都是用C语言写的），而且是拿来即用，避免重复早轮子，那么这些函数就称为内置函数，
                到目前为止python给我们提供的内置函数一共是68个，由于时间关系以及考虑这些函数的不同重要性我们会挑常用的重要的内置函数去讲，

            黄色一带而过：all()  any()  bytes() callable() chr() complex()
             divmod() eval() exec() format() frozenset() globals() hash()
             help() id() input() int()  iter() locals() next()  oct()
              ord()  pow()    repr()  round()↳

            红色重点讲解：abs() enumerate() filter()  map() max()
             min() open()  range() print()  len()  list()  dict()
             str()  float() reversed()  set()  sorted()  sum()
              tuple()  type()  zip()  dir()

                蓝色未来会讲： classmethod()  delattr() getattr()
                 hasattr()  issubclass()  isinstance()  object() property()
                  setattr()  staticmethod()  super()

内置函数讲解：
            eval()  剥去字符串的外衣，运算里面的代码   s = '1+3'    print(eval(s))
                    s1 = "{ 'name':'alex'}'
                    但是，可能会带来病毒，，，，不建议使用。  黑客劫持，修改代码， 字符串包装病毒。

            exec  代码流    harsh  哈希值       callable   是否可调用    help

# 看下面代码，能否对其简化？说说你简化后的优点？
print()
def chain(*iterables):
    for it in iterables:
    #     for i in it:
    #         yield i
        yield from it
    print(iterables,type(iterables))
    # yield from iterables  # 方法错了，可迭代对象，一次一个元素，你看看你的元素是什么。
g = chain('abc',(0,1,2))
print(list(g))  # 将迭代器转化成列表

怎么让生成器 输出数值：  next ,for 循环 。 list 将其列表化
"""


#  生成器的生成方式 之  生成器函数：
# 将函数里面的 return 改为 yield 就可以了，，，这样函数不会被执行
def func1():
    print(666)
    print(888)
    yield 3
    print(f'到此为止，这是第一个')
    a=1
    d=4
    print(a,d)
    yield 5       # 一个 Yield对应一个next ，


ret = func1()         # <generator object func1 at 0x00000243A7F76F90>
print(ret)      # 生成器，相当于迭代器，取值用 next
print(next(ret))  #  如果想我之前调用 next(func1)那么每次都是从头开始的
print()
print(ret.__next__())

print()
#                                           例2 ：       生成器的作用：大量数据
# iter()  需要从已经有的数据转化，不能直接得到  生成器自动生成
def func2():
    l1 = []
    for i in range(1,101):
        l1.append(f'第{i}个包子')      # 2万一多了浪费呢？
    return l1
ret = func2()
print(ret)

def gen_func2():
    for i in range(1,101):
        yield f'第{i}个包子'
ret = gen_func2()
print(ret.__next__())

for i in range(20):
    print(next(ret))

for i in range(10):
    print(next(ret))

print()
#                                           例子3  yield from 的利用，好好看清楚
def func3():
    l1 = [1,2,3,4,5]
    yield l1
ret = func3()
print(ret.__next__())

def yield_from_func3():
    l1 = [1,2,3,4,5]
    l2 = [' 威龙','雪碧','可乐']
    yield from l1
    yield from l2
ret = yield_from_func3()

for i in range(8):
    print(next(ret))
print(type(ret))


print()
#                                               例子 4  列表推导式
def gen_list():
    l1 = []
    for i in range(1,11):
        l1.append(i)
    yield l1
ret = gen_list()
print(next(ret))

print(f'列表推导式')
l1 = [i for i in range(1,11)]
print(l1)


"""        列表推导式：  用一行代码构建一个比较复杂的有规律的列表
                    循环模式 ：   [ virable for virable in iterable]
                        l1 = [i for i in range(1.txt,11)]
                        print(l1)

                    筛选模式：   [ virable for virable in iterable if condition]
                    """
print()
# 将10 以内数的平方加入列表中
l2 = [i**2 for i in range(1,11) ]
print(l2)
# 100以内的偶数加入列表
l3 = [i for i in range(100) if i%2==0]
print(l3)
# 将python第一期 到python100期写入列表
l1 = [f'python{i}期' for i in range(1,101)]
print(l1)

# 过滤掉长度小于3的列表元素，并且将剩下的转化为大写字母
l1 =['sdfa',1452,'gas','ww',1344,{'so':12,33:'taiyang'}]  # len int 没有len属性

l2 = [str(i).upper() for i in l1 if len(str(i))>=3]
print(l2)
# 找到嵌套列表中，名字含有两个 'e' 的人名留下来
l1 = [['Tom','Billy','Jefferson','Andrew','Wesley','Stevfen','Joe'],
      ['Alice','Jill','Ana','Wendy','Jennifer','Sherry','Eva']]
l2 = [j for i in l1  for j in i if j.count('e')==2]
print(l2)


print()
#                                           例子5 生成器表达式
# 与列表推导式的写法基本一致      []  --->  ()   也有筛选模式和 循环模式
gen = (i for i in range(1,11))
print(gen,type(gen))
for i in gen:
    print(i)

print()
#                               练习题
# 构建一个列表，[1.txt,2,3,...10.'J','Q','K','A']
l = [i for i in range(2,11)] + list('JQKA')
print(l)


print()
#                               字典 推导式
l1 = ['jay', 'jj', 'meet']
l2 = ['周杰伦', '林俊杰', '元宝']
dic = {i:j for i in l1 for j in l2}  # 这样就出错了，因为两层循环，每次结束之后都到了 元宝。所以错了
print(dic)
dic = {l1[i]:l2[i] for i in range(len(l1))}
print(dic)

print()
#                           内置函数
# eval  剥去字符串外衣，进行内部运算、
s = "{'name':'alex'}"
print(eval(s),type(s),type(eval(s)))

# exec 与 eval 基本一样，代码流
msg = """
for i in range(10):
    print(i)
"""
print(exec(msg))

# hash  哈希值
print(hash('siog'))

# help (args,kwargs)
print(help(str.upper))

# callable  判断对象是否可以调用  用于判断是否是函数，能被调用
s = 'aglsgsl'
print(callable(s))
print(callable(func1))
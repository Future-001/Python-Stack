# day11作业
# 请写出下列代码的执行结果：
# 例一：
def func1():
    print('in func1' )
def func2():
    print('in func2' )
ret = func1
ret()   # 输出了 func 1.txt
ret1 = func2
ret1()     # func2
ret2 = ret
ret3 = ret2
ret2()      # func1
ret3()       # func1
# 执行结果： 记住指向的是地址就行了


# 例二：
print()
def func1():
    print("**'in func1' **")
def func2():
    print("**'in func2' **")
def func3(x, y):
    x()
    print("**'in func3' **")
    y()
print(111)
func3(func2, func1)       # in func2  in func3 in func1
print(222)

# 执行结果：

#  例三（选做题）：
print()
def func1():
    print("**'in func1' **")
def func2(x):
    print("**'in func2' **")
    return x
def func3(y):
    print("**'in func3' **")
    return y
ret = func2(func1)    # 输出了  2
ret()   # 1.txt
ret2 = func3(func2)   # 3
ret3 = ret2(func1)    # 2
ret3()   # 1.txt

# 执行结果：


# 看代码写结果：
print()
def func(arg):
    return arg.replace('苍老师', '***')
def run():
    msg = "Alex的女朋友苍老师和大家都是好朋友"
    result = func(msg)
    print(result)
run()      # 一定要注意返回值的事情
# 输出了  Alex的女朋友***和大家都是好朋友
def func(arg):
    return arg.replace('苍老师', '***')
def run():
    msg = "Alex的女朋友苍老师和大家都是好朋友"
    result = func(msg)
    print(result)
data = run()   # 考察返回值问题，   输出了 Alex的女朋友***和大家都是好朋友  但是 data = None
print(data)


# 看代码写结果：
print()
item = '老男孩'
def func():
    item = 'alex'

    def inner():
        print(item)

    for item in range(10):
        pass
    inner()   # 就近原则 9
func()

# 看代码写结果：
print()
l1 = []
def func(args):
    l1.append(args)
    return l1
print(func(1))
print(func(2))
print(func(3))

# [1.txt]
# [1.txt, 2]
# [1.txt, 2, 3]

# 看代码写结果：
print()
name = '太白'
def func():
    global name
    name = '男神'
print(name)   # 就近原则  太白
func()
print(name)   # 男神


# 看代码写结果：
print()
name = '太白'
def func():
    print(name)
func()     # 太白

# 看代码写结果：
print()
# name = '太白'
# def func():
#     print(name)
#     name = 'alex'         # 会造成歧义，不知道你要用的是哪一个
# func()


# 看代码写结果：
#
def func():
    count = 1

    def inner():
        nonlocal count
        count += 1
        print(count)

    print(count)      # 1.txt
    inner()     # 2
    print(count)  # 2
func()


# 看代码写结果：
print()
def extendList(val, list=[]):     # 默认参数是可变的数据类型
    list.append(val)
    return list

list1 = extendList(10)     # [10]
list2 = extendList(123, [])    # [123]
list3 = extendList('a')         # [10,'a']
# 默认参数使用一个地址，但是给默认参数传递数值时，使用另一个地址，不信  id

print('list1=%s' % list1)       # [10,'a']
print('list2=%s' % list2)       # [123]
print('list3=%s' % list3)        # [10,'a']


# 看代码写结果：
print()
def extendList(val, list=[]):
    list.append(val)
    return list

print('list1=%s' % extendList(10))      # [10]
print('list2=%s' % extendList(123, []))      # [123]
print('list3=%s' % extendList('a'))      # [10.'a']


# 用你的理解解释一下什么是可迭代对象，什么是迭代器。
"""可以进行更新迭代的对象，能够明显的看到数据，适合数据量小，占用内存   '__iter__'    dir   不能直接取值，转化为迭代器再取值
迭代器： 可以进行迭代的  '__iter__'   '__next__'  数据量大，不占用太大内存，空间换时间"""

# 如何判断该对象是否是可迭代对象或者迭代器？
#  '__iter__'  '__next__' in dir

print()
# 写代码：用while循环模拟for内部的循环机制（面试题）。
l = [11,22,33,44,55]  #  可迭代对象
obj = iter(l)
print(obj)
while 1:
    try:
        print(obj.__next__())
    except StopIteration:
        break


# 写函数，传入一个参数n，返回n的阶乘   例如: cal(7)     计算7654321
print()
def jc(x):
    r = 1
    for i in range(x,0,-1):
        r = r*i
    return r
print(jc(4))


# 写函数，传入n个数，返回字典  {‘max’:最大值,’min’:最小值}
print()
#           例如: min_max(2, 5, 7, 8, 4)    返回: {‘max’:8,’min’:2}(此题用到max(), min()内置函数)
def min_max(*args):
    a = max(args)
    b = min(args)
    return {'max':a,'min':b}
# 或者 return {'max':max(args),'min':min(args)}

print(min_max(1,234,45,6,7))

# 写函数，返回一个扑克牌列表，里面有52项，每一项是一个元组(选做题)
print()
# 例如：[(‘红心’，2), (‘草花’，2), …(‘黑桃’，‘A’)]

def pk():
    l1 = ['红桃','黑桃','方片','梅花']
    l2 = ['J','Q','K','A']
    l3 = [2,3,4,5,6,7,8,9,10]
    l3 =l3+l2
    l = []
    for i in l3:
        for j in l1:
            l.append((j,i))
    return l
print(pk())

# 写代码完成99乘法表.(选做题，面试题)
print()
# 1.txt * 1.txt = 1.txt
# 2 * 1.txt = 2
# 2 * 2 = 4
# 3 * 1.txt = 3
# 3 * 2 = 6
# 3 * 3 = 9
# ......
# 9 * 1.txt = 9
# 9 * 2 = 18
# 9 * 3 = 27
# 9 * 4 = 36
# 9 * 5 = 45
# 9 * 6 = 54
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81
for j in range(1,10):
    i = 1
    for i in range(1,j+1):
        print(f'{j}*{i}={i*j}')



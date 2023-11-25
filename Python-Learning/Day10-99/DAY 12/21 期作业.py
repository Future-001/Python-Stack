# 本次作业需要在周日下午6点前提交到码云的 day12文件中。

# 写出三元运算的基本格式及作用？
a = 1 if 3>2 else 3

# 看代码写结果
def func(*args, **kwargs):
    print(args, kwargs)
# a. 执行 func(12,3,*[11,22]) ，输出什么？

func(12,3,*[11,22]) # 输出为一个元组： (12,3,11,22)  {}
# b. 执行 func(('alex','武沛齐',),name='eric')
func(('alex', '武沛齐',), name='eric')    # 输出为 (('alex', '武沛齐',),)    {'name':'eric'}

# 看代码分析结果
def func(arg):
    return arg.pop(1),arg  # 返回值多个，那么返回一个元组，否则是原数据类型
result = func([11, 22, 33, 44])
print(result,type(result))   # 注意，返回值是删除的元素。。。。。。22，剩下的是([11,33,44],)

# 看代码分析结果
print()
def f1():
    print('f1')
def f2():
    print('f2')
    return f1
func = f2()
'执行后得到:  f2 然后返回了f1 的地址'
result = func()
# 执行了 f1 返回值为空
print(result)

# 看代码分析结果【面试题】
print()

def f1():
    print('f1')
    return f3()
def f2():
    print('f2')
    return f1
def f3():
    print('f3')
func = f2()
result = func()
print(result)
"""f2 f1 f3 NONE"""

# 看代码分析结果
print()
name = '景女神'
def func():
    def inner():
        print(name)
    return inner()
v = func()
print(v) # 结果： 景甜  NONE


# 看代码分析结果
#
name = '景女神'
def func():
    def inner():
        print(name)
        return "老男孩"

    return inner()
v = func()
print(v)


# 看代码分析结果
print()
name = '景女神'
def func():
    def inner():
        print(name)
        return '老男孩'
    return inner
v = func()     # 结构： 返回了一个地址给v 没有输出
result = v()   #输出了 '景女神'
print(result) # 老男孩


# 看代码分析结果
print()
def func():
    name = '武沛齐'
    def inner():
        print(name)
        return '老男孩'
    return inner

v1 = func()
v2 = func()
print(v1, v2)  # 结果是： 就返回了一个地址。。。。
print(f'但是注意一下，你看一下，局部名称空间每次分配的地址是，，，，，{v1 is v2} 一样的啊 ')


# 看代码写结果
def func(name):
    def inner():
        print(name)
        return '老男孩'

    return inner

print()
v1 = func('金老板')  # 得到了一个地址，
v2 = func('alex')     # 还是一个地址啊
print(v1, v2)   # 还是一个地址呢


# 看代码写结果

def func(name=None):
    if not name:
        name = '武沛齐'

    def inner():
        print(name)
        return '老男孩'

    return inner
print()
v1 = func()   # 这里使用默认参数，那么， name = '武沛齐'  返回了一个地址呢
v2 = func('alex') # 这里使用此时的 name = alex
print(v1, v2)

# 看代码分析结果【面试题】
print()
def func(num):
    def inner():
        print(num)
    return inner
result = []
for i in range(10):
    f = func(i)
    result.append(f)   # result 里面都是存储的地址。都是执行 inner 函数，但是，但是他们的 Inner地址不一样

print(i)
print(result)
v1 = result[0]()
# 输出为： 0  ============== 注意了，原来他会保存原本函数的 num============
v2 = result[9]()  # 输出为 ： 9
print(v1, v2)   # none none


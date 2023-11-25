# 写函数，接收n个数字，求这些参数数字的和。（动态传参）
def sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum(19,1,234,65,7))

# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
#
a = 10   # 全局名称空间
b = 20
def test5(a, b):      # 局部名称空间
    print(a, b)         # 内置空间
c = test5(b, a)      #打印出来的数字时 20，10
print(c)  # 结果是 空，，，，，，

# 读代码，回答：代码中, 打印出来的值a, b, c分别是什么？为什么？
# a = 10
# b = 20
def test5(a, b):
    a = 3
    b = 5
    print(a, b)
c = test5(b, a)    # 打印出来的结果是 3 5 就近原则
print(c)     # 返回值还是空

# 传入函数中多个列表和字典, 如何将每个列表的每个元素依次添加到函数的动态参数args里面？如何将每个字典的所有键值对依次添加到kwargs里面？
l1 = [1,2,3,4,5]        #  一定忘记了 * **的魔性用法，聚合以及拆散时是什么了。
l2 = [11,22,33,44,55]
dic = dict(name='zhagnsan ',age=18,sex =' F')
dic2 = dict(name='lisi ',age=22,sex ='M')
dic3 = dict(time='lisi ',a=22,s ='M')
def use(*args,**kwargs):
    print(args)
    print(kwargs)
# use(*l1,*l2,**dic,**dic2)  # 为什么错了，因为两个字典里面都有name,重复了，冲突了
use(*l1,*l2,**dic,**dic3)


# 写函数, 接收两个数字参数, 将较小的数字返回.

# 写函数, 接收一个参数(此参数类型必须是可迭代对象), 将可迭代对象的每个元素以’_’相连接, 形成新的字符串, 并返回.
# 例如 传入的可迭代对象为[1.txt, '老男孩', '武sir']  返回的结果为’1_老男孩_武sir’
def forget(*args,**kwargs):
    result = ''
    print(kwargs)
    for i in args or kwargs.items():
        if type(i) == str:
            result += i + '_'
        else:
            result+=str(i)+'_'
    return result.strip('_')
print(forget(*[1,2,'name','kevin']))
#  一定不要忘记了 * 的魔性用法啊，*  **用于接受位置参数，关键字参数，用于打散功能。。。。
print(forget(**{'name':'taiy','age':88,'sex':'Male'}))


# 19.
print()
# 有如下函数:
def wrapper():
    def inner():
        print(666)
    inner()
    inner()
wrapper()
# 你可以任意添加代码, 执行inner函数.

# 20.  相关面试题：
# 写出下列代码结果：
print()
def foo(a, b, *args, c, sex=None, **kwargs):         # 位置参数一定要在关键字参数之前。。。。一定记住。。
    print(a, b)
    print(c)
    print(sex)
    print(args)
    print(kwargs)

foo(1,2,3,4,c=6)         #  1.txt,2,6 None （3,4）               1.txt 2 （3，4） 6 None
# foo(1.txt,2,sex='男',name='alex',hobby='old_woman')      # 关键字参数一定不能少来着，特殊位置的关键字参数，，，，，
# foo(1.txt,2,3,4,name='alex',sex='男')  # 1.txt ,2 (3,4) c 还是没有接收到参数，，，，还是错的。。。
foo(1,2,c=18)      # 输出的结果是  1.txt 2 18  None （）{}
foo(2, 3, [1, 2, 3],c=13,hobby='喝茶')  # 2 ,3 13 None ([1.txt,2,3],)  {hobby：喝茶}
foo(*[1, 2, 3, 4],**{'name':'太白','c':12,'sex':'女'})   # 1.txt,2  12 '女'  (3,4)  {‘name':'太白“}
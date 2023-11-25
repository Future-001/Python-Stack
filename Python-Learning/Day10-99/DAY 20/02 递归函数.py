"""
divmode(除数，被除数) 返回元组。
=================================================递归=================================================
但是没做理解，你好好看一下。
注意的一些问题：
    少用 remove  insert
    少用 global nonlocal

recursionError 递归错误

            最大递归深度： 1000层（官网）
    998的说法怎么来的呢？
        count = 0
        def func():
            global count
            count+=1
            print(count)      出错之前输出  997/998  实际上 count 是从 0 开始加的，那么实际上就是 998/999
            func()
            print(456)
        func()         再加上这一次调的一次，那么递归的深度就是 999/1000

为什么设置递归深度： 为了节省内存空间，不让用户无限地使用内存（函数没执行完，不释放内存）
只在python中有限制，前端是没有限制的。

递归：
    1 要尽量控制次数，如果需要很多层传递才能解决问题，那么不适合用递归解决
    2. 递归和循环的关系：
            递归不是万能的
            递归比循环更占用内存。因为没结束不释放内存。
    sys.setrecursionlimit(n) 设置递归的内存。

递归函数必须要停下来：
        利用条件判断，结束函数。
        递归的关键：
                函数的调用
                函数的参数
                函数的返回值

传递参数的递归：
def func(count):
    count + = 1
    print(count)
    if count==5: return 5
    func(count)
print('--->',func(1))
并不是函数中有return ，返回值就一定能在调用函数的外层接收到。
----> 为什么返回值为空呢，需要关注每一个函数的返回值，到底返回给谁了，他的返回值是从哪里来的。。。返回值从那里来了。
一定要在程序里面 每一次都要将上一次的结果return。才能传递出去。

递归的关键是什么：
        一定要找到  f(n)  f(n-1)  f(n-2)  f(n-3) 的关系，找到你要得到的什么东西
        就是 结束时函数的关系，结束的表达式。

        最最重要的两点：  结束条件，结束的表达式。

"""
import sys
# sys.setrecursionlimit(66)
# count = 0
# def func():
#     global count
#     count+=1
#     print(count)
#     func()
#     print(456)
# while 1:
#     try:
#         func()
#     except RecursionError:
#         break


# =========================== 练习题 ================================================
# 循环
# 递归     两种方法都是一下：

#  1 计算阶乘
def func1(n):
    if n==1: return n
    else:
        return n*func1(n-1)
num = int(input('请输入一个正整数：'))
print('阶乘的结果是： ',func1(num))

# for 形式
result = 1
for i in range(1,num+1):
    result = result*i
print(result)


#  2. os 模块，查看一个文件夹下的所有文件，还有这个文件夹下面的文件夹。不能用 walk条件下
import os
i = 1
def func2(path):
    global i
    dir_list = os.listdir(path)
    for j in dir_list:
        file_path = os.path.join(path,j)
        if os.path.isfile(file_path):
            print(file_path)
        elif os.path.isdir(file_path):
            func2(file_path)

            # 当时做错了的原因，，： 一直想着return。但是这里不需要return。
        # else:return os.listdir(file_path)

path = input('请输入文件路径： ')
func2(path)

#  3. os 模块，计算一个文件夹下所有文件的大小，这个文件夹下面还有文件夹，不能用walk

# 这样的代码其实有一点问题： 为什么外面一定要有 size  呢？ 你还给他放外面了？
size = 0
def func3(path):
    global size   # 尽量不用 global ，可能有一定问题。不行。可能修改了全局变量。
    dir_list = os.listdir(path)
    for file in dir_list:
        abs_path = os.path.join(path,file)
        if os.path.isfile(abs_path):
            print(abs_path,os.path.getsize(abs_path))
            size= size + os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            return func3(abs_path)
func3("D:\Code Files\Python\Python-Learning\Class-code\DAY 19")
print(size)


def func3_2(path):
    size = 0
    dir_list = os.listdir(path)
    for file in dir_list:
        abs_path = os.path.join(path,file)
        if os.path.isfile(abs_path):
            size+=os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            ret = func3_2(abs_path)
            size+=ret
    return size

ret = func3_2(("D:\Code Files\Python\Python-Learning\Class-code\DAY 20"))
print(ret)

#  4 . 计算斐波那契数列      1 1 2 3 5 8 .。。。试一下，找第100个数，试一试效率
count = 2
l1 = [1,1]
while count<15:
    l1.append(l1[-1]+l1[-2])        # a,b = b,a+b
    count+=1
print(l1)

# 方法三：
def fb(n):
    a,b=1,1
    while n>2:
        a,b = b,a+b
        n-=1
    return b

# 方法四  同样是递归，为什么这个这么快呢？
def fb1(n,a=1,b=1):
    if n==1 or n ==2: return b
    else:
        a,b=b,a+b
        return fb1(n-1,a,b)


# 为什么这么慢呢？ 因为两段代码中： 这一段代码涉及到了重复的不断递归。  f(10)=f(9)+f(8)   下面的两个数又得不断地计算。。。。。
import time
start_time = time.time()
def func4(n):
    if n==1 or n==2:return 1
    else:
        return func4(n-1)+func4(n-2)
print(func4(10)) # 递归的太慢了，直接减少一点。
end_time = time.time()
print(f'执行时间{start_time-end_time}')


# 第五种方法：
def scq_fb(n):
    if n==1:
        yield 1
    else:
        yield from(1,1)
        a,b=1,1
        while n>2:
            a,b=b,a+b
            yield b
            n-=1
for i in scq_fb(5):
    print(i)

#  5. 三级菜单。 可能是 n 级 不确定下面有多少级。
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
def menu_func(menu):
    flag = True
    while flag:
        for i in menu:
            print(i)
        key = input('请输入：')
        if menu.get(key):
            # for j in menu[key]:
            #     print(j)
            dic = menu[key]
            flag = menu_func(dic)
        elif key.upper() == 'B':
            return True
        elif key == 'Q':
            return False  # 中间返回了 NONE 相当于 False
        else:
            print('输入错误，请重试。')
menu_func(menu)


def menu_func(menu):
    while True:
        for i in menu:
            print(i)
        key = input('请输入：')
        if menu.get(key):
            # for j in menu[key]:
            #     print(j)
            dic = menu[key]
            flag = menu_func(dic)
            if not flag:return
        elif key.upper() == 'B':return True
        elif key == 'Q':return False  # 中间返回了 NONE 相当于 False
        else: print('输入错误，请重试。')
menu_func(menu)




# 给l1 = [1.txt,1.txt,2,2,3,3,6,6,5,5,2,2] 去重，不能使用set集合（面试题）。
l1 = ["1.txt","1.txt",2,2,3,3,6,6,5,5,2,2]
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)

# 第二种
print(list(set(l1)))


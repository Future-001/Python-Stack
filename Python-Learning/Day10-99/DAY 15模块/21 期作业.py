# sys.path.append("/root/mods") 的作用？
#  就是将 /root/mods 添加到路径当中


# 字符串如何进行反转？
# reversed?

# 不用中间变量交换a和b的值。
# a = 1
# b = 2
#a,b=b,a

# *args和 ** kwargs这俩参数是什么意思？我们为什么要用它。
# 用于接受位置参数   用于接受关键字参数  可以用于功能的扩展



# 看代码写结果：
my_dict = {'a': 0, 'b': 1}
print(id(my_dict))
f = 1
print(f'f的id是 {id(f)}')
l1 = [1,2,3,4]
def func(d,n,ll):
    d['a'] = 1
    print(id(d))
    n=11
    ll.append(666)
    print(f'n 的 id 是 {id(n)}')
    return d,n
func(my_dict,f,l1)  # 看看这里，返回值变了吗？?? 为什么变了呢？ 这里传递的是地址，，，，
print(f)
my_dict['c'] = 2
print(l1)
print(my_dict)   # 只是在其中添加了一个 d=2


# 什么是lambda表达式
# 一句话函数，

# range和xrang有什么不同？
#
# "1.txt,2,3"
# 如何变成['1.txt', '2', '3',]
#
# ['1.txt', '2', '3']   分割，split
print("1.txt,2,3".split(','))
# 如何变成[1.txt, 2, 3]

#
# def f(a, b=[]) 这种写法有什么陷阱
#  默认参数是可变的数据类型，那么传递的时候，不指定的话，这个默认的参数的地址是同一个，不会被释放。

# 如何生成列表[1, 4, 9, 16, 25, 36, 49, 64, 81, 100] ，尽量用一行实现。
print([pow(i,2) for i in range(1,11)])

# python一行print出1~100偶数的列表, (列表推导式, filter均可)
print([i for i in range(1,101) if i%2==0])
print(list(filter(lambda x:x%2==0 , range(1,101))))

# 把下面函数改成lambda表达式形式
# def func():
#     result = []
#     for i in range(10):
#         if i % 3 == 0:
#             result.append(i)
#     return result
#
print(list(filter(lambda i:i%3==0 ,range(1,10))))

# 如何用Python删除一个文件？
# os.remove()
# 如何对一个文件进行重命名？
# os.rename()
# python如何生成随机数？
#  import random
""" random.random()   random.randint()  random.uniform()  random.sample()  random.shuffle()"""

# 从0 - 99这100个数中随机取出10个数，要求不能重复，可以自己设计数据结构。
import random
print(random.sample(range(0,100),10))  # for 10 每次检查是不是已经在列表中了？  或者 set 将相同的合并了，在其取

# 用Python实现9 * 9乘法表 （两种方式）
#   两个for 我之前写过
#  方式二： 尝试一些列表推导式：
t=iter([f'{i}*{j}={i*j}' for i in range(1,10) for j in range(1,i+1) ])

for j in range(10):
    for i in range(j+1):
        try:
            print(next(t),end=' ')
        except StopIteration:
            break
    print()

# 请给出下面代码片段的输出并阐述涉及的python相关机制。
#
def dict_updater(k, v, dic={}):
    dic[k] = v    # 记住默认参数的坑就好了
    print(dic)

dict_updater('one', 1)
dict_updater('two', 2)
dict_updater('three', 3, {})

# 写一个装饰器出来。
# 用装饰器给一个方法增加打印的功能。
# as 请写出log实现(主要功能时打印函数名)
import time
def log(f):
        def inner(*args,**kwargs):
            print(f.__name__)
            ret=f(*args,**kwargs)
            return ret
        return inner
@log
def now():
    ti = time.strftime('%Y-%m-%d  %H:%M:%S' , time.localtime())
    print(ti)
now()
# now()
# # 输出
# # call now()
# # 2013-12-25


# 向指定地址发送请求，将获取到的值写入到文件中。
# import requests  # 需要先安装requests模块：pip install requests
#
# response = requests.get('https://www.luffycity.com/api/v1/course_sub/category/list/')
# print(response.text)
#
# # 获取结构中的所有name字段，使用逗号链接起来，并写入到 catelog.txt 文件中。
# """
# [
#     {'id': 1, 'name': 'Python', 'hide': False, 'category': 1},
#     {'id': 2, 'name': 'Linux运维', 'hide': False, 'category': 4},
#     {'id': 4, 'name': 'Python进阶', 'hide': False, 'category': 1},
#     {'id': 7, 'name': '开发工具', 'hide': False, 'category': 1},
#     {'id': 9, 'name': 'Go语言', 'hide': False, 'category': 1},
#     {'id': 10, 'name': '机器学习', 'hide': False, 'category': 3},
#     {'id': 11, 'name': '技术生涯', 'hide': False, 'category': 1}
# ]
# 就是不断地 遍历这个列表，然后将其取出来，写入文件，如果存在相同名称，不写入就可以了
# """

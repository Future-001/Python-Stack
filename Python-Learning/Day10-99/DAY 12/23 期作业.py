# 整理今天笔记，课上代码最少敲3遍。
# 用列表推导式做下列小题
# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
"""
l1 = [i.upper() for i in l1 if len(i)>=3]
"""

# 求(x,y)其中x是0-5之间的偶数，y是0-5之间的奇数组成的元祖列表

l1 = [tuple(i for i in range(0,6,2)),tuple(j for j in range(6) if j%2!=0)]
print(l1,type(l1[0]))

# 求M中3,6,9组成的列表M = [[1.txt,2,3],[4,5,6],[7,8,9]]

M = [[1,2,3],[4,5,6],[7,8,9]]
# 方法一： 列表推导式
l1 = [j for i in M for j in i if j%3==0]
print(l1)
print([[i-2,i-1,i] for i in range(3,10,3)])

# 方法二 普通列表
l1 = []
l2 = []
for i in range(1,10):
    if i%3 == 0:
        l2.append(i)
        l1.append(l2)
        l2 = []
    else:
        l2.append(i)
print(l1)

# 求出50以内能被3整除的数的平方，并放入到一个列表中。
l2 = [i**2 for i in range(50) if i%3==0]
print(l2)

# 构建一个列表：['python1期', 'python2期', 'python3期', 'python4期', 'python6期', 'python7期', 'python8期', 'python9期', 'python10期']
l3 = [f'python{i}期' for i in range(1,11) if i!=5]
print(l3)

# 构建一个列表：[(0, 1.txt), (1.txt, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
li = []
for i in range(6):
    li.append((i,i+1))
print(li)
l = [(i,i+1) for i in range(6)]
print(l)

# 构建一个列表：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

l = [i for i in range(20) if i%2==0]

# 有一个列表l1 = ['alex', 'WuSir', '老男孩', '太白']将其构造成这种列表['alex0', 'WuSir1', '老男孩2', '太白3']
l1 = ['alex', 'WuSir', '老男孩', '太白']
l1 = [l1[i]+str(i) for i in range(len(l1))]
print(l1)

print()
# 有以下数据类型：
x = {'name':'alex',
     'Values':[{'timestamp':1517991992.94,'values':100,},
               {'timestamp': 1517992000.94,'values': 200,},
            {'timestamp': 1517992014.94,'values': 300,},
            {'timestamp': 1517992744.94,'values': 350},
            {'timestamp': 1517992800.94,'values': 280}],}
# 将上面的数据通过列表推导式转换成下面的类型：[[1517991992.94, 100], [1517992000.94, 200],
# [1517992014.94, 300], [1517992744.94, 350], [1517992800.94, 280]]
l2 = [[x['Values'][i]['timestamp'],x['Values'][i]['values']] for i in range(len(x['Values']))]
print(l2)

# 用列表完成笛卡尔积
print()
# 什么是笛卡尔积？ 笛卡尔积就是一个列表，列表里面的元素是由输入的可迭代类型的元素对构成的元组，
# 因此笛卡尔积列表的长度等于输入变量的长度的乘积。
#  a. 构建一个列表，列表里面是三种不同尺寸的T恤衫，每个尺寸都有两个颜色（列表里面的元素为元组类型)。
print()
colors = ['black', 'white']
sizes = ['S', 'M', 'L']   # 按照笛卡尔积，它的长度是 2*3 = 6
l1 = [(i,color) for i in sizes for color in colors]
print(l1)

# b. 构建一个列表,列表里面的元素是扑克牌除去大小王以后，所有的牌类（列表里面的元素为元组类型）。
# l1 = [('A','spades'),('A','diamonds'), ('A','clubs'), ('A','hearts')......('K','spades'),('K','diamonds'), ('K','clubs'), ('K','hearts') ]
l1 =['黑桃','红桃','方块','梅花']
l2 = [str(i) for i in range(2,11)] +list('JQKA')
L = [(i,j ) for i in l2 for j in l1]
print(L)

# 简述一下yield 与yield from的区别。
"""yield 是生成器函数，可以相当于迭代器，运行后不会停止，通过 next取值
yield from 是将 原来的可迭代对象 iterable 转化为了 迭代器，节省了内存。"""


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
"""
l1 =[]
while 1:
    try:
        l1.append(next(g))
    except StopIteration:
        break
print(l1)
"""

# 看代码求结果（面试题）：
print()
v = [i % 2 for i in range(10)]
print(v)   # 0 1.txt 0 1.txt 0 1.txt 0 1.txt 0 1.txt

v = (i % 2 for i in range(10))
print(v) # 这是一个生成器推导式。。。。还有筛选模式呢

for i in range(5):
    print(i)
print(i)      # 4


# 看代码求结果：（面试题）
""" 好好看一看 """
print()
def demo():
    for i in range(4):
        yield i
g = demo()       # 这是一个 生成器： 可以将其转化为列表。

g1=(i for i in g)      # 生成器推导式这里都是生成器， 通过循环生成器可以对其进行取值操作。。。。。。。
g2=(i for i in g1)

print(g1)

print(list(g1))        # 生成器转化为列表，那么里面的元素可视化
print(list(g2))        # 为什么为空 ：



# 看代码求结果：（面试题）
print()
def add(n,i):
    return n+i

def test():
    for i in range(4):
        yield i
g=test() # 是一个生成器 （函数）
for n in [1,10]:
    g=(add(n,i) for i in g) # 这也是一个生成器呢，

print(list(g))


# 通过代码实现如下转换
print()
# bin otc hex
# 二进制转换成十进制：v = '0b1111011'
v = '0b1111011'
print(int(v,0))
# 十进制转换成二进制：v = 18
print(bin(18))
# 八进制转换成十进制：v = '011'
v = '0o11'
print(int(v,0))
# 十进制转换成八进制：v = 30
print(oct(30))
# 十六进制转换成十进制：v = '0x12'
v = '0x12'
print(int(v,0))
# 十进制转换成十六进制：v = 87
print(hex(87))







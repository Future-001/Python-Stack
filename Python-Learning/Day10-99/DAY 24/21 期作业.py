# 1.计算文件夹的大小
# 基础：文件夹中只有文件
# 进阶：文件夹中还有文件夹，且文件夹的层数不确定
import os
import random

size = 0
for path,dirname,filename in os.walk('D:\Code Files\Python\Python-Learning\Class-code\DAY 25'):
    for file in filename:
        size+= os.path.getsize(os.path.join(path,file))
print(size)
# 另一种就是采取递归的方法，之前已经做过了

# 2.拼手气发红包
"""常用模块：  random
此模块提供了和随机数获取相关的方法：
        random.random() 获取【0.0,1.0) 范围内的浮点数
        random.randint(a,b)   获取 【a,b】 中间的一个整数
        random.uniform(a,b)  获取 【a,b) 内的浮点数 b,可以取到也可以取不到，不一定的
        random.shuffle(x):  混洗 也就是将x 打乱，一定是可变的数据类型。
        random.sample(x,k)   从 x 中随机抽取 k 个数据以列表返回"""
# 注意每个人抢到的钱数的概率都是均等的
# 注意抢到的金额精确到分  有一些问题，有的人可能没抢到钱。得改，还有就是精确到分不能这么写。下面是一个 gpt的回答
def money(amount,count):   # 可以递归调用？
    l = []
    if count>1 :
        get = float('%.2f' % (random.uniform(0, amount)))
        # print(count,get)
        l.append(get)
        money(amount - get,count-1)
    elif count==1:
        get = '%0.2f' %(amount)
        # print(count,'%0.2f' %(get))
        return l.append(get)
money(10.00,5)

"""import random

def divide_red_packet(total_amount, total_people):
    result = []
    amount = total_amount * 100  # 将金额转换为分
    for i in range(1, total_people):
        max_amount = amount - (total_people - i)
        money = random.randint(1, max_amount)
        amount -= money
        result.append(money / 100.0)  # 将金额转换回元，并保留两位小数
    result.append(amount / 100.0)  # 最后一个人抢到剩下的钱
    random.shuffle(result)  # 打乱顺序，确保每个人的概率均等
    return result

total_amount = 10  # 发放的总金额（元）
total_people = 5  # 总共有几个人抢红包

red_packet = divide_red_packet(total_amount, total_people)
print("每个人抢到的金额：", red_packet)"""

# 3.校验两个文件的一致性
# 要求：大文件校验   分段，分别校验

# 4.根据代码研究super和mro的关系
# super只对新式类有作用，对旧式类，必须  self(子类名,属性) 起作用  按照mro 的顺序寻找父类。

class A:
    def func(self):
        print('in a')

class B(A):
    def func(self):
        print('in b')
        super().func()
class C(A):
    def func(self):
        print('in c')
        super().func()
class D(B,C):
    def func(self):
        print('in d')
        super().func()

d = D()
d.func()  # d b  c a

# 6.整理模块和面向对象的所有内容
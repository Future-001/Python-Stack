"""
=========================================  今日大纲 =========================================
多态是什么意思呢？
在java当中：
就是数据类型。int str都是类，然后写的时候一般不写数据类型（例如C里面就给写数据类型）
多态，看一看01 中的例子，如果拟采用 pay(Applepay obj,int money)
那么Wechatpay又得换
如果你想让两个类型的对象都可以传，那么，必须让这个类型继承自同一个父类，在指定类型的时候，使用父类来指定。

鸭子类型：只要展现了 __xxx__ 的方法，就是 鸭子类型。
在python中： 只要类的内部实现了 __xxx__ 的，函数就不用指定类型了，例如之前的 Payment 这个规范。
在Java（C)中：   必须得指定数据类型，就是如果是面向对象的，那么肯定含有  数据类型，一定要指定数据类型。这种的就是鸭子类型了。
                在面向对象的编程中：在一个类中 含有了 __xxx__ 的方法，其余的类 都继承了 这个类，那么，他们就是鸭子模型。

鸭子类型：
        我们说一个对象是某某类，通常有两种方法:
                1. 通过继承从而说明是某某类
                2. 不通过继承，判定是不是某某类，反而一般来说通过他们都拥有某种方法从而说明他们是某某类的
                    只要这个类满足了某些类型的特征，我们就说他长得像这个类，就是这个类的鸭子类型。
                例如：  都拥有  __iter__  说明他们是可迭代的， __enter__
                       主要是看他们长得像，什么算长得像呢？ 内部都拥有  __xx__ 这种方法。

"""
# 举例
l = [] # 实际上时实例化了一个对象

class list(object):
    def __init__(self,*args):
        self.l1 = [1,2,3]
        self.length = len(args)
    def append(self,num):
        self.l1.append(num)
        self.length+=1
    def __len__(self):
        return self.length    # 得到长度就是通过这种方法实现的。

l1 =[1,2,3]    # 在实例化的时候，我已经获取到了你的长度了，不是通过len才循环计算了。
l1.append(4)
def len(obj):
    obj.__len__()
#  所有实现了 __len__ 方法的类，在调用 len 函数的时候，我们都说 obj 这个对象是鸭子类型。
#  迭代器：   含有 __iter__   , __next__ 是迭代器 ，（看起来像）
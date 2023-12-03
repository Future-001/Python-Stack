"""
一些内置的魔术方法：
    __new__:*****
            实例化： 先创建一个空间，指针指向类  ---->   __new__
            先调用  __new__   在调用 __init__   只能调用父类的 __new__
            <<设计模式>>    :
                    单例模式：一个类 从头到尾，只会创建一次self的空间,
            什么时候执行： 实例化的时候。之开辟一段空间，以后就不会变了。
            为什么要有： 初始化之前开辟空间时候
            单例模式：
    __call__： 对象() 调用这个类中  __call__ 方法。
    __len__ ： 利用 __len__ 方法，直接返回长度，在外面在定义一个 len 函数，之后调用相应的 __len__方法
    __eg__
    __str__  与  __repr__   :
                要去打印一个对象的时候，调用 __str__。只能返回一个  str 数据类型的数据。
                 在 %s 拼接；str()类的时候调用的也是__str__ 方法
                repr作为str 方法的备胎  ，打印是调用不到 str 那么就用 repr 代替
                ，除非利用占位符  %r 或者 repr()   调用 repr  但是没有，什么都不打印。

    __del__
    __enter__
    __exit__
    .......

     ==  会自动调用类中的 __eq__ 方法
     __gt__   __lt__  比较大小自动调用了。

"""
class A:
    def __new__(cls,*args,**kwagrs):
        o = super().__new__(cls)
        f = object.__new__(cls)
        print('执行 new',o,f)
        return o
    def __init__(self):
        print("执行 init',",self)
A()

class Baby:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,cloth,pants):
        self.cloth = cloth
        self.pants = pants
b1 = Baby('白衬衫','嗨皮库')
b2 = Baby("绿毛衣",'蓝裤子')
print(b1.cloth,b2.cloth)

class B:
    def __call__(self):
        print('hello wusir')
    def __len__(self):
        return 'Error'
def len1(obj):
    return obj.__len__()
B()()

class Course:
    def __init__(self,name,price,period):
        self.name = name
        self.price = price
        self.period = period
    def __str__(self):
        return ','.join([self.name,str(self.price),self.period])
py22 = ['PYHON22',19800,'5month']
linux = ['linux',9800,'2  month']
mysql = ['mysql',800,'3  month']
lst = [py22,linux,mysql]
for c in lst:
    print(c)



#    ==  会自动调用类中的 __eq__ 方法
class B:
    def __eq__(self,other):     # 两个对象作比较的时候，自动调用
        print('开始执行 ')
        print(self)
        print(other)
        return "执行结束， 看看结果"
b1 = B()
b2 = B()
print(b1==b2)
"""
========================================= 昨日回顾 =========================================
面向对象：
        类  对象/ 实例 实例化
        类 是具有相同属性和相似功能的一类事物
                一个模子\大的范围\抽象
                你可以知道它有哪些属性，但是不知道具体值
        对象==实例：
                给类中的属性赋予相应的值。只有一个类，但是可以有多个对象都是这个类的对象。
        实例化： 实例=类名()
                首先开辟空间，然后调用 init 方法，将地址传递给 self
                init 方法中一般暗藏： 把属性的值存储在 self空间里，--对象的初始化
        方法： 定义在类里面的函数，带有 self 函数
            实例变量   self.xxx

=========================================  今日大纲 =========================================
类型：  int float str bool dict  tuple list set-- 类（内置的数据类型)
       函数也是一个  类， 迭代器，生成器也是类   类的方法。好好想一想
变量名 = xx 数据类型
python 当中，一切皆对象，这里能理解了吧。 实例化的对象的类型就是 类。

类的成员和命名空间：
            查看类的命名空间   对象.__dict__  显示其中所有的东西的地址。
            类的加载顺序：从上到下， 先将类的方法或静态属性先进行存储后，再将类名指向这一块地址。
            实例化对象的时候，在对象中存储了一个类指针，存储和类相关的东西，
            寻址顺序： 先从自己的命名空间去找，找不到再去类的名称空间里去找。

类中的变量 是静态变量
对象的中的变量 只属于对象本身 每个对象有属于自己的空间来存储对象的变量
当使用对象去调用某一个属性的时候，会优先在自己的空间中寻找，找不到再去类中寻找
如果自己没有，就引用类的，如果类也没有，就报错
对于类来说，类中的变量所有的对象都是可以读取的，并且读取的是同一分变量。

如果一个变量，是所有的对像共享的值，那么这个变量应该被定义为静态变量
所有和静态变量相关的静态变量，都应该使用类名来处理
而不应该使用对象名直接修改静态变量

组合：
    一个类的对象是另一个对象的属性。
    对象变成了一个属性，就是将对象作为一个参数，传递到一个别的对象中作为属性，就能调用该对象的属性。


"""
class A:
    Country = '中国'
    Time = 1001
    def __init__(self,name,age,Country,Time):       # 绑定方法，存储在类的命名空间里
        self.name = name
        self.age = age
        self.Country = Country  # 优先找自己空间里面的东西。
    def f1(self):
        print(self)

    def f2(self):pass
    def f3(self):pass
    Country = '印度'
print(A.__dict__)
# a = A()
# print(a)
# print(A)

# A.f1()    # 这样会报错，因为需要一个形参 self
# a.f3()  #  ==A.f3(a)  相当于从类中调用相应函数，并且将对象名传进去作为 self
print(A.Country,A.f1)  # 但是调用  A.f1()  会出错 少传递了参数
print(A.f2(1))
# print(a.f2())

a=A('alex',83,'伦敦',1002)
print(a.Time)
print(A.Time)




#
# 学生类：
#         姓名 性别 年龄 学号 班级 手机号
# 班级信息：
#         班级名字
#         开版时间
#         当前讲师
class Student:
    def __init__(self,name,sex,age,num,classes,phone):
        self.name=name
        self.sex=sex
        self.age=age
        self.num=num
        self.classes=classes
        self.phone=phone
class Clas:
    def __init__(self,cname,begin,teacher):
        self.cname = cname
        self.begin = begin
        self.teacher = teacher
py22 = Clas('python22期','2023-11-1','自学')
大壮=Student('大壮','male',18,26,py22,123456789)
print(大壮.classes.begin)

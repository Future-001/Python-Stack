# 简述面向对象三大特性并用代码表示。
# 继承 多态 封装
print('==================封装==============')
class Student:      # 封装的三个理由： 不让外界调用，不让改，只能用我给的方式改  ，注意封装的原理，子类不能继承父类。。。
    def __init__(self,name,pwd):
        self.__pwd = pwd
        self.name = name
    def __get_pwd(self,new_pwd):
        self.__pwd = new_pwd
        return self.__pwd
    def change_pwd(self,pwd):
        self.__get_pwd(pwd)
        print(self.__pwd)
A = Student('张三',119)
A.change_pwd(123)

print('=================继承==================')  # 新式类，经典类，广度优先 深度优先 C3算法
class Course(Student):
    def __init__(self,name,classes,course,pwd):
        Student.__init__(self,name,pwd)  # 原来的方法里有什么参数就要传递什么参数。
        self.classes = classes
        self.course = course

print('==================多态========================') # python 中的多态 Java中的多态。 就是一个子类的数据类型，其实也是父类的
# 区分的话，主要在Java中，python中不太需要指定

# 什么是鸭子模型？
# 从继承讲起，一个对象是xxx类，可以通过继承，
# 另一种方法是通过 类中都是实现了 __xxx__ 方法，就是他们都是 某类型的鸭子模型。


# 列举面向对象中的类成员和对象成员。
#  类指针（如果有父类，） 方法名地址。静态变量

# @classmethod和 @ staticmethod的区别
#  @classmethod 主要是将对象绑定的方法转变为类方法，  @staticmethod  主要是将 外面的方法移动到类中，不需要self参数。
#
# Python中双下滑 __有什么作用？  私有变量
#
print()
# 看代码写结果
class Base:
    x = 1
obj = Base()
print(obj.x)  # 输出就是 1
obj.y = 123
print(obj.y)  # 123
obj.x = 123
print(obj.x)  # 123
print(Base.x)   # 静态变量，1


print()
# 看代码写结果
class Parent:
    x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x)  #  1  1  1
Child2.x = 2
print(Parent.x, Child1.x, Child2.x)   # 1  1   2
Child1.x = 3
print(Parent.x, Child1.x, Child2.x)   #   1  3  2


print()
# 看代码写结果
class Foo(object):
    n1 = '武沛齐'
    n2 = '金老板'
    def __init__(self):
        self.n1 = '女神'
obj = Foo()
print(obj.n1)  #  这里的结果是 女神
print(obj.n2)   #  金老板


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
#
class Foo(object):
    n1 = '武沛齐'
    def __init__(self, name):
        self.n2 = name
obj = Foo('太白')
print(obj.n1)   #  武沛齐
print(obj.n2)    #  太白

print(Foo.n1)   # 这里是 武沛齐
# print(Foo.n2)    # 错误，没有这个属性


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
class Foo(object):
    a1 = 1
    __a2 = 2
    def __init__(self, num):
        self.num = num
        self.__salary = 1000
    def show_data(self):
        print(self.num + self.a1)
obj = Foo(666)

print(obj.num)     # 666
print(obj.a1)   # 1
# print(obj.__salary)    # 调用不到，私有变量
# print(obj.__a2)    # 同样调用不到
print(Foo.a1)    # 1
# print(Foo.__a2)    # 还是调用不到


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
#
class Foo(object):
    a1 = 1
    def __init__(self, num):
        self.num = num
    def show_data(self):
        print(self.num + self.a1)

obj1 = Foo(666)
obj2 = Foo(999)
print(obj1.num)  # 666
print(obj1.a1)   #  1

obj1.num = 18
obj1.a1 = 99

print(obj1.num)   # 18
print(obj1.a1)     # 99

print(obj2.a1)   # 1
print(obj2.num)   # 999
print(Foo.a1)     # 1
print(obj1.a1)    # 99


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
class Foo(object):
    def f1(self):
        print('f1')
    @staticmethod   # 用于定义静态方法， 可以通过类或实例化对象进行调用。不需要传递 self or  cls  但是但是： 不能访问类的属性。
    def f2():
        print('f2')
obj = Foo()
obj.f1()
obj.f2()

# Foo.f1()   # 这里会报错，因为 f1 是一个实例方法。
Foo.f1(obj)
Foo.f2()


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
class Foo(object):
    def f1(self):
        print('f1')
    @classmethod
    def f2(cls):
        print('f2')
obj = Foo()
obj.f1()
obj.f2()

# Foo.f1()   这里会报错，因为这是实例方法。必须要传递一个实例化对象：
Foo.f1(obj)
Foo.f2()


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
class Foo(object):
    def f1(self):
        print('f1')
        self.f2()
        self.f3()
    @classmethod
    def f2(cls):
        print('f2')
    @staticmethod
    def f3():
        print('f3')
obj = Foo()
obj.f1()    # 输出肯定是  f1 f2 f3  因为在类中调用，但是如果在类中加一个 f4 就会出错 必须要一个实例化对象
# 判断错误，加上 f4 不出错，为什么？ 开辟空间？还是实例化变量的空间？所以不需要？ 验证后，好像是的
"""# class Fa:
#     def f1(self):
#         self.f2()
#         self.f3()
#         self.f4()
#         print('in f1')
#     @classmethod
#     def f2(cls):
#         print('in f2')
#     @staticmethod
#     def f3():
#         print('in f3')
# Foo.f1()   # 确实，这里调用就直接出错了。所以不行"""


print()
# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
# class Base(object):  # 都不是子类，肯定找不到了
class Base:
    @classmethod
    def f2(cls):
        print('f2')
    @staticmethod
    def f3():
        print('f3')
class Foo(Base):
    def f1(self):
        print('f1')
        self.f2()
        self.f3()
obj = Foo()
obj.f1()  # 先输出  f1 f2 f3

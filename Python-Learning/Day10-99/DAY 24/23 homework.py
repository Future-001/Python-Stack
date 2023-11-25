# 看代码写结果【如果有错误，则标注错误即可，并且假设程序报错可以继续执行】
class Foo(object):
    a1 = 1
    def __init__(self, num):
        self.num = num
    def show_data(self):
        print(self.num + self.a1)
obj1 = Foo(666)
obj2 = Foo(999)
print(obj1.num)  # 输出是 666
print(obj1.a1)   # 1

obj1.num = 18
obj1.a1 = 99

print(obj1.num)   # 18 99
print(obj1.a1)

print(obj2.a1)   # 这里的数值是 1
print(obj2.num)  # 999

print(Foo.a1)  # 1 99
print(obj1.a1)

print()
# 看代码写结果，注意返回值。
#
class Foo(object):
    def f1(self):
        return 999
    def f2(self):
        v = self.f1()
        print('f2')
        return v
    def f3(self):
        print('f3')
        return self.f2()
    def run(self):
        result = self.f3()
        print(result)
obj = Foo()
v1 = obj.run()  # 输出是  f3 （得到一个返回值999，但是暂时不输出） f2 （同时返回了一个999） 最后输出了一个999
print(v1)  # 这里的输出，应该是空，没有返回值了


# print()
# 看代码写结果
# class Foo(object):
#     def __init__(self, num):
#         self.num = num
# v1 = [Foo for i in range(10)]  # 列表推导式 里面存了10个地址，都是Foo，
# v2 = [Foo(5) for i in range(10)]  # 里面存了很多个地址，可以查看具体的内容，内容肯定是  num=5
# v3 = [Foo(i) for i in range(10)]   # 还是地址，地址里面的内容是 0-9 刚开始为什么想错了，
# 实例化，相当于开辟一段空间，所以不同的i ，开辟的空间肯定是不一样的。 并不是和 生成器表达式一样的。

# print(v1)
# print(v2)
# print(v3)
# for i in v2:
#     print(i.num,end='  ')
# for j in v3:
#     print('  |'+str(j.num),end = ' ')
#
# print()
# 看代码写结果
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#     def changelist(self, request):
#         print(self.num, request,end='   ')
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     print(item.num,end = '      ' )
# print()
# config_obj_list = [StarkConfig(1), StarkConfig(2), StarkConfig(3)]
# for item in config_obj_list:
#     item.changelist(666)


# print()
# 看代码写结果：
# class Department(object):
#     def __init__(self, title):
#         self.title = title
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)  # 这是组合，只是相当于传递了一个参数进去而已。
# p2 = Person('alex', 18, d1)
# p3 = Person('安安', 19, d2)
#
# print(p1.name)  # 输出是  '武沛齐'
# print(p2.age)   # 18
# print(p3.depart)    #  这里应该是一个地址来着
# print(p3.depart.title)   # 销售部


# print()
# # 看代码写结果：
# class Department(object):
#     def __init__(self, title):
#         self.title = title
# class Person(object):
#     def __init__(self, name, age, depart):
#         self.name = name
#         self.age = age
#         self.depart = depart
#     def message(self):
#         msg = "我是%s,年龄%s,属于%s" % (self.name, self.age, self.depart.title)
#         print(msg)
# d1 = Department('人事部')
# d2 = Department('销售部')
#
# p1 = Person('武沛齐', 18, d1)
# p2 = Person('alex', 18, d1)
# p1.message()   # 我是武沛齐,年龄18,属于人事部
# p2.message()   # 我是alex,年龄18,属于人事部

print()
# 看代码写结果： # 这是继承
class A:
    def f1(self):
        print('in A f1')
class B(A):
    def f1(self):
        print('in B f1')
class C(A):
    def f1(self):
        print('in C f1')
class D(B, C):
    def f1(self):
        super(B, self).f1()  # 这里涉及到了 super方法，一般来说，只存在于新式类，python2中必须加入 （子类名，self)参数
        print('in D f1')
obj = D()  # 继承顺序： 新式类：广度优先：D B C A
obj.f1()   # 这里输出的执行顺寻   in B f1 -->  in D f1
# 错了，为什么错了，注意这里：  我们super里面的是子类，正常来说是 D，但是这里我们传递了B作为子类。同时，我们的寻址顺序中，下一个是C所以锁了
print(D.mro())


print()
# 看代码写结果：
class A:
    def f1(self):
        print('in A f1')
class B(A):
    def f1(self):
        super().f1()
        print('in B f1')
class C(A):
    def f1(self):
        print('in C f1')
class D(B, C):
    def f1(self):
        super().f1()
        print('in D f1')
obj = D()
obj.f1()  # 这里答案很明显了  C B D


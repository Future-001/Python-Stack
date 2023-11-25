# 简答题：

# 面向对象为什么要有继承？继承的好处是什么？
# 面向对象中super的作用。

# 代码题(通过具体代码完成下列要求)：
class A:
    def func(self):
        super().func()
        print('in A')
class B:
    def func(self):
        print('in B')
class C(A,B):
    def func(self):
        # self.func()  # 不能用这个，因为你有这个方法，会一直在你这个类中找
        super().func()
        print('in C')
# 可以改动上上面代码，完成下列需求：对C类实例化一个对象产生一个c1，然后c1.func()
c1 = C()
c1.func()
#1. 让其执行C类中的func
#2. 让其执行A类中的func
#3. 让其执行B类中的func
#4. 让其既执行C类中的func，又执行A类中的func
#5. 让让其既执行C类中的func，又执行B类中的func
#

print()
# 下面代码执行结果是什么？为什么？
class Parent:
    def func(self):
        print('in Parent func')
    def __init__(self):
        self.func()
class Son(Parent):
    def func(self):
        print('in Son func')
son1 = Son()    # in son func
class A:
    name = []
p1 = A()
p2 = A()
p1.name.append(1)
# p1.name，p2.name，A.name 分别是什么？  都是1
print(p1.name,p2.name,A.name)
p1.age = 12
# # p1.age，p2.age，A.age 分别又是什么？为什么？   只有 p1有age  别的都没有这个属性


print()
# 写出下列代码执行结果：
class Base1:
    def f1(self):
        print("**'base1.f1'**")
    def f2(self):
        print("**'base1.f2'**")
    def f3(self):
        print("**'base1.f3'**")
        self.f1()
class Base2:
    def f1(self):
        print("**'base2.f1'**")
class Foo(Base1, Base2):
    def f0(self):
        print("**'foo.f0'**")
        self.f3()
obj = Foo()
obj.f0()   # foo.f0   base1.f3   base1.f1



# 有如下类：
# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(A):
#     pass
# class E(B,C):
#     pass
# class F(C,D):
#     pass
# class G(D):
#     pass
# class H(E,F):
#     pass
# class I(F,G):
#     pass
# class K(H,I):
#     pass
# 如果这是经典类，请写出他的继承顺序。     深度优先，先找到最终的父类
#
# 如果这是新式类，请写出他的继承顺序，并写出具体过程。   广度优先，C3算法
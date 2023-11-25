# 实现一个类，能自动统计这个类实例化了多少个对象。
class A:
    count = 0
    def __init__(self):
        A.count+= 1 # 尽量使用类名，直接操作，不要创建对象属性。
A.AAA=123
a=A()
B=A()
c=A()
print(A.count)


# 读程序，标出程序的执行过程，画出内存视图，并说明答案和为什么
class B:
    Country = ['中国']
    def __init__(self, name, age,Country):  # 绑定方法，存储在类的命名空间里
        self.name = name
        self.age = age
    def f1(self):
        print(self)
a=B('alex',83,'印度')
a.Country[0]='泰国' # 肯定改成了  泰国
print(a.Country) # 泰国
print(B.Country)   # 泰国  原来的列表里面的东西都被改了，肯定改了 如果是可哈西数据类型呢？
b=B('wusir',23,'日本')
b.Country='RIB'
print(B.Country)       # 类中不可变的数据类型，无法通过 对象调用该静态变量 修改 类中的元素


class B:
    Country = ['中国']
    def __init__(self, name, age,Country):  # 绑定方法，存储在类的命名空间里
        self.name = name
        self.age = age
    def f1(self):
        return self.Country
a=B('alex',83,'印度')
b=B('wusir',23,'日本')
print(a.Country)
# print(a.Country())

# 班级类
#     包含一个属性--课程
# 课程
#     课程名称
#     周期
#     价格

class Clas:
    def __init__(self,name): # ,course  要不要先设立参数，
        self.name=name
        # self.course=course
class Course:
    def __init__(self,name,time,price):
        self.name=name
        self.time=time
        self.price=price
course = Course('操作系统1',106,19999)
linux57=Clas('python22') # ,course
linux57.course=course
print(linux57.course.price)
#  后一个参数可以 写出来   linux57.course=course ，就可以少传递一个了？
#  就是增加了一个属性，这样的话，就不用每次都在里面写一个属性。
print(linux57.course.name)



# 作业，第二大题 通过圆形类实现一个圆环类，要求接收参数，外圆半径和内圆面积
# 完成方法： 计算圆环面积和圆环周长  借助组合

from math import pi
from math import sqrt
class Re_Circle:
    def __init__(self,w_r,i_area):
        self.w_r=w_r
        self.i_area=i_area
        self.i_r=sqrt(i_area/(pi))
class Re_circle_area:
    def __init__(self,Circle):
        self.Circle=Circle
        self.area=pi*Circle.w_r**2-Circle.i_area
class Length:
    def __init__(self,Circle):
        self.len= 2*pi*Circle.w_r+2*pi*Circle.i_r
环1=Re_Circle(5,4*pi)
a = Re_circle_area(环1)
长度=Length(环1)
print(长度.len)

print(a.area)
# Length.Re_Circle=Re_Circle()
# Re_circle_area.Re_Circle=Re_Circle()



# 好像找到了另一种方法来着：   理解错了
class 圆:
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*self.r**2
    def len(self):    # 所得到的都是函数，函数都是要执行的，不可能说调用了就调用了，
        # 你的self 只是调用了圆本来的属性，没有说直接有了这个新的属性。
        self.length=2*pi*self.r
        return 2*pi*self.r
内圆=圆(5)
print('内圆的周长',内圆.len())

class Ring:
    def __init__(self,outer,inner):
        outer,inner=(outer,inner) if outer>inner else (inner,outer)
        self.out_r=圆(outer)
        self.in_r=圆(inner)
    def area(self):
        return self.out_r.area()-self.in_r.area()
    def len(self):
        return self.out_r.len()+self.in_r.len()
a=Ring(8,10)
print(a.len())
# 传递的半径的大小先后问题
# 为什么要用组合？  能用方法，为什么要用组合呢？
                #  程序里的需求，不同需求之间有公用的东西。 同时，万一有复用的代码，只需要修改一个地方就可以了。

# 不用这种方法的话，一个个的实例化，然后再次创建。


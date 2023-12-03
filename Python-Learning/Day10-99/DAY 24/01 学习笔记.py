"""
========================================= 昨日回顾 =========================================
命名空间：
        在类的命名空间里：静态变量，绑定方法
        在对象的命名空间里： 类指针，对象的属性（实例变量）

        静态变量调用的习惯
            类名.静态变量
            对象.静态变量（利用对象调用静态变量的时候，不能对静态变量进行赋值操作，  对象.静态变量 这样会改变对象空间里面的静态变量的值)

        绑定方法的调用习惯：
            对象.绑定方法()   <===>  类名.绑定方法(对象)

        实例变量的调用：
            对象.实例变量：
            类不能调用实例变量

组合：
        一个类的对象是另一个类对象的属性
        两个类值键，xx有xx的关系，： 例如：班级，学生，  课程，
=========================================  今日大纲 =========================================
三大特性： 封装 继承 多态
继承：
        解决代码的重复，降低冗余度。
    继承语法：  class 类(父类)
    class B(A):  A 是父类、基类 、超类，  B子类 派生类
                子类可以使用父类中的静态变量，方法。
        开辟空间的顺序：
                    定义类的时候： 开辟一块class 的空间  self 指向这块空间
                                空间里有一个类指针----> 如果有继承关系，指向相应的父类
                                注意，是定义类的时候就已经指向了相应的父类。
                    注意： 实例化对象开辟空间，类指针指向原本的类，
                          实例化的对象调用init ，先在自己空间里面找，没找到，到类中去找，还没找到，最后去父类中找。
                          当子类和父类的方法重名了，优先用自己空间找。自己没有，用父类的，
                          自己有，父类有，同时还想用父类的，那么用下面的方法：

        有时候，子类想要调用父类的同名方法的时候，还想调用自己的方法：
            利用          父类名.方法名(self)   self参数一定要传

    代码的执行顺序： 先类 开辟空间， init 方法，self 执行该空间 执行完成该方法，
    单继承：            class A:pass
                      class B(A):pass
                      class C(B):pass
            只强调父子关系，只要有一个 父类 就是单继承，不管有几个子类，只有一个父类就可以
    多继承：  有一些语言不支持多继承
            python可以在面向对象中支持多继承
            class A:pass
            class B:pass
            class C(A,B):pass      从左到右，依次去找，顺序都是从左到右的。

补充：
        object 类： 类祖宗
                    python3中所有的类都默认的继承object类，例如 __init__
                                            class A:pass   a=A()不会报错
        通用性代码： class A(object):

        .__bases__ 查看父类有哪些。  只显示上一层的所有的父类。不会显示在上层的类。
        绑定方法和普通的函数：  类名.  调用是函数     对象.  调用是方法
                from types import FunctionType,MethodType
                FunctionType: 函数
                MethodType: 方法
        isinstance type:判断数据类型
                isinstance(a,str)   ==? type(a) is int
                那么区别呢？  isinstance(a,Cat)  能判断这个类和父类有没有继承关系。type不能，type只能判断本类。

                类名.函数名()  --->  是一个函数   ===     isinstance(a,FunctionType)   就可以判断是函数还是方法。
                对象.函数名  ---->   方法。


        自定义的类都是 type 类型的。（99.9%）
        __base__ 查看上一级父类  __bases__  所有父类    对象.__属性__ == 对象.属性
        __module__  看定义在那个函数（模块）里面
        __doc__ 查看函数、类中的注释。

pickle 的牛逼之处。dump 进去之后，load 出来直接就是   对象
                直接就可以用   obj=pickle.load(f)   obj.__dict__
封装
多态
进阶
"""

# 重复代码过多了，需要适当简化
"""
class Cat:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name}正在 eating')
    def drink(self):
        print(f'{self.name}正在 drinking')
    def climb_tree(self):
        print(f'{self.name} is climbing')
class Dog:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f'{self.name}正在 eating')
    def drink(self):
        print(f'{self.name}正在 drinking')
    def 舔(self):
        print(f'{self.name} is 舔')
小白=Cat('小白')
里斯=Dog('里斯')
小白.drink()
"""

# 继承
class Animal:   # 注意，此时里面的类指针由于没有父类，指向了自己
    def __init__(self,name,food):
        self.name=name
        self.food=food
        self.blood=99
        self.wise=99
    def eat(self):
        print(f'{self.name}正在 eating')
    def drink(self):
        print(f'{self.name}正在 drinking')
# 子类（派生类） 可以调用父类（基类）的方法。
class Cat(Animal):  # 里面的类指针已经已经（没实例化之前）已经指向了父类
    def eat(self):
        self.blood+=100
        Animal.eat(self)  # 还想用父类的，一定要用父类名.方法(self)  一定要手动传参。
        self.drink
    def climb_tree(self):
        print(f'{self.name} is climbing')
class Dog(Animal):
    def eat(self):
        self.wise+=200
        Animal.eat(self)
    def 舔(self):
        print(f'{self.name} is 舔')
小白=Cat('小白','猫粮')  # 实例化后，类指针指向了 cat类，cat类指向父类。
里斯=Dog('里斯','狗粮')
小白.drink()
小白.climb_tree()
小白.eat()
里斯.eat()
print(小白.__dict__)
print(里斯.__dict__)


import time
class Foo:
    def __init__(self):
        print('hello')
        self.func()
    def func(self):
        print('in foo')
class Son(Foo):
    def func(self):
        print('in son')
Son()   # 为什么执行了呢？ 看一下执行顺序。
# son ()  实例化对象，产生类指针，指向自己的地址，--->  去找 init --> 先执行 init 里面的内容。

# 狗个性化属性： 型号
# 猫： 猫的眼睛的颜色
class Cat_eye(Animal):
    def __init__(self,name,food,eye_color):
        Animal.__init__(self,name,food)   #需要传递的参数，注意一下  调用了弗雷德初始化，去完成通用属性的初始化
        self.eye_color=eye_color   # 派生属性

class Dog_kind(Animal):
    def __init__(self,name,food,kind):
        Animal.__init__(self,name,food)
        self.kind=kind


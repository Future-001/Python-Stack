"""内置函数补充：
property：
        @property
            将一个方法伪装成一个属性，这样就可以调用这个方法的时候不需要加  () 就可以使用了。
            不需要使用   对象.方法() 进行调用了  对象.方法名  就可以了
        但是，注意一点： 装饰的这个方法不能有参数

        进阶：  同名方法名.setter
               创建同名方法：   修改里面的东西
            删除property 的方法： 使用装饰器    方法名.deleter   在内部在进行删除

 这两个方法在 DAY 27中讲了
@classmethod 装饰器：
    用于定义类方法，类方法的第一个参数通常命名为 cls，表示对类本身的引用。
       关键在于：  可以通过类或类的实例来调用。
    类方法可以访问类的属性，并且可以在没有实例的情况下被调用。   需要对他们传递一个实例化的对象才能访问类的其他方法
    适合在方法中需要与类本身相关联的逻辑，例如工厂方法等。

@staticmethod 装饰器：
    用于定义静态方法，静态方法不需要表示自身对象的 self 或类对象的 cls 参数。
    如果要调用实例化方法，那么，可以通过  类名.方法名(实例化对象) 才能调用。
        关键在于：  可以通过类或类的实例来调用。
    静态方法不能访问类的属性，因为它们与类的实例或类本身无关。 需要对他们传递一个实例化的对象才能访问类的其他方法
    适合在方法中不需要访问实例或类属性的情况下使用，例如一些纯粹的辅助函数。
反射"""
import time
class  Person:
    def __init__(self,name,birth):
        self.name = name
        self.birth = 1998
    @property
    def age(self):
        return time.localtime().tm_year - self.birth
太白 = Person('太白',2023)
print(太白.age)

# property 的第二个应用场景： 和私有的属性合用

class  User:
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = 1900
    @property
    def pwd(self):
        return self.__pwd
太白2 = User('太白',2023)
print(太白2.pwd)

# 第三个应用场景
class Goods:
    discount = 0.8
    def __init__(self,name,origin_price):
        self.name = name
        self.__price = origin_price
    @property
    def price(self):
        return self.__price*self.discount
    # 进阶
    @price.setter
    def price(self,new_value):
        print('调用成功')
        if isinstance(new_value,int):
            self.__price = new_value
    @price.deleter
    def price(self):
        print('调用成功')
        del self.__price
apple = Goods('苹果',5)
print(apple.price)   # 调用的是 property装饰的 price
# 如果没加上 price.setter  那么，price 是一个方法，只是伪装成为了一个属性，所以还是有错误的。
apple.price = 10    # 调用的是 setter 装饰的 price
print(apple.price)
# 直接del 不能删除 price
del apple.price  # 调用的是  @price.deleter   一定要注意一下


# classmethod  与 staticmethod
class MyClass:
    country = 'china'
    @classmethod
    def class_method(cls):
        cls.name = 'aaaaa'
        print("This is a class method")
    def hhh(self):
        print('hhhh')
    @staticmethod
    def static_method():
        print("This is a static method")
    def aaa(self):
        print('aaa')

# 通过类调用
MyClass.class_method()  # 输出：This is a class method
MyClass.static_method()  # 输出：This is a static method
print(MyClass.country)

# 通过类的实例调用
my_instance = MyClass()
my_instance.class_method()  # 输出：This is a class method
my_instance.static_method()  # 输出：This is a static method

# staticmethod装饰类的静态方法使用：
MyClass.aaa(my_instance)   # 必须要传递一个实例化的对象。否则会报错。
MyClass.hhh(my_instance)   # 必须要传递一个实例化的对象。否则会报错。



"""
python核心编程/ 基础教程 / 流畅的python / 数据结构与算法 /(机械工业出版社) / cook book
=========================================  今日大纲 =========================================
两个装饰器方法：
    @classmethod:   ******
                把一个对象绑定的方法，修改为类方法；在这个方法中，还可以引用类中的静态变量
                可以通过类名，或者对象名调用
                可以不用实例化对象，就直接在外部调用这个方法
                什么时候用：  定义了一个方法，默认传递self.但是这个 self没有被使用
                            并且你在这个方法里用到了当前的类名，或者你准备用这个类的内存空间中的名字的时候。
    @staticmethod：  **
                被装饰的方法会成为一个静态方法。
                将一个普通的函数，被挪到类中执行，那么直接给这个函数添加@staticmethod装饰器就可以了
                在函数的内部，既不会用到self 变量也不会用到类，那么就不需要使用

能定义到类中的内容：
            静态变量 ：所有的对象共享的变量   不能重新赋值。
            绑定方法 ： 是个自带 self 参数的函数，  由对象调用
            类方法  ： 是个自带 cls 参数的函数    由对象 或者类调用
            静态方法 ：  不带任何参数的普通函数    由对象 或者类调用
            property属性  ： 将方法伪装成属性    有对象调用，不需要加括号


"""
# classmethod
class Goods:
    __discount = 0.8
    def __init__(self):
        self.__price = 5
        self.price = self.__price*self.__discount
    def chage_discount(self,new_discount):
        Goods.__discount=new_discount
        # 这里不能用 self 不然只是在对象的空间里改折扣

# 定义了一个方法，默认传递 self ，但是这个 self 没有用
    @classmethod
    def change_discount2(cls,new_discount):
        print(Goods,cls)
        cls.__discount=new_discount   # 不用 GOOds主要是万一以后要修改很麻烦
    @staticmethod
    def aaa():
        print('aaa')
Goods.aaa()   # 必须传一个对象

import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        struct_time = time.localtime()
        date = cls(struct_time.tm_year,struct_time.tm_mon,struct_time.tm_mday )
        return date
date1 = Date.today()
print(date1.year)
print(date1.day)

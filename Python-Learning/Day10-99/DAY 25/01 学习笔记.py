"""
========================================= 昨日回顾 =========================================
继承：
    通过继承来解决代码的重用问题
=========================================  今日大纲 =========================================
内置的数据结构：
        {}  key--value   Key找值非常快
        []  序列  index 很快
        ()
        {1,}
        'sex'   str
不是内置的数据结构：
        Queue队列：先进先出 (FIFO)
        Stack栈：  后进先出 (LIFO)

继承：（进阶的知识点）
        多继承的继承顺序问题（项目、源码）
        通过继承实现类的开发规范（工作当中）
多态：
        python当中处处是多态，一切皆对象
        什么是多态？借助Java
        鸭子类型

背诵：（维护代码的话，只能去看代码）
只要继承object类就是新式类，不继承object类的都是经典类

    在python3当中，所有的类都继承object ====> python3当中所有类都是新式类
    在python2当中，不继承object类的都是经典类，继承object的类都是新式类

经典类（旧式类）在python3当中根本不存在，在python2中不继承object类的都是经典类

经典类和新式类的区别：
        在单继承中：无论新式类还是经典类，他们都是一直往父类走的----> 深度优先
        多继承中： 新式类：广度优先，（优先将同级的找完，最后才轮到终极父类） python3全部新式类，
                 经典类：深度优先，一条路先走到最终的父类，   python2不继承object的是经典类
                        走过的就不会再走了

        特殊的广度优先：“小乌龟模型”(好好想一下）  https://www.processon.com/diagraming/6548a4862263183952cd6edb

        多继承的广度优先：  C3算法。可以直接调用方法查看：  类名.miro()  查看继承顺序。只在新式类中有用，经典类中没有。
                    C3算法的流程：
                            A(object）= [AO]
                            B(A) = [BAO]
                            C(A) =[CAO]
                            D(A) = [DAO]
                            E(B) = [EB(A)] =[EBAO]
                            F(C) = [FC(A)] =[FCAO]
                            G(D) = [GD(A)] =[GDAO]
                            H(E,F,G) = C3(E,F,G) = C3(E(B(A))+F(C(A)) + G(D(A)) )
                            = [ H] + [EBAO] +  [FCAO] + [GDAO]
                            = 提取规则：从左到右，出现的第一个父类没有出现在后面的节点中，先提取出来
                            H = [EBAO] +  [FCAO] + [GDAO]
                            HE = [BAO] +  [FCAO] + [GDAO]
                            如果一个父类，出现在第一个，但是没有出现在后面类的第一个，那么先从后面类中提出只出现一次的类
                            HEB = [AO] +  [FCAO] + [GDAO]
                            HEBF = [AO] +  [CAO] + [GDAO]
                            HEBFC =  [AO] +  [AO] + [GDAO]
                            HEBFCG =  [AO] +  [AO] + [DAO]
                            如果从左到右的第一个类也出现在后面所有类作为类的第一个，那么提取出第一个。
                            HEBFCGD =  [AO] +  [AO] + [AO]
                            HEBFCGDA =  [O] +  [O] + [O]
                            HEBFCGDO

python2不支持中文，利用   coding:utf-8    才能使用注释。


普通的类：
抽象类：
        是一个开发的规范，约束一些子类必须实现和父类相同的方法。
        抛异常时，一定要和下面类中的方法传递一样的参数，
        下例
实现抽象类的另一种方法：
            from abc import ABCMeta,abstractmethod  然后进行语法糖，装饰
            缺点：依赖abc模块。
例子：
        支付程序： 微信支付   url链接，告诉你参数什么格式  {'uaername':‘用户名','money':200}
                 支付宝支付   url链接，告诉你参数什么格式  {'uname':'用户名',price':100}
        class Alipay:
            def __init__(self, name):
                self.name = name
            def pay(self,money):
                dic = {'uaername':self.name,'money':money}
                print('%s成功支付宝支付%s 成功'%(self.name,money))

        class Wechatpay:
            def __init__(self, name):
                self.name = name
            def pay(self, money):
                dic = {'uaername': self.name, 'money': money}
                print('%s成功微信支付%s 成功' %(self.name,money))

归一化设计：
        主动 异常抛  raise
        raise xxxx    功能：主动出现一个规范的报错
        raise NotImplementedError('xxx')    发出相应的错误提示信息
        raise ValueError   ....


"""

from abc import ABCMeta, abstractmethod
# 主动抛异常的规范化开发。
class Payment(metaclass=ABCMeta):   # 抽象类，约束子类必须实现和他相同的方法
    # 实现抽象类的另一种方法：
    @abstractmethod   # 如果下面类中的方法不是 Pay 直接实例化都做不了，你看看
    #     Can't instantiate abstract class Applepay with abstract method pay
    def pay(self,money):  # 规定的参数 money ，下面的pay 方法里传递了了什么，也必须接受什么
        raise NotImplementedError('请在子类中重写一个pay 方法')

class Alipay(Payment):
    def __init__(self, name):
        self.name = name
    def pay(self,money):
        dic = {'uaername':self.name,'money':money}
        print('%s成功支付宝支付%s元'%(self.name,money))

class Wechatpay(Payment):
    def __init__(self, name):
        self.name = name
    def pay(self, money):
        dic = {'uaername': self.name, 'money': money}
        print('%s成功微信支付%s元' %(self.name,money))
# 是不是可以统一的做一个功能呢？
import sys
def pay(name,price,kind):
    # if kind == 'Wechatpay':
    #     obj =Wechatpay(name)
    # elif kind == 'Alipay':
    #     obj = Alipay(name)
    # elif kind == 'Applepay':
    #     obj = Applepay(name)
    # obj.pay(price)

    # 学习了反射之后，可以对其进行改进如下：
    class_name = getattr(sys.modules['__main__'],kind)
    obj = class_name(name)
    obj.pay(price)

pay('alex',19999,'Alipay')

#增加一个苹果支付
class Applepay(Payment):
    def __init__(self,name):
        self.name = name
    # def pay(self,money):  如果那个傻批重新起名一个函数，pay 函数里面就没有了 self.pay方法。
    #     dic = {'uaername': self.name, 'money': money}
    #     print('%s成功苹果支付%s元' % (self.name, money))
    def 付钱(self, money):
        dic = {'uaername': self.name, 'money': money}
        print('%s成功苹果支付%s元' % (self.name, money))
pay('张三',999,"Applepay")

# 错误类提示信息：规范化开发

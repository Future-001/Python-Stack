"""                         反射
用字符串数据类型的名字来操作这个名字对应的函数/ 实例变量/绑定方法/各种方法
具体化：
      age = 18 输入age 直接就输出18
有时候，你明明知道一个变量的字符串数据类型的名字，你想直接调用它，但是调不到。
使用反射：
    1. 反射对象的 实例变量
    2. 反射类的 静态变量 绑定方法， 其他方法
    3. 模块中的所有变量
            被导入的模块（模块)
            当前执行的py文件(脚本）

    getattr(对象,'属性或方法名')
    如果是方法名，那么得到的是那个方法的地址
    对象名.属性名/方法名  ======>   getattr(对象名(实际上是内存地址),'属性名/方法名')
    反射本文件中的内容：   getattr(sys.modules['__main__'],'属性名/方法名'
     ====  >  回到第25期 01 学习笔记去看一看支付改进的代码。

     反射的 用法，通常根据  归一化设计，然后通过 反射简化了代码
     反射： 静态变量，绑定方法，实例变量/属性
            模块中的所有变量
            导入模块中的所有的变量
    hasattr(类名/地址,’属性/方法名')  判断一个xxx能否反射
    callable()   判断能不能调用。

    if hasattr(sys.modules['__main__'],'name'):
    print(getattr(sys.modules['__main__'],'alex'))
    # 如果是方法，一定要判断是不是可调用的
    if callable(alex.qq):  # 一定要是可调用的才能加括号
        getattr(alex,'qq')()

setattr(object,'x','y'）   给一个对象设置一个属性：   object.x = y  属性名 x  属性值  y
只能通过 getattr来获取相应的值
"""
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def qq(self):
        print('qqxing')
alex = Person('alex',83)
wusir = Person('wusir',74)
ret = getattr(alex,'name')
print(ret)
ret = getattr(wusir,'qq')
print(ret,wusir.qq)   # 会得到一个内存地址  是类中方法的地址
ret()

# 简化代码的映射
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__))+r'\DAY 25')
# import '01 学习笔记' as a
# ret = getattr(a,'Wechatpay')
# ret2 = getattr(a,'Alipay')

import 测试 as a
print(a.Alipay)
print(a.Wechatpay)
print(getattr(a,'Alipay'))
print(getattr(a,'Wechatpay'))
print(id(a))

# print(sys.modules)
print(sys.modules['测试'])
print(id(sys.modules['测试']))
print(getattr(sys.modules['测试'],'Alipay'))
print(getattr(sys.modules['测试'],'Wechatpay'))

name = "taibai"
age = 22
if hasattr(sys.modules['__main__'],'name'):
    print(getattr(sys.modules['__main__'],'alex'))
    # 如果是方法，一定要判断是不是可调用的
    if callable(alex.qq):  # 一定要是可调用的才能加括号
        getattr(alex,'qq')()


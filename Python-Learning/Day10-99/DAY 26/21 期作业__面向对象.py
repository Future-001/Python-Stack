# 今日作业
# day21作业 面向对象特殊成员和异常处理

# 列举你了解的面向对象中的特殊成员，并为每个写代码示例。



# 看代码写结果
class Base(object):
    def __init__(self, a1):
        self.a1 = a1
    def f2(self, arg):
        print(self.a1, arg)
class Foo(Base):
    def f2(self, arg):
        print('666')
obj_list = [Base(1), Foo(2), Foo(3)]
for obj in obj_list:
    obj.f2(2)   # 调用的 f2 需要传递一个参数来着。


print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print('666')
config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
for item in config_obj_list:
    print(item.num)  # 1 2 3


print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
class RoleConfig(StarkConfig):
    pass
config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)   # 1 168 2 168 3 168



print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
for item in config_obj_list:
    item.changelist(168)   # 1 168 2 168 666 3


print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
    def run(self):
        self.changelist(999)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
config_obj_list = [StarkConfig(1), StarkConfig(2), RoleConfig(3)]
config_obj_list[1].run()   #  2 999
config_obj_list[2].run()    # 666 3



print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
    def run(self):
        self.changelist(999)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self, k, v):
        self._registry[k] = v

site = AdminSite()
print(len(site._registry))   # 空的字典，长度为 0
site.register('range', 666)
site.register('shilei', 438)
print(len(site._registry))   # 字典里内容：  range:666  shilei:438  长度的话 只统计了键吗？所以是 2
#
site.register('lyd', StarkConfig(19))
site.register('yjl', StarkConfig(20))
site.register('fgz', RoleConfig(33))
#
print(len(site._registry))  # 5
print(site._registry)   # 这个字典内容的话：   上面的东西加上  lyd: xxx  yjl:xxx  fgz:xxx  后面的都是地址


print()
# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
    def run(self):
        self.changelist(999)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self, k, v):
        self._registry[k] = v

site = AdminSite()
site.register('lyd', StarkConfig(19))
site.register('yjl', StarkConfig(20))
site.register('fgz', RoleConfig(33))
print(len(site._registry))  # 3
for k, row in site._registry.items():
    row.changelist(5)   # 19 5 20 5 666 33


print()
# 看代码写结果
class F3(object):
    def f1(self):
        ret = super().f1()   # 去找子类的父类的f1方法了。
        print(ret)
        return 123
class F2(object):
    def f1(self):
        print('123')
class F1(F3, F2):   # 多继承，新式类，广度优先。  F1 F3 F2
    pass
obj = F1()
obj.f1()   # 123 None
print(F1.mro())


print()
# 看代码写结果
class Base(object):
    def __init__(self, name):
        self.name = name
class Foo(Base):
    def __init__(self, name):
        super().__init__(name)
        self.name = "于大爷"
obj1 = Foo('alex')
print(obj1.name)     # 于大爷

obj2 = Base('alex')
print(obj2.name)    # alex



print()
# 看代码写结果
class Base(object):
    pass
class Foo(Base):
    pass
obj = Foo()
print(type(obj) == Foo)   # True
print(type(obj) == Base)   # False
print(isinstance(obj, Foo))   # TRUE
print(isinstance(obj, Base))    # TRUE


print()

# 补全代码
class Stack(object):   # 后进先出
    def __init__(self):
        self.data_list = []
    def push(self, val):
        self.data_list.append(val)
    def pop(self):
        return self.data_list.pop()

obj = Stack()
# 调用push方法，将数据加入到data_list中。
obj.push('alex')
obj.push('武沛齐')
obj.push('金老板')
#
# 调用pop讲数据从data_list获取并删掉，注意顺序(按照后进先出的格式)
print(obj.pop())  # 金老板
print(obj.pop())   # 武沛齐
print(obj.pop())  # alex




# 如何主动触发一个异常？
#  raise NotImplementError

print()
# 看代码写结果
def func(arg):
    try:
        int(arg)
    except Exception as e:
        print('异常')
    finally:
        print('哦')
func('123')
func('二货')

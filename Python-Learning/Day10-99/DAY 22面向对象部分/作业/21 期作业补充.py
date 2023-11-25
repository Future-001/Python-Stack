# 今日作业
# 简述编写类和执行类中方法的流程。
# 编写类的流程和执行类中方法的流程

# 简述面向对象三大特性?
# 将以下函数改成类的方式并调用:
# def func(a1):
#     print(a1)
class A:
    def __init__(self,a1):
        print(a1)
a=A(5)

# 面向对象中的self指的是什么?     我认为指的是一个形式参数，用来存放了 __init__ 的地址。存放属性。

# 以下代码体现向对象的么特点?
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# obj = Person('武沛齐', 18, '男')

# 以下代码体现向对象的么特点?
# class Message:
#     def email(self):
#         """发送邮件:return:"""
#         pass
#     def msg(self):
#         """发送短信:return:"""
#         pass
#     def wechat(self):
#         """  发送微信 :return:"""
#         pass

# 看代码写结果
class Foo:
    def func(self):
        print('foo.func')
obj = Foo()
result = obj.func()     # 输出了 foo.func
print(result)  # none


# 面向对象中为什么要有继承?
#
# Python继承时，查找成员的顺序遵循么规则?
#
# 看代码写结果
class Base1:
    def f1(self):
        print('base1.f1')
    def f2(self):
        print('base1.f2')
    def f3(self):
        print('base1.f3')
        self.f1()
class Base2:
    def f1(self):
        print('base2.f1')
class Foo(Base1, Base2):
    def f0(self):
        print('foo.f0')
        self.f3()
obj = Foo()  # 这里的话，应该不执行什么，就是只是地址。
obj.f0()     # 执行后，输出的结果是： f00.f0  base1.f3  base1.f1
# 最后，应该在同一片空间中，优先寻找f1


# 看代码写结果:
class Base:
    def f1(self):
        print('base.f1')
    def f3(self):
        self.f1()
        print('base.f3')
class Foo(Base):
    def f1(self):
        print('foo.f1')
    def f2(self):
        print('foo.f2')
        self.f3()
obj = Foo()
obj.f2() # foo.f2  base.f1   base.f3
  #  出错了，第二个  应该输出   foo.f1????  寻址顺序： 优先从主类里面寻找
  #  主类-->  当前类-->其余类


# 补充代码实现
user_list = []
while True:
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    email = input("请输入邮箱:")
#     """
#     # 需求
#     1.txt. while循环提示用户输入: 户名、密码、邮箱(正则满 邮箱格式)
#     2. 为每个用户创建一个对象，并添加到表中。
#     3. 当表中的添加3个对象后，跳出循环并以此循环打印所有 户的姓名和邮箱
#     """
#     补充代码: 实现用户注册和登录。
#     class User:
#         def __init__(self, name, pwd):
#             self.name = name
#             self.pwd = pwd
#     class Account:
#         def __init__(self):
#             # 用户列表，数据格式：[user对象，user对象，user对象]
#             self.user_list = []
#         def login(self):
#             """
#             用户登录，输入用户名和密码然后去self.user_list中校验用户合法性
#             :return:
#             """
#             pass
#         def register(self):
#             """
#             用户注册，没注册一个用户就创建一个user对象，然后添加到self.user_list中，表示注册成功。
#             :return:
#             """
#             pass
#         def run(self):
#             """
#             主程序
#             :return:
#             """
#             pass
#     if __name__ == '__main__':
#         obj = Account()
#         obj.run()



#     预习
#     类成员
#     http: // www.cnblogs.com / wupeiqi / p / 4493506.
#     html
#     http: // www.cnblogs.com / wupeiqi / p / 4766801.
#     html
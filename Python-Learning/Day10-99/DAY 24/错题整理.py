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
# 看代码写结果
class Foo(object):
    def __init__(self, num):
        self.num = num
v1 = [Foo for i in range(10)]  # 列表推导式 里面存了10个地址，都是Foo，
v2 = [Foo(5) for i in range(10)]  # 里面存了很多个地址，可以查看具体的内容，内容肯定是  num=5
v3 = [Foo(i) for i in range(10)]   # 还是地址，地址里面的内容是 0-9 刚开始为什么想错了，
# 实例化，相当于开辟一段空间，所以不同的i ，开辟的空间肯定是不一样的。 并不是和 生成器表达式一样的。
# 注意一个例子： 如果实例化对象没有用到，那么地址是一样的，但是一旦用到了实例化对象，那么地址就不同了。
# 看一下  DAY27 面向对象收尾，笔记回顾

# print(v1)
# print(v2)
# print(v3)
for i in v2:
    print(i.num,end='  ')
for j in v3:
    print('  |'+str(j.num),end = ' ')

print()
# 看代码写结果
class Foo(object):
    n1 = '武沛齐'
    n2 = '金老板'
    def __init__(self):
        self.n1 = '女神'
obj = Foo()
print(obj.n1)  #  这里的结果是 女神
print(obj.n2)   #  金老板

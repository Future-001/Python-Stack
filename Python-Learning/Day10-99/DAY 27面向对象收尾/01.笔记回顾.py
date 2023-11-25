""" classmethod
         用不到对象，并且要用类名的时候
         装饰一个对象绑定方法，被装饰的方法会变成类方法
 staticmethod
         把一个函数放到类里，变成一个静态方法
         把这个方法及用不到对象，也用不到类

 魔术方法：
         __new__: 构造方法，开辟空间的，在实例化对象之前的，在 __init__ 之前执行
                 单例模式
         __call__: 这要类中有这个方法，这个类的对象就可以 加括号，调用的就是  __call__ 方法
         __len__:  只要类中有这个方法，就可以直接使用 len(obj)
         __str__:  只要类中有这个方法，打印对象/\%s\str()  对象就显示这个方法的返回值
         __repr__:  str的备胎，但是他自己的 %r/repr()   的时候就只显示这个 方法的返回值


  是否被引用决定了对象地址是否一致：    例子如下
    """
class A:
    def __init__(self,n):
        self.n = n
print(A(1))
print(A(3))
print(A(1) == A(3))
print(id(A(1)) == id(A(3)))

print(A(1)==A(1))

obj1 = A(1)
obj2 = A(2)
print("注意看地址： ",obj1,obj2)
print(id(obj1.n),id(obj2.n))



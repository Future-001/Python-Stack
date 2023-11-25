# 请写出下列代码片段的输出结果：
#
def say_hi(func):
    def wrapper(*args,**kwargs):
        print(id(wrapper))
        print("HI")
        print(id(func))
        ret=func(*args,**kwargs)
        print(id(func))
        print("BYE")
        print(id(wrapper))
        return ret
    return wrapper

def say_yo(func):
    def wrapper(*args,**kwargs):
        print(id(wrapper))
        print("Yo")
        print(id(func))
        return func(*args,**kwargs)
    return wrapper
@say_hi  # 抱歉没看懂，这里是两个装饰器来着： func = say_hi(func)  但是这里的 func 等于 say_hi 里wrapper 的地址
            # 或许理解了，这里的话 func 的真实地址没有被传输进去，因为函数没有被执行。
@say_yo    # 这里我再次换了，  func = say_yo(func)   但是这里的 func 等于 say_yo 里wrapper 的地址
            # 这里 func 指向的 wrapper1 再次指向了 wrapper2 ,注意，函数没有被执行，所以没有传进去 func 的真实地址
def func():
    print("ROCK&ROLL")
    print(id(func))
func()       # 函数执行，找到离他最近的 装饰器，传输进去地址。
#  最终输出的是：   yo HI ROCK&ROLL BYE  实际上是 HI YO ROCKi&ROLL BYE

# 解释： 由外到内，逐步调用，ji
"""
在你的装饰器链中，@say_hi 装饰器被应用在 @say_yo 装饰器之上。
这意味着 say_hi 装饰器的 wrapper 函数将成为 say_yo 装饰器的外部包装，而不是内部包装。
因此，装饰器链的由内到外顺序:
@say_yo 装饰器应用于 func，将 func 替换为 say_yo 装饰器的 wrapper 函数。
@say_hi 装饰器应用于 func，将 func 替换为 say_hi 装饰器的 wrapper 函数。
所以，func 最终引用的是 say_hi 装饰器中的 wrapper 函数。这是由于装饰器链的执行方式，从外到内执行。
如果你想要让 func 最终引用 say_yo 装饰器中的 wrapper 函数，你需要调整装饰器的顺序，将 @say_yo 放在 @say_hi 之上：

既然 func 最终指向是 yo 中的wrapper，为什么不直接执行 yo 中的wrapper呢？还有转换一次呢
你的问题是非常合理的。根据你的装饰器链，func 最终指向的是 say_yo 装饰器中的 wrapper 函数。
因此，为什么最终的输出不是直接执行 say_yo 中的 wrapper 呢？
这是因为装饰器链的应用是从内到外的，也就是说，最内层的装饰器最后起作用。当你调用 func() 时，
实际上首先执行的是最内层的 say_yo 装饰器的 wrapper 函数。
然后，这个 wrapper 函数返回的结果将传递给中间的 say_hi 装饰器的 wrapper 函数，以此类推，直到最外层的装饰器。
在你的装饰器链中，func 确实最终指向 say_yo 装饰器中的 wrapper 函数，但装饰器链的执行顺序是按照装饰器的嵌套顺序执行的。
这就解释了为什么最终的输出不是直接执行 say_yo 中的 wrapper。
所以，输出的顺序是 "HI"（来自 say_hi 装饰器） → "Yo"（来自 say_yo 装饰器） → "ROCK&ROLL"
（来自 say_yo 装饰器，最内层的装饰器的效果） → "BYE"（来自 say_hi 装饰器，最外层的装饰器的效果）。
"""



# 下面自己写一个把：理解一下，总之就是先执行 B 在执行 A
"""有一点我不理解，执行到@A,那么为什么没有星这里进去呢？就比如说，原函数f,为什么没有被赋值为A里面的wrapper, 
A里面的f就是原函数f的地址，然后执行到@B的时候，原来的f由A的wrapper变成了B的wrapper,同时，B里面的f是A的wrapper， 
这样执行的结果和运行的结果不同，我想知道为什么不是这样呢？谢谢解答

补充∶我理清楚了你文档里面的东西，就是执行到f的时候，我们从B进去，那么此时的f就是B里面wrapper的地址，
B里面的f就是真实的f的地址，之后，执行A,此时f由B里面wrapper的地址变为了A的wrapper,地址，A里面的f是B里面的wrapper的地址，
希望我这样的理解没错 但是我不太理解，按照这样的逻辑，由于Python是解释型语言，那为什么不是按照我的第一种理解去执行呢？"""
print()
def A(f):
    print('我是 A 的外1层')
    def inner(*args,**kwargs):
        print('我是 A 的内1层')
        ret= f(*args,**kwargs)
        print('我是 A 的内2层')
        return ret
    print('我是 A 的外2层')
    return inner

def B(f):
    print('我是 B 的外1层')
    def inner(*args,**kwargs):
        print('我是 B 的内1层')
        ret= f(*args,**kwargs)
        print('我是 B 的内2层')
        return ret
    print('我是 B 的外2层')
    return inner

# @A
# @B
def func(a,b):
    print('终于轮到我了，我是一个什么函数啊')
    return a+b

print(func(1,3))

# 上述代码相当于这个东西
print()
func=A(B(func))
# 也就是  func1 = B(func)   func = A(func1)
result = func(1,3)
print(result)

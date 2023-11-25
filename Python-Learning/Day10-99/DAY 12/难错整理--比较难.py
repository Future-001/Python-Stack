# 看代码求结果：（面试题）
""" 好好看一看 """
print()
def demo():
    for i in range(4):
        yield i


g = demo()       # 这是一个 生成器： 可以将其转化为列表。
print(g)
g1 = (i for i in g)
# 生成器推导式这里都是生成器， 通过循环生成器可以对其进行取值操作。。。。。。。  只要你没有取值操作，可以无限循环，
#  当然，循环取到的数值 也和 g 一样的，都是 0123
g2=(i for i in g1)
# 这里也是循环，得到了同一个迭代器，（地址是不一样的哈，注意，只是他们指向的数据的地址是同一个？）

print(g1)

print(list(g1))  # 生成器转化为列表，那么里面的元素可视化   注意 生成器是 不能会有的  一路 next 不能回头
# list((i for i in demo())) 相当于这个了呢
print(list(g2))        # 为什么为空 ：   不能回头，取到最后去不回来了，
# g1,g2的地址是不同的，但是，他们只想的 生成器的数据地址可能是一样的，所以，g1 循环输出结束后，由于不能回头，所以输出了空

""" 
        +++++++++==================================++++++++++++++++=============================================================
"""

print()
# 看代码求结果：（面试题）


def add(n,i):
    return n+i


def test():
    for i in range(4):
        yield i


# 是一个生成器 （函数）  g 生成器中含有 0123
g = test()
for n in [1,10]:
    g=(add(n,i) for i in g)     # 这也是一个生成器呢，
    # 错误思路是这样 先对 g 循环，然后开辟一个新的内存空间存储新数据，最后 g 指向了新的内存地址。
    # 实际上，第一次执行完毕后，并不会存储 g ,只是会将 第一次 g 运算的表达式存储一次。但是注意 n 会被第二次的 n 替换
    # 第一次循环  n =1.txt  g = (add(n,i) for i in g)
    # 第二次循环  n =10  g = (add(n,i) for i in g)

# 一定要注意，第二次的 n 将第一次的 n 覆盖了，所以，所以，最后的输出 是  n = 10 进行了两次加法
    # list(g) ------list(add(n,i) for i in (add(n,i) for i in test()))
    # list(g) ------list(add(10,i) for i in (add(10,i) for i in test()))
    #  等同于  ：  list(g) ------list(add(10,i) for i in (add(10,i) for i in [1.txt,2,3,4]))
    #  等同于  ：  list(g) ------list(add(10,i) for i in ([11,12,13,14]))
    l1 = (add(n,i) for i in test())
    l2 = (add(n,i) for i in test())
#     不理解的点是： 为什么生成器的 对象 可以直接 和 n 相加呢？  哦哦 原来用了循环
#     生成器的取值方法：  next  for  list
    if n == 1:
        print(list(l1))  # [1.txt, 2, 3, 4]
    if n ==10:
        print(list(l2))   # [10, 11, 12, 13]

print(list(g))

# 为什么输出是   [20, 21, 22, 23]
# 第一次循环  n =1.txt  g = (add(n,i) for i in g)
# 第二次循环  n =10  g = (add(n,i) for i in g)
# 第二次的 n = 10 会将第一次的 n 覆盖掉，但是 g 没有被覆盖，为什么呢？ 因为 第一次的 g 都没有运行呢，所以不会得到这个结果，
# 相当于两次的 n 都是 10 ，并且第一次的 g 没有被保存，只是保存了表达式

# list(g) ------list(add(n,i) for i in (add(n,i) for i in test()))
# list(g) ------list(add(10,i) for i in (add(10,i) for i in test()))
#  等同于  ：  list(g) ------list(add(10,i) for i in (add(10,i) for i in [1.txt,2,3,4]))
#  等同于  ：  list(g) ------list(add(10,i) for i in ([11,12,13,14]))



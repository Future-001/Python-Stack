# 1.你了解生产者模型消费者模型么？如何实现？
    # 主要是利用队列，传递消息  q = Queue()   q.put()  q.get()

# 2.GIL锁是怎么回事?
    # 全局解释器锁，主要用来限制线程的并发，不然的话会导致内存的不安全性。

# 3.请简述进程和线程的区别？
    # 进程是计算机资源分配的最小单位，
    # 线程是CPU进行资源调度。

# 4.多进程之间是否能实现数据共享？用哪个模块实现？
    # 不能，可以利用Manager 模块实现

# 生成器练习题
# 1.读代码猜答案

g1 = filter(lambda n:n%2==0,range(10))  # i: 0 2 4 6 8
g2 = map(lambda n:n*2,range(3))  # 0,2,4
for i in g1:
    print("i",i)
    for j in g2:
        print("j", j)
        print(i*j)  # 注意一下，生成器不走回头路啊，，，，，，读取完了就结束了

# 2.以下代码的输出是什么？请给出答案并解释。

def multipliers():
    return [lambda x:i*x for i in range(4)]
    # return [lambda 2:i*2 for i in range(4)]  这里其实都得到同样大小的数字 [6,6,6,6,]
print([m(2) for m in multipliers()])  # 这里的结果是：

# 请修改multipliers的定义来产生期望的结果。 [0,2,4,6]

def multipliers2():
    return (lambda x:i*x for i in range(4))

print([m(2) for m in multipliers2()])
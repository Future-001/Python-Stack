# 1.你了解生产者模型消费者模型么？如何实现？
# 2.GIL锁是怎么回事?
# 3.请简述进程和线程的区别？
# 4.多进程之间是否能实现数据共享？用哪个模块实现？

# 生成器练习题
# 1.读代码猜答案
#
# g1 = filter(lambda n:n%2==0,range(10))
# g2 = map(lambda n:n*2,range(3))
# for i in g1:
#     for j in g2:
#         print(i*j)
# 2.以下代码的输出是什么？请给出答案并解释。
#
# def multipliers():
#     return [lambda x:i*x for i in range(4)]
# print([m(2) for m in multipliers()])
# 请修改multipliers的定义来产生期望的结果。
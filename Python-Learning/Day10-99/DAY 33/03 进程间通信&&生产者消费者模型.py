"""
Inter Process commuciation  (IPC) 进程间通信
        基于文件：同一台机器上的多个进程间的通信(进程间的通信！！！)
            队列：一定是multiprocessing 中的队列
                基于socket文件级别的通信来完成数据传递

        基于网络：同一台或者多台机器上的多进程间通信
                第三方工具：(消息中间件)
                    memcache
                    redis
                    rabbitmq
                    kafka

"""
from multiprocessing import Queue,Process

def son(q):
    q.put("hello")

if __name__=="__main__":
    q=Queue()
    Process(target=son,args=(q,)).start()
    print(q.get())  # 注意，如果在开启一个程序，但是他的get 和 put 不匹配，get 多的话，输出缓冲区中没有了数据，会一致阻塞
    # 不然的话，有多少他就会取出多少数据


import time,random
"""
=================================生产者消费者模型=========================================
应用：爬虫，分布式操作 clelry 其实就是两个大的生产者消费者模型
本质： 就是让生产数据和消费数据的效率达到平衡平最大化的效率

"""
def consumer(q,name):
    while True:
        food=q.get()
        if food:
            print("%s吃了%s" %(name,food))
        else:break

def producer(q,name,food):
    for i in range(10):
        foodi="%s%s" %(food,i)
        print("%s生产了%s" %(name,foodi))
        time.sleep(random.random())
        q.put(foodi)


if __name__ == "__main__":
    q= Queue()
    c1 =Process(target=consumer,args=(q,"王五"))
    p1=Process(target=producer,args=(q,"李四","香蕉"))
    p2=Process(target=producer,args=(q,"张三","草莓"))
    c1.start()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)
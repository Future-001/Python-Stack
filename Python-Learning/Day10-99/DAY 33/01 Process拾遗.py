"""
===========================================昨日内容回顾====================================================
同步异步阻塞和非阻塞：
    同步阻塞/非阻塞：
        调用一个函数需要等待该函数执行结果，在此过程中同时CPU不工作/工作
        input,join()    eval
    异步非阻塞：
        调用一个函数，不需要等待结果，同时CPU工作   start()
    异步阻塞：
        调用一个函数不需要等待执行结果，同时在此过程中CPU不工作
        开启10个进程，异步， 某种方法获取这个进程的返回值，谁先结束，获取谁的返回值

进程的三状态图：
        就绪，运行，阻塞

进程的调度算法：
        先来先服务，短作业优先，多级反馈算法；分子

进程开启和关闭：
        父进程，子进程
        父进程要负责给子进程回收进程结束之后的资源

join

============================================今日内容===========================================
Process类拾遗：
    开启进程的另一种方法：   例1
            面向对象的方法，通过继承和重写run方法，完成了启动子进程
            通过重写 init 和调用父类的 init 完成了给子进程传递参数

    Process类的一些其他方法\属性：
                "查看进程的名字:",p.name)
                "查看进程的id号：",p.pid,p.ident)
                "杀死进程：",p.terminate())
                "查看进程是否还活着：",p.is_alive())
                time.sleep(0.01)
                "说明了他是异步非阻塞", p.is_alive()

    守护进程：
            .daemon     一定要在进程启动之前
            主进程会等待所有的子进程结束，是为了回收子进程的资源
            守护进程会等待主进程的代码执行结束（不是等待主进程结束，里面还有其他子进程，主进程是最后结束的，要回收资源）之后在结束
            主进程的代码什么时候结束，守护进程就什么时候结束，和其他子进程的执行进度无关。
            以前小米：通过守护进程向系统报告进程挂没挂，监控功能

进程同步 --- lock  锁 *****
进程之间通信 --- 队列  ***
进程之间的数据共享 --- Manager  *

"""
# 开启进程的另一种方法  例1
from multiprocessing import Process
import os,time

class MyProcess(Process):
    def run(self):
        print(os.getpid(),os.getppid(), self.msg)

    # 如果需要进行传参的话
    def __init__(self, msg):
        self.msg = msg
        super().__init__()


if __name__ == '__main__':
    for i in range(3):
        p = MyProcess("只能在这里传参")
        p.start()
        print("查看进程的名字:",p.name)
        print("查看进程的id号：",p.pid,p.ident)
        print("杀死进程：",p.terminate())  # 就看不了run 里面运行的代码了。所以有问题
        print("查看进程是否还活着：",p.is_alive())
        time.sleep(0.01)
        print("说明了他是异步非阻塞", p.is_alive())

        print()

# print("========================守护进程===================================")

# 这个会执行三次：为什么？看上面的原理,还是没有理解

def son1():
    while True:
        print("--> in son1")
        time.sleep(1)
def son2():
    for i in range(10):
        print("in son2")
        time.sleep(1)

if __name__ == "__main__":
    p1 = Process(target=son1)
    p1.daemon = True  # 表示设置 p1是一个守护进程
    p1.start()
    p2 = Process(target=son2)
    p2.start()
    time.sleep(3)
    print("in main")
    p2.join()  # 这样的话，守护进程就会等待主进程结束之后在结束

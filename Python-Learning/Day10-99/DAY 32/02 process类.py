"""
multiprocessing :
            多元的处理进程的模块（和进程相关的内容都在这个模块里面）
            from multiprocessing import Process  这个首字母大写，是一个类，当然有process模块，二者不一样


为什么要用 if __name__ == "__main__": =======> 只会在主进程中执行的代码
    windows:    进程之间的所有的内存是隔离开的
        主进程（父进程）加载顺序： 内置名称空间内容==> 全局名称空间 ==> os,Process,func p等
        执行到 p.start 开始加载子进程， import 父进程所在的文件 os Process func==> 此时 __name__
        脚本执行的时候是原来的文件名，就不执行继续开启进程的操作了，不然不断开启进程。。。。==> 开启子进程让执行，func恰好有func,执行func
    Linux:    fork进程 直接将父进程的内存空间中的所有内容，全部copy到了子进程内存空间来了

能不能给子进程传递参数:
        肯定可以 Process(target=func,args=("传递的数据一定要是一个元组",))

能不能获取子进程的返回值:
        不能，由于进程内存隔离，

能不能同时开启多个子进程:
        可以

join的用法：
        p.join()  同步阻塞，直到p这个子进程执行完毕才继续执行代码
        for i in args_list:
            p.Process(target=func,args=i)
            p.start()
        p.join()   由于P有同名变量，把之前的进程给覆盖了，你就看不到是不是执行完成了。。。

        改进，p_l = []  ,  p_l.append(i)   ,  for p in p_l: p.join()

同步阻塞   异步非阻塞

验证多进程之间的数据是否隔离：
        n=0
        def func():
            global n
            n+=1
        if __name__ = "__main__":
            p_l = []
            for i in range(100)
                p = Process(target=func)
                p.start
                p_l.append(p)
            for p in p_l:p.join()
            print(n)  会明显看到，他还是 n=0


是引用多进程实现一个并发的socket 的server
"""
from multiprocessing import Process
import os
import time

def func(args):
    print(args)
    time.sleep(1)
    print("这里相当于子进程： ",os.getpid(), os.getppid())           # ppid parent process id


print("windows 主进程和子进程都可以执行，下面的代码只在主进程中执行一次")
if __name__ == "__main__":  # windows开发平台必须要加这句话，主要是他的内存空间的顺序。
    print("主进程：         ",os.getpid(), os.getppid())
    p = Process(target=func,args=("传递元组,并发进程1",))

    p.start()   # 这相当于开启了一个子进程（以现在的进程作为父进程（注意进程id))

    p = Process(target=func,args=("并发进程2",))
    p.start()  # 异步非阻塞

    p = Process(target=func,args=("并发进程3",))
    p.start()

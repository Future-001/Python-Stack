"""
进程：进行中的程序就是一个进程
       占用资源，需要操作系统调度
       pid : 进程id，每次重新启动都不一样。
       进程是计算机当中最小的资源分配单位。

并发：
     多个程序同时执行===> 其实特指，只有一个CPU，多个程序轮流在一个CPU上执行
     宏观上：多个程序在同时执行
     微观上：多个程序轮流在一个CPU上执行，本质上还是串行

并行：
    多个程序 同时 在 多个CPU 上执行

同步：
     执行某个A程序，发起了另一个B程序，必须等待B执行完成之后才能执行A

异步：
    执行某个A程序，发起了另一个B程序，不需要等待B执行完成，就可以继续执行A

阻塞：
     CPU不工作，就是阻塞，input accept recv recvfrom sleep connect
非阻塞:
     CPU工作的时候

线程：
     存储在进程当中，一个进程可以含有多个线程，
     线程是计算机中能被CPU调度的最小单位


进程，线程，并发，并行，同步，异步，阻塞，非阻塞

input 只能在父进程中使用，子进程中不能使用
"""
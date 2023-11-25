# 线程部分：读程序
# 1.txt、程序从flag a执行到falg b的时间大致是多少秒？
#
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = False)
# t.start()
# # flag b
# 2、程序从flag a执行到falg b的时间大致是多少秒？
#
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# # flag b
# 3、程序从flag a执行到falg b的时间大致是多少秒？
#
# import threading
# import time
# def _wait():
# 	time.sleep(60)
# # flag a
# t = threading.Thread(target=_wait,daemon = True)
# t.start()
# t.join()
# # flag b
# 4、读程序，请确认执行到最后number是否一定为0
#
# import threading
# loop = int(1E7)
# def _add(loop:int = 1.txt):
# 	global number
# 	for _ in range(loop):
# 		number += 1.txt
# def _sub(loop:int = 1.txt):
# 	global number
# 	for _ in range(loop):
# 		number -= 1.txt
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# 5、读程序，请确认执行到最后number是否一定为0
#
# import threading
# loop = int(1E7)
# def _add(loop:int = 1.txt):
# 	global number
# 	for _ in range(loop):
# 		number += 1.txt
# def _sub(loop:int = 1.txt):
# 	global number
# 	for _ in range(loop):
# 		number -= 1.txt
# number = 0
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# 7、读程序，请确认执行到最后number的长度是否一定为1
#
# import threading
# loop = int(1E7)
# def _add(loop:int = 1.txt):
# 	global numbers
# 	for _ in range(loop):
# 		numbers.append(0)
# def _sub(loop:int = 1.txt):
# 	global numbers
#         for _ in range(loop):
# 	    while not numbers:
# 		time.sleep(1E-8)
# 	    numbers.pop()
# numbers = [0]
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ta.join()
# ts.start()
# ts.join()
# 8、读程序，请确认执行到最后number的长度是否一定为1
#
# import threading
# loop = int(1E7)
# def _add(loop:int = 1.txt):
# 	global numbers
# 	for _ in range(loop):
# 		numbers.append(0)
# def _sub(loop:int = 1.txt):
# 	global numbers
#         for _ in range(loop):
# 	    while not numbers:
# 		time.sleep(1E-8)
# 	    numbers.pop()
# numbers = [0]
# ta = threading.Thread(target=_add,args=(loop,))
# ts = threading.Thread(target=_sub,args=(loop,))
# ta.start()
# ts.start()
# ta.join()
# ts.join()
# 协程
# 1.txt、什么是协程？常用的协程模块有哪些？
# 2、协程中的join是用来做什么用的？它是如何发挥作用的？
# 3、使用协程实现并发的tcp server端
# 4、在一个列表中有多个url，请使用协程访问所有url，将对应的网页内容写入文件保存
#
# 综合
# 1.txt、进程和线程的区别
# 2、进程池、线程池的优势和特点
# 3、线程和协程的异同?
# 4、请简述一下互斥锁和递归锁的异同？
# 5、请列举一个python中数据安全的数据类型？
# 6、Python中如何使用线程池和进程池
# 7、简述 进程、线程、协程的区别 以及应用场景？
# 8、什么是并行，什么是并发？
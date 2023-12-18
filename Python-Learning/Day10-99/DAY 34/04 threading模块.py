from threading import Thread,current_thread,active_count,enumerate
import time

def func(i):
    print("start%s"%i,current_thread().ident)
    time.sleep(1)
    print("end%ss" %i)

for i in range(10):
    Thread(target=func,args=(i,)).start()

print(enumerate(),active_count())  # 注意，总共有11个线程，因为还要包括主线程

print("所有的线程都执行完了")
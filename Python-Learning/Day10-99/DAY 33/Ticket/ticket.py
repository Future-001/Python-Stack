import json
import time
from multiprocessing import Process,Lock

def search(i):
    with open("ticket",encoding="utf-8") as f:
        ticket = json.load(f)
    print("%s:当前的余票是%s张" %(i,ticket['count']))

def buy_ticket(i):
    with open("ticket", encoding="utf-8") as f:
        ticket = json.load(f)
    if ticket['count']>0:
        ticket['count']-=1
        print("%s,购票成功" %i)
    time.sleep(0.2)  # 主要是为了控制延迟
    with open("ticket", encoding="utf-8",mode ="w" ) as f:
        json.dump(ticket,f)


# 锁 ：  lock.acquire()   lock.release()
def get_ticket(i,lock):
    search(i)
    # lock.acquire()  # 这里直接将异步进程 转变为了同步进程
    # buy_ticket(i)   # 这种方式，一旦这段代码出错，会导致一致锁死在这里，
    # lock.release()

    with lock:  # 可以代替acquire 和release 同时在此基础上进行一些异常处理，保证程序能正常运行
        buy_ticket(i)

    # 互斥锁，： 连续的两个acquire 不能在同一个进程中连续acquire多次。

if __name__=="__main__":
    lock = Lock()
    for i in range(10):
        # 为什么 lock=Lock() 加在这里就不行，显示所有人都购票成功？异步执行。

        # Process(target=search,args=(i,)).start()
        # Process(target=buy_ticket,args=(i,)).start()  # 一下子全买成功了，，，离谱
        Process(target=get_ticket,args=(i,lock)).start()  # 一下子全买成功了，，，离谱
import os,time
from multiprocessing import Process

def son1():
    while True:
        print("--> in son1")
        time.sleep(1)
def son2():
    for i in range(10):
        print("in son2")
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=son1)
    p1.daemon = True  # 表示设置 p1是一个守护进程
    p1.start()
    p2 = Process(target=son2).start()
    time.sleep(3)
    print("in main")
# 异步阻塞
import requests
from multiprocessing import Process,Queue

url_list = [
    "https://movie.douban.com/subject/36207130/",
    "https://www.baidu.com",
    "https://xueqiu.com/k?q=%E9%87%8F%E8%83%BD%E6%80%8E%E4%B9%88%E7%9C%8B",
    "https://www.52pojie.cn/forum-4-1.html",
]
def producer(i,url,q):
    ret = requests.get(url)
    q.put((i,ret.status_code))

if __name__ == "__main__":
    q = Queue()
    for index,url in enumerate(url_list):
        Process(target = producer,args = (index,url,q)).start()
    for i in range(4):  # 看结果是 异步阻塞，没有按照顺序等待结果，而是所有的任务都在异步执行这，但是我要等结果又不知道谁的结果先来
        # 涉嫌结束我就获取谁的结果
        print(q.get())
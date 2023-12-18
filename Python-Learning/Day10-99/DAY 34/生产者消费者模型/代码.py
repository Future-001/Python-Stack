import requests
from multiprocessing import Process,Queue

url_dic = {
    "douban":"https://movie.douban.com/subject/36207130/",
    "baidu":"https://www.baidu.com",
    "雪球":"https://xueqiu.com/k?q=%E9%87%8F%E8%83%BD%E6%80%8E%E4%B9%88%E7%9C%8B",
    "52破解":"https://www.52pojie.cn/forum-4-1.html",
}

def producer(name,url,q):
    ret = requests.get(url)
    q.put((name,ret.text))

def Consumer(q):
    while True:
        content = q.get()
        if content==None:break
        with open("%s.html" %content[0],encoding = "utf-8",mode="w") as f:
            f.write(content[1])

if __name__ == "__main__":
    q = Queue()
    p_l = []
    for name,url in url_dic.items():
        p=Process(target = producer,args = (name,url,q))
        p.start()
        p_l.append(p)
    Process(target=Consumer,args=(q,)).start()
    for i in p_l:i.join()
    q.put(None)

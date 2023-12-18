from multiprocessing import Process,Manager,Lock

def change_dic(lock,dic):
    with lock:  # 保证了数据安全
        dic['count']-=1

if __name__ == "__main__":
    m = Manager()   # 这里相当于 with  Manager() as m: 下面的代码不变
    lock = Lock()
    dic = m.dict({"count":100})
    # dic = {"count":100}
    p_l = []
    for i in range(100):
        p=Process(target=change_dic,args=(lock,dic,))
        p.start()
        p_l.append(p)

    for p in p_l:p.join()
    print(dic)
    # 注意： dic 中count的数据是不一样的，数据不安全，因为同时取用数据了（并发）
from core import src
# from core.src import status
from conf.setting import *

def limit_time(t=0):
    last_call = 0
    def auth(f):
        def inner(*args,**kwargs):
            nonlocal last_call
            if src.status == True or f.__name__ in ('login','register'):
                if time.time()-last_call>=t:
                    ret = f(*args,**kwargs)  # 用户名应该是要传递回来的，不传递回来做不了后面的usr
                    # 但是传回来了，应该给谁呢？下面的列表函数能传参数，但是，参数怎么传递呢？都是从登录这块拿走的
                    last_call = time.time()
                    return ret
                else:
                    print('操作太频繁，请稍后再试。')
                    return
            else:
                print('请先登录后操作。')
        return inner
    return auth
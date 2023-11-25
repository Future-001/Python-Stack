import time
def log(path):
    def wrapper(func):
        def inner(*args,**kwargs):
            ret = func(*args,**kwargs)
            with open(path,mode='a',encoding = 'utf-8') as f:
                msg = f"{time.strftime('%Y-%m-%d %H:%M:%S')} ,执行了{func.__name__}\n"
                f.write(msg)
            return ret
        return inner
    return wrapper

@log('login.log')    # r = log('login.log')==wrapper  @r==@wrapper--->  login = wrapper(login)
def login():
    pass

@log('buy.log')
def buy():
    pass
login()
buy()

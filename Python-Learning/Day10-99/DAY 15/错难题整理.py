
# 函数的参数传递是地址还是新值？
# 函数的参数传递 是 传递的地址还是新值？？？ 如果是变量，那么只是传递了数值，没有共享地址，如果是函数名，那么传递了地址？
# 那么这里就是说，如果传递的是 可变的数据类型，那么，他传递的是地址，是吗？？？？？

# 请实现一个装饰器，限制该函数被调用的频率，如10秒一次（借助于time模块，time.time()）（面试题,有点难度，可先做其他）
import time
def time_limit(t=0):
    def wrapper(func_name):
        last_called_time = 0
        def inner(*args,**kwargs):
            nonlocal last_called_time
            current_time = time.time()
            if func_name.__name__=='test' and current_time - last_called_time <t:
                print('函数调用太频繁，请稍后再试')
                return
            ret = func_name(*args, **kwargs)
            last_called_time = current_time
            return ret
        return inner
    return wrapper
@time_limit(5)  # @time_limit(5) 等价于 test = time_limit(5)(test)
def test():
    print('限制使用时间')
    t1 = time.strftime("%Y-%m-%d  %H:%M:%S",time.localtime())
    print(f'使用时间是 {t1}')
    return t1
@time_limit()
def test2():
    print('只针对特定函数')
test2()
test2()
test()
test()
time.sleep(3)
test()
time.sleep(6)
test()
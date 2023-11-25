# 整理今天的笔记以及课上代码，完善昨天没有写完的作业，先把上午留的装饰器认证登录的完成。
#
# 将课上模拟博客园登录的装饰器的认证的代码完善好，整清楚。
# 看代码写结果：
def wrapper(f):
    def inner(*args,**kwargs):
        print(111)
        print("每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码")
        ret = f(*args,**kwargs)
        print(222)
        return ret
    return inner

@wrapper
def func():
    print(333)

print(444)
func()    # 这里执行了 inner 先输出 111 333 222  好吧，没用装饰器。。。。
print(555)
#
# 编写装饰器,在每次执行被装饰函数之前打印一句’每次执行被装饰函数之前都得先经过这里,这里根据需求添加代码’。



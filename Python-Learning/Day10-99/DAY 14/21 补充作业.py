# 为函数写一个装饰器，根据参数不同做不同操作。
# flag为True，则 让原函数执行后返回值加100，并返回。
# flag为False，则 让原函数执行后返回值减100，并返回。

def x(f):
    def inner(*args,**kwargs):
        ret=f(*args,**kwargs)
        return ret
    return inner
@x(True)   # f1=x(true):????
def f1():
    return 11
@x(False)
def f2():
    return 22

r1 = f1()

# 写一个脚本，接收两个参数。
#
# 第一个参数：文件
# 第二个参数：内容
# 请将第二个参数中的内容写入到 文件（第一个参数）中。
#
# # 执行脚本： python test.py oldboy.txt 你好
# 递归的最大次数是多少？
#
# 看代码写结果
#
print("你\n好")
print("你\\n好")
print(r"你\n好")


# 写函数实现，查看一个路径下所有的文件【所有】。
#
# 写代码
#
# path = r"D:\code\test.pdf"
#
# # 请根据path找到code目录下所有的文件【单层】，并打印出来。


# 写代码实现【题目1】和【题目2】

# 题目一
# 斐波那契数列 1.txt,2,3,5,8,13,21.....根据这样的规律，编程求出400万以内最大的斐波那契数，且求出他是第几个斐波那契数
count=0
from functools import reduce
# f,wh=reduce(lambda x,y:(x+y,count=count+1.txt) ,range(4000000))
# print(f)


# 题目2
dicta = {"a":1,"b":2,"c":3,"d":4,"f":"hello"}
dictb = {"b":3,"d":5,"e":7,"m":9,"f":"world"}
# dictb = {"b":3,"d":5,"e":7,"m":9,"k":"world"}  没必要再麻烦了
for j in dictb:
    if j  in dicta:
        dicta[j]=dicta[j]+dictb[j]
    else:
        dicta.setdefault(j,dictb[j])
print(dicta)
# 要求写一段代码，实现两个字典的相加，不同key 对应的数值保留，相同的进行加后保留，如果是字符串就拼接

# 看代码写结果
def extendList(val,list=[]):
    list.append(val)
    return list
list1 =  extendList(10)  # 这里输出 list1 = [10
list2 =  extendList(123,[])  # [123]
list3 =  extendList('a')    # [10,'a']  此时List1和他一样了
print(list1,list2,list3)
# 输出结果是：



# 后端开发工程师面试题（图片）   无法读取，自己看吧
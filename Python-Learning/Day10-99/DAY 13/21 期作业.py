# 什么是匿名函数？
# 一句话函数 lambda x:return

# 尽量多的列举你了解的内置函数？【默写】
#
l1 = [1,2,3,4,5]
print( '__iter__' in dir(l1))
print( '__iter__' in dir(l1) and '__next__' in dir(l1))
print(dir(iter(l1)))

print(int(9.3))
print(float(24))
print(eval('1.txt  +23  +13'))
msg = """
for i in range(3):
    i=i*2
    print(i)"""
exec(msg)  # exec 没有返回值

import os
# print(hash([12,3]))   unhashable type: 'list'
print(callable(l1))  # 类 模块 否则都是错的
print(callable(os))
print(help(callable))

print(complex(1,2))
print(hex(5))
print(oct(8))
print(bin(8))
print(int('0xA345',0))
print(int('0o7345',0))
print(int('0b1010',0))

print(divmod(5,7))
print(round(2.12324,4))
print(pow(2,3,4))
# encode和bytes只是 适合可哈希的可迭代对象
msg = 'slgsogha'
print(bytes(msg,encoding = 'gbk'))
print(msg.encode('gbk'))
t=msg.encode('gbk')
print(t.decode('gbk'))

print(ord('中'))
wh =ord('中')
print(chr(wh))

print(repr(msg))

print(sum([1,2,3],10))

# min max map filter sorted reversed  zip abs  reduce

from functools import reduce
print(reduce(lambda x,y:pow(y,x) , [1,2,3]))


# filter / map / reduce函数的作用分别是什么？
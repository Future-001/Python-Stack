"""
今日大纲：
    基础数据类型的补充
    数据类型之间的转换
    编码的进阶

昨日内容回顾：
    id id ==
    代码块：一个文件，函数，模块，交互式界面的一行代码
    同一代码块之间的缓存机制：
            字典，重用， int bool 几乎所有字符串，
            节省空间，提升性能
    不同代码块之间的缓存机制：小数据池
            -5~256   一定规则的字符串。 bool

    集合：
            列表去重
            关系测试： 交并差

    深浅copy:
            浅copy: 在内存中开辟一个新的空间，存放copy的对象，但是里面的元素采用和原对象中的元素共用一个内存地址。
            深copy： 在内存中开辟一个新的空间，存放copy的对象，对于可哈希的数据类型，共用一个内存地址，不可哈希的数据使用不同地址。


数据类型的补充：
    str:
        .capitalize()  首字母大写，其余变小写
        .swapcase()    大小写翻转
        .title()       每个 单词 的首字母大写。
        .center(width,fillder)    默认填充物空格
        .find(element)   通过元素找索引，找不到就返回-1.txt
        .index(element)   通过元素找索引，找不到就报错

    tuple:
        元组里面只有一个元素且没有逗号，不是元组，就是里面数据的数据类型。
        .count()     计数
        .index()      通过元素名去找索引

    list:
        count pass
        .index(element)    通过元素找索引
        .sort(reverse=False)   排序，从大到小。      默认从小到大
        .reverse()              列表的反转
        +    字典的相加。直接进行加法
        *    列表与数字相乘，就是复制几次、

        li =[10] 超出索引  li = [10:]  切片就不会出错
        切片 倒序 思维置换删除法，索引处要删除的元素，在删除
        循环一个列表时，最好不要改变列表的大小，会影响索引对应元素的数值。就算是利用 for 循环索引，其实也是一种索引取值

    dict 的补充，：
        .update(element)  增加一个元素，迭代着增加   既能增又能改  更新，有则改之，无则增加
        dict.fromekeys('键名',键值) 来自键，      将键名迭代着增加进入字典，作为键名，将键值作为其中每个键名的键值。
                坑： 值共有一个， 一定要注意，这个是共用一个，共用一个，共用一个。。。。。。。
                    dic=dict.fromekeys([1.txt,2,3],[])
                    dic[1.txt].append(666)
                    print(dic)

        循环一个字典时，如果改变这个字典的大小，就会报错。
        dic = {'k1':1.txt,'k2':2,'k3':3,'k4':4}   将其中含有k 的键值对全都删除
                for i in dic.keys():   但是如果将  list(dic) 不会出错。 就是强转化成一个列表，和原来的字典无关，就能删除。
                    if 'k' in i:
                        del dic[i               #  dictionary changed size during iteration

            另一个种方法就是：
            li = []
            for i in dic:
                if 'k' in i:
                    li.append(i)
            for i in li:
                dic.pop(i)

数据类型之间的转换：
        所有的数据都能转换为 bool数值， 0 '' {} set()

编码的进阶：
    ASCII  GBK Unicode  utf-8
    不同的编码之间能否相互识别？   不能

    数据在内存中全部是以 Unicode 编码的（全，除去bytes），但是当你的数据用于网络传输或存储到硬盘中，必须是以非Unicode编码，也就是bytes类型。
    将 gbk   编码转换为 utf-8 都是通过 unicode 进行的，  ，decode，encode
    bytes:
            内存中的编码方式。非 Unicode   # utf-8
            b`nheool'  就是在前面加上一个 b
            操作的方式与字符串基本一致。。   但是，主要用于中文，中文不一致。
                                s1='中国'
                                b=b'中国'  这样是错误的
                                b=s1.encode('utf-8')


    str------------------> bytes
                .encode('utf-8')

    bytes------------------> str
                 .decode('utf-8')   用什么转换的，就用什么转化回去。

    gbk--------------------> utf-8
                先转换为 unicode然后在转化为 utf-8


"""

print('==============================数据类型的补充===================================')
print('=================str===============')
s='fial2to3 d5o 56som3ething 3Yse'
print(s.capitalize())        # 首字母大写
print(s.swapcase())             # 大小写翻转
print(s.title())                  # 每个单词的首字母大写
print(s.center(40,"*"))
print(s.index('n'))    #  .index('element',start,end)
print(s.find('name'))  # 都是根据元素去找索引，但是这个找不到返回-1.txt，index找不到报错


print()
print('=================tuple===============')
s=(1,2,54,'time',[1,7,4],{'name':'kevin','pwd':'1234'})
print(s.index(1))
print(s.count(1))

print()
print('================list===============')
l1=list(['time','kevin','美女'])
l1.reverse()
print(l1)
l1.sort(reverse=False)
print(l1)
print(l1.index('time'))

l2=[1,2,45,7,3]
print(l1+l2)
print(l2*3)

print()
print('=================列表中的面试坑===============')

import random
l1=[]
i=0
while i<10:
    li = random.randrange(120)
    l1.append(li)
    i+=1
print(l1)
#  将索引为奇数的元素删除，li只是举个例子，不让一行一行删。
# 正常思路：
# 先将所有的索引列出来，加以判断。 index%2==1.txt    但是一个错误的点，删除之后次序就已经变化了，每一次的index对应的元素不一致了。

# 最简单的，按照切片去删除。

del l1[1::2]
print(l1)
# 倒叙删除元素。
li=[11,22,33,44,55,66,77,88]
for i in range(len(li)-1,-1,-1):
    li.pop(i)
print(li)
# 思维置换： 将原列表中索引为偶数的数值取出来放在另一个列表中。

print()
print('=================字典===============')
dic = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4,'name':234}
print(list(dic))
dic2=dict.fromkeys(['迭代','着','增加'],1234)
print(dic2)

print(dic2.setdefault('修改','数值'))
print(dic2)
dic2['迭代']='共用一个数值,但是我们这里是从单个元素指向的地址进行了修改'
print(dic2)

dic=dict.fromkeys([1,2,3],[])
dic[1].append(666)
print(dic)
print()

dic2.update(dic)
print(dic2)
print()

print('=================列字典修改中的面试坑===============')
dic = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4,'hello':'world'}
# for i in dic.keys():
#     if 'k' in i:
#         del dic[i]                     #  dictionary changed size during iteration
# print(dic)

for i in list(dic):
   if 'k' in i:
       del dic[i]
print(dic)

dic = {'k1': 1, 'k2': 2, 'k3': 3, 'k4': 4,'hello':'world'}
l1 =[]
for i in dic:
    if 'k' in i:
        l1.append(i)
print(l1)

for i in l1:
    dic.pop(i)
print(dic)


print()
print('=================编码的进阶===============')
s1='中国'
s2=b'name'
print(s2,type(s2))
b=s1.encode('utf-8')                # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(b,type(b))

g=s1.encode('gbk')
print(g,type(g))
b1=b'\xd6\xd0\xb9\xfa'
s2=b1.decode('gbk')
print(s2)
b2=s2.encode('utf-8')
print(b2)


"""
v = {'k1':'v1'}
# 判断v是不是字符串？
if type(v) == str:
    print('v是字符串')
elif type(v) == dict:
    print('v是字典')
elif type(v) == list:
    print('v是列表')
elif type(v) == tuple:
    print('元组')
elif type(v) == set:
    print('集合')
"""


# 4。车牌区域划分结合以下车牌，根据车牌提供的信息，分析出各省的车牌持有量
cars = ['鲁A3244A','鲁B123333','京B345346M','黑C23434','黑V934847','沪A2348905']
local ={'沪':'上海','京':'北京','黑':'黑龙江','鲁':'山东'}
result = {}
# for i in local:
#     count=0
#     for j in cars:
#         if i in j:
#             count+=1.txt
#             num[local[i]]=count
# print(num)

# 思想真的超级重要，没有就增加元素。
for i in cars:
    if local[i[0]] not in result:
        result[local[i[0]]]=1
    else:
        result[local[i[0]]]+=1
print(result)
# 结果 {山东2，黑龙江2 京1 沪 1.txt}

dic = {}
#  只针对本题的一种方法   .get()
for i in cars:
    dic[local[i[0]]]=dic.get(local[i[0]],0)+1
print(dic)
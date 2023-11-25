"""
=========================================  今日大纲 =========================================
JavaScript object notation： Java脚本兑现标记语言
已经成为了一种简单的数据交换格式，所有数据都转换为了字符串类型

 但是 python 中 set 不支持

序列化模块：
            结构化数据： 一个数据有很多方法在背后支撑
            线性数据：  数据之间没有引用关系

序列化过程： 将内存中结构化的数据，转换为 字节，用以保存在文件或者通过网络传输，（拆分）
反序列化过长：  从文件，网络中获取的数据 转换为内存中结构化的数据（组合）
区别方法： 数据是从内存中来，还是存储到内存中去

json:  将数据转化为字符串，用于存储或者网络传输，  序列化不太彻底，不是字节，
import json
    jsom.dumps(obj)  将一个对象，转换为 json 格式的字符串序列化再次放到内存当中，此时放的是 字符串类型 是不太彻底的序列化
                    元组序列化后 变成了 列表了。 字典的话就是变成了 字符串类型
                    不是所有的数据类型都可以 序列化

    对文件 都去掉 s 就可以了,dupms 和 loads 也可以写入文件，只是参数不同 ，需要打开文件 先 序列化，然后再写
    json.dump(obj,fp)    用于： 将 json 结果写到文件中  fp 是文件操作符
                        dump 直接对文件进行 写入的操作

    反序列化： 将网络 文件 的内容 存储 到内存
    json.loads(obj)   元组经过序列化 再次反序列化 转换只能得到列表了
                      也可以操作文件，将文件 先读取出来，然后进行反序列化

    从文件中反序列化： 直接对文件内容进行反序列化
    json.load(fp)   从文件句柄中将 (没有 obj) 读取了 文件的全部内容
                json 只能一次写 ，一次 读   注意，一定要注意，只能一次写一次读取，
                当然，使用了其他方式可以 一次读写
                ：  将需要序列化的对象，利用文件的write 方法， 把多次序列化后的 json 字符串
                            f.write(json.dump((1.txt,2,3)+'\n')
                    反序列化： 按行读取的方式
                            json.loads(f.readline().strip())


#  一次性写入文件多个数据， dump 和 Load 一定是不行的，因为他们写入能成功，但是读取不出来了，无论是
# 采用  loads  load 都读不出来，因为中间有 json 格式的结束符，你无法进行转换，一定只能用 dumps loads
# 写入和读取多行数据

open里面的 mode 模式  t  模式，指的是文本模式
============================================================================================================

pickle : 最彻底的 序列化方式
        将python中 所有的 所有的 数据类型 转换为 字节串 （字节串 b  字节了）
        或者 将字节串转换为 python 中的数据类型 （反序列化）
        可以保存元组的数据类型，set 的也可以

        也是  .dumps(element)    .dump(element,fp)  序列化后写入文件,
        .loads(element)    .load(fp,element)     反序列化后 读取数据
        注意一个点：  因为 pickle 他的模式一定是 wb 字节模式的，
        还有一个点： 对于 dump 和 load :   json 只能一次写一次读，但是 pickle 可以多次写多次读，每次读取一段数据
        dumps loads 只能用于网络传输,不能用于写入文件，

最常用的场景：  一次写一次读取： 不然可能出错了啊：  因为 for 的时候，取了一整行，建议用 for in range()

json 和 pickle 区别：
        json 不是所有的数据类型都可以序列化
                不能多次对同一个文件序列化
                可以跨语言，
        pickle: 所有类型都可以序列化， 都序列化为 字节
                可以对多次对文件序列化
                不能跨语言

==============================================================================================================
hashlib:  模块  封装一些用于加密的 类。
        dir(hashlib)        dir 查看一个模块当中有哪些可用的方法或者属性：

        加密的目的： 用于判断和验证，而并非解密
        特点： 将一个大的数据切分为不同块，分别对不同的块进行加密，再汇总的结果，和直接对整体数据加密的结果是一致的
             单向加密： 不可逆（但是现在破解了）
             原始数据的一点小的变化，将导致结果得非常大差异，‘雪崩’

        加密算法的流程，以  md5 为例：
        md5 加密算法：  m=hashlib.md5()   获取一个加密对象
                      m.update('element'.encode('utf-8')    利用  .update(element)   对加密对象进行加密   因为中文无法 b' xxx'
                      res = m.hexdigest()    通过 .hexdigest()   获取加密的结果（字符串）   .digest()   获取到结果（字节串 ）

        可以调用同一个加密方法 对不同元素进行加密 ；

应用：  验证： 用另一个数据加密的结果 和 第一次加密的结果对比， 如果结果相同，证明原文相同。

不同加密算法： 实际上就是 加密的 结果得长度不同，
创建加密对象时 ： 可以指定参数，多次加密称为  salt   就是说  hashlib.md5(b'xxx')  == 先 md5 然后 update(b'xxx')

======================================================================================================
collections :  定义了一些常用的 子 类   （常用的容器类）

namedtuple()   : 命名元组， 多了一个 named  给他起名了，本身 tuple 就是没有名字，是引用，这样命名之后可以  . 属性方式 引用元素
                aaa = namedtuple('可以作为要创建的 元组类的 名称的一些描述信息。', 元组类所含有的参数)    第一个参数不能有空格
                        aaa 是真正的类名，  aaa = namedtuple('AAA_tuple',['width','length'])
                                         r = aaa(15,9)
                                         print(r.width,r.length)
                        优点： 更直观知道元组里面的元素啊。

defaultdict():  默认值字典
                d = defaultdict(函数名, adc=222 等创建函数的方式)
                一但去获取一个 没有定义的东西，那么，会将 其 和默认值（一般是返回值）添加到字典当中。
                当创建一个字典的时候，

Counter()   计数器  返回值是一个字典，
            计算可迭代对象中每个元素的出现的次数， 还可以指定参数 ，具体看看 .
"""

import json
print(json.dumps(10))
print(json.dumps(dict(name=11,ta='23')),type(json.dumps(dict(name=11,ta='23'))))

print(json.dumps((1,2,3)))  # 元组会被转化为 列表
a = 'sghs,你在哪里呢'
b = json.dumps(a,ensure_ascii=False)   # ensure_ascii 确保中文正常显示
print(b)
print(json.loads(b))
print(repr(b),type(b))

dic = dict(one=1,two=2,three=3)
dic1 = json.dumps(dic)
dic2 = json.loads(dic1)
print(dic1,type(dic1))
print(repr(dic1))
print(dic2)

f = open('序列化.txt',mode = 'wt',encoding = 'utf-8')
json.dump(dic1,f)         # 写入成功了，但是读取不出来了，，，，，，
json.dump(b,f)
f.flush()
f.close()
#  一次性写入文件多个数据， dump 和 Load 一定是不行的，因为他们写入能成功，但是读取不出来了，无论是
# 采用  loads  load 都读不出来，因为中间有 json 格式的结束符，你无法进行转换，一
# 定只能用 dumps loads 写入和读取多行数据 ，就算你换了 dump(obj+'\n',fp) 但是 load 是直接对文件操作的，不是换行，所以也不行


f1 = open('序列化.txt',encoding = 'utf-8')
s = f1.read()
print(s,len(s),s[40:45])
# ss = json.loads(s)   # 这里难怪读取不出来了，因为有 json 的结束符，dump 和 load 搭配，一定只能读写一行，多了都不行
# print(ss,type(ss))
# json.dump(b,f)
f1.close()

#  如果要进行多行读写
dic1 = {'username':'alex'}
dic2 = {'username':'kevin'}
dic3 = {'username':'mette'}
f = open('多行序列化读写.txt',mode = 'wt',encoding = 'utf-8')
a = json.dumps(dic1)
f.write(a+'\n')
a = json.dumps(dic2)
f.write(a+'\n')
a = json.dumps(dic3)
f.write(a+'\n')

# 直接写，不加 换行符的时候，这样也是读取不出来的，换行符呢，没办法

# a = json.dumps(dic1)
# f.write(a)
# a = json.dumps(dic2)
# f.write(a)
# a = json.dumps(dic3)
# f.write(a)

f.flush()
f.close()

f1 = open('多行序列化读写.txt',encoding = 'utf-8')
for line in f1:
   # 直接写，不加 换行符的时候，这样也是读取不出来的，换行符呢，没办法
    s =json.loads(line)
    print(s,type(s))

f1.close()
# =======================================================================================
import pickle
a1 = [1,2,3,]
dic1 =dict(so=1,s=2,osg=4)
dic = pickle.dumps(dic1)
a = pickle.dumps(a1)
print(dic ,a )   # 转化为字节串
print(pickle.loads(dic),pickle.loads(a))

f = open('pickle序列化.txt',mode='wb')
pickle.dump(dic1,f)
pickle.dump(a1,f)
f.close()

f = open('pickle序列化.txt',mode='rb')
print('这样能认识结束符：')
print(pickle.load(f))
print('就是这样的')
print(pickle.load(f))
f.close()

# ============================================================================================
import hashlib

# 见 DAY 17

# ============================================================================================
import collections
abc ='this is a goog idea'
print(collections.Counter(abc))

a = collections.namedtuple('thie_is_a_tuple',['width','length'])   # 忘记了，描述里面不能有空格
b = a(12,34)
print(b.width,b.length)

d = collections.defaultdict(lambda : 'key error')  # 里面的参数时函数名
result = {'name':'alex','as':[1,2,3]}
print(d['key2'])   # 键不存在，那么就增加
print(d)





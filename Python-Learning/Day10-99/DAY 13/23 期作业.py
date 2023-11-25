# 看代码分析结果
func_list = []
for i in range(10):
    func_list.append(lambda :i)    # func_list = [0,1.txt,2,,,,9] 大错特错,这里列表中是函数名,是地址
v1 = func_list[0]()
v2 = func_list[5]()
print(v1,v2)
# 输出的是 我还真的不理解...这里为什么是这个呢?不是很理解,一句话函数,

# 看代码分析结果
func_list = []

for i in range(10):
    func_list.append(lambda x:x+i)

v1 = func_list[0](2)
v2 = func_list[5](1)
print(v1,v2)
# 输出的是:  我们的输出数值是 11 10

# 看代码分析结果
func_list = []

for i in range(10):
    func_list.append(lambda x:x+i)

for i in range(0,len(func_list)):
    result = func_list[i](i)
    print(result,end=' ')
# 输出是:  0 2 4 6 8 10 12 14 16 18

print()
# 看代码写结果（面试题）：
def func(name):
    v = lambda x:x+name
    return v

v1 = func('太白')   # 这里只是返回了一个地址,还没有被执行呢.  里面的参数是  name = 太白
v2 = func('alex')    # 这里同理
v3 = v1('银角')       # 注意二者指向了同一个地址, 传入了参数是 x = 银角
v4 = v2('金角')
print(v1,v2,v3,v4)
# 输出是:  一个地址, 一个地址, 银角太白 金角 Alex

print()
# 看代码写结果【面试题】
result = []
for i in range(10):
    func = lambda : i      #  func 是一个地址,函数名.注意：函数不执行，内部代码不会执行。
    result.append(func)   # result里面有10个地址,但是执行的都是 func函数的功能

print(i)   # i 肯定是 9 啊
print(result)  # 九个相同的地址呢.
v1 = result[0]()   # 输出的是9
v2 = result[9]()      # 还是9
print(v1,v2)
# 输出是:

print()
# 看代码分析结果【面试题】
def func(num):
    def inner():
        print(num)   # 闭包
    return inner

result = []
for i in range(10):
    f = func(i)
    result.append(f)         # 降低至加入了列表,但是,但是,但是,由于闭包,自由便来给你不会消失,那么,会导致,后面 Num
# 后面 Num的数值被修改了,
print(i)  # 9
print(result)  # 全是地址,而且不同呢
v1 = result[0]()     # 为什么是 0 ,因为 每次执行,都对每个 f 创建了一个不同的 Num,
# 由于 num不能被外部修改,那么,相当于创建了 9 个 num 而且互不影响
v2 = result[9]()
print(v1,v2)     # 输出了  NONE NONE 函数已经被执行完了...没有返回值了
# 输出是:

# 看代码写结果【新浪微博面试题】
print()
def func():
    for num in range(10):
        pass   # 此时 i = 9
    v4 = [lambda :num+10,lambda :num+100,lambda :num+100,]  # 里面都是地址哈,注意了
    result1 = v4[1]()  # 109
    result2 = v4[2]()   # 109
    print(result1,result2)
func()

print()
# 请编写一个函数实现将IP地址转换成一个整数。【面试题，较难,可以先做其他题】
#
# 如 10.3.9.12 转换规则为二进制：
#         10            00001010
#          3            00000011
#          9            00001001
#         12            00001100
# 再将以上二进制拼接起来计算十进制结果：00001010 00000011 00001001 00001100 = ？
print()
IP = '10.3.9.12'
sum = ''
IP_TEM = IP.split('.')
for i in IP_TEM:
    port = bin(int(i))[2:]
    print(i,port)
    sum+= port.zfill(8)
    print(sum)
print(int('0b'+sum,0))
# 都完成的做一下作业（下面题都是用内置函数或者和匿名函数结合做出）：


# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
name=["oldboy",'alex','wusir']
print(list(map(lambda i:i+'sb',name)))
def add_sb(i):
    return i+'sb'
print(list(map( add_sb,name)))


# 用map来处理下述l，然后用list得到一个新的列表，列表中每个人的名字都是sb结尾
l = [{'name':'alex'},{'name':'y'}]
print(list(map(lambda i:i['name']+'sb',l)))

# 用filter来处理,得到股票价格大于20的股票名字
shares={ 'IBM':36.6, 'Lenovo':23.2,'oldboy':21.2,'ocean':10.2,}
print(list(filter(lambda i:shares[i]>20,shares)))

# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中结果：list一下[9110.0, 27161.0,......]
#
portfolio = [
  {'name': 'IBM', 'shares': 100, 'price': 91.1},
{'name': 'AAPL', 'shares': 50, 'price': 543.22},
{'name': 'FB', 'shares': 200, 'price': 21.09},
{'name': 'HPQ', 'shares': 35, 'price': 31.75},
{'name': 'YHOO', 'shares': 45, 'price': 16.35},
{'name': 'ACME', 'shares': 75, 'price': 115.65}]
print(list(map(lambda i:i['shares']*i['price'],portfolio)))
# 还是上面的字典，用filter过滤出单价大于100的股票。
i = list(filter(lambda i:i['price']>100,portfolio))
for j in i:
    print(j['name'],sep = '&&',end=' ')

# 有下列三种数据类型，
print()

l1 = [1,2,3,4,5,6]
l2 = ['oldboy','alex','wusir','太白','日天']
tu = ('**','***','****','*******')
#  写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# [(3, 'wusir', ''), (4, '太白', '*******')]这样的数据。
print(list(filter(lambda i:i[0]>2 or len(i[2])>3, list(zip(l1,l2,tu)))))

#  7. 有如下数据类型(实战题)：
#
l1 = [ {'sales_volumn': 0},{'sales_volumn': 108},{'sales_volumn': 337},
{'sales_volumn': 475},{'sales_volumn': 396},{'sales_volumn': 172},
{'sales_volumn': 9},{'sales_volumn': 58},{'sales_volumn': 272},{'sales_volumn': 456},
{'sales_volumn': 440},{'sales_volumn': 239}]

#  将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
print(sorted(l1,key = lambda i:i['sales_volumn'] ))


print(f'\n感觉比较难啊')
# 求结果(面试题)
v = (lambda :x for x in range(10))   # 生成器表达式
print(v)    # v里面一定要记住，他是十个地址，但是这个地址 还没有被执行， 一旦执行后，里面输出的都是 9
# print(v[0])      为什么这两行错了呢？因为这是一个生成器。生成器可以对他进行取值，但是，
# print(v[0]())
print(next(v))  # 输出的肯定是9
print(next(v)())   # 输出还是 9


print()
map(str,[1,2,3,4,5,6,7,8,9])    # map返回的是一个迭代器，经送进去变成了字符串，但是是在迭代器里面的。
u = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(u,type(u[0]))
# 输出是什么? (面试题)


# 求结果：（面试题，比较难，先做其他题）
def num():
	return [lambda x:i*x for i in range(4)]  # 列表推导式，里面存储了 四个地址。一旦执行，输出的i 都是 4 ，最后的都是4
print([m(2)for m in num()])   # 输出的是 ：这里输出的是 一个列表  [6,6,6,6]
# 返回的是一个列表啊， 注意了，和刚才那个题的区别，可以去看看 错题里面的东西



print()
# 有一个数组[34,1.txt,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数的总和（上面数据的没有重复的总和为1+2=3)(面试题)
# 突然想到一个简化部分重复数字的方法：   set 但是还会保留部分元素啊
# gpt 提供的一个思路可以，记录下每个数字的出现次数，然后去计算，最终用列表得出一个数值

# l1 = [34,1.txt,2,5,6,6,5,4,3,3]
# l2= []
# def num(i):
#     for j in l1:
#         if len(str(j))==1.txt:
#             if l1.count(j)==1.txt:
#                 l2.append(i)
#                 return i
#         else :
#             count = True
#             for k in str(j):
#                 if l1.count(int(k))==0:
#                     pass
#                 else:
#                     count = False
#             if count == True:
#                 l2.append(i)
#                 return i

# for j in l1:
#     if len(str(j))==1.txt:
#         if l1.count(j)!=1.txt:
#             l1.remove(j)
#     else :
#         count = True
#         for k in str(j):
#             if l1.count(int(k))!=0:
#                 l1.remove(int(k))
#                 l1.remove(j)
#                 break
# print(l1)
#
# # print(list(filter(num,l1)))
# # print(list(map(num,l1)))

# 第一版
print(list(filter(lambda i:l1.count(i)==1,l1)))
# 第二版


# 为什么偏偏忘记了使用闭包呢？？？？ 难道是 filter  函数就忘记了？


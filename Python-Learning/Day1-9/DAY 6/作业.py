# 1.txt.列举你了解的字典中的功能（字典独有）。
#  增加： 直接改， .setdefault()    .update()
#  删除：  .pop()   del   .clear()
#  修改：   索引修改：，
#  查：    索引查询，  for    .get(键名)
#    其他功能：     dic.keys()   dic.values()   dic.items()

# 2.列举你了解的集合中的功能（集合独有）。
#   .add   .update     .discard   .pop   .remove()     & intersection()    | .union()   -   .difference()

# 3.列举你了解的可以转换为 布尔值且为False的值。
#   ''     0

# 4. 请用代码实现
info = {'name': '王刚蛋', 'hobby': '铁锤'}
# 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出。
while 1:
    choice=input('请输入你的选择 ： (name/hobby) >>> ')
    if choice in info:
        print(info[choice])
        break
    else:
        print('键不存在')
# 循环提示用户输入，根据用户输入的值为键去字典中获取对应的值并输出（如果key不存在，则获取默认“键不存在”，并输出）。
# 注意：无需考虑循环终止（写死循环即可）

# 5.请用代码验证"name"是否在字典的键中？
info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}  #  ...100个键值对
if 'name' in info.keys():
    print('name 在字典中 ')
while 1:
    data=input('请输入姓名>>> ')
    val = info.get(data,'键不存在')
    print(val)

# 6.请用代码验证"alex"是否在字典的值中？
info = {'name': '王刚蛋', 'hobby': '铁锤', 'age': '18'}  #  ...100个键值对
if 'alex' in info.values():
    print('在字典中 ')
#
# 7.有如下
v1 = {'武沛齐', '李杰', '太白', '景女神'}
v2 = {'李杰', '景女神'}
#       请得到 v1 和 v2 的交集并输出
print(v1 & v2  ,v1.intersection(v2))
#       请得到 v1 和 v2 的并集并输出
print(v1.union(v2),  v1 | v2)
#       请得到 v1 和 v2 的 差集并输出
print(v1-v2, v2.difference(v1))

# 8.循环提示用户输入，并将输入内容追加到列表中（如果输入N或n则停止循环）
li = []
while 1:
    ad = input('请输入内容： （N或n停止输入）>>> ')
    if ad.upper()=='N':
        break
    else:
        li.append(ad)
print(li)

# 8.循环提示用户输入，并将输入内容添加到集合中（如果输入N或n则停止循环）
s = set()
while 1:
    ad = input('请输入内容： （N或n停止输入）>>> ')
    if ad.upper()=='N':
        break
    else:
        s.add(ad)
print(s)

# 9.写代码实现
v1 = {'alex', '武sir', '肖大'}
v2 = []
# # 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
while 1:
    i = input('请输入你想要添加的输入：(输入N或n则停止) >>> ')
    if i.upper()=='N':
        break
    elif i in v1:
        v2.append(i)
    elif i not in v1:
        v1.add(i)    #  update 是迭代着增加
        # v1=v1.add(i)是错的，因为返回值是None
print(v1,v2)

# 11.判断以下值那个能做字典的key ？那个能做集合的元素？
#   字典的key一定是可哈西德，集合的元素也是可哈希的
# 1.txt
# - 1.txt
# ""
# None
# [1.txt, 2]
# (1.txt, )
# {11, 22, 33, 4}
# {'name': 'wupeiq', 'age': 18}

# 12，is 和 == 的区别？
#  is 是比较内存地址是否相等 ， ==比较的是数值是否相等。数值相等 地址不一定相等。

# 13.type使用方式及作用？
#  type用于查看数据类型。

# 14.id的使用方式及作用？
#  id 查看元素在内存中的存储地址。

# 15.看代码写结果并解释原因
#  都是True.数值相等。==       由于同一代码快的缓存机制。  （很快打脸了，。。。。第二个是错的）  注意一下缓存机制针对的具体细则： 一定是可哈希的。。。。。。

v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = {'k1': 'v1', 'k2': [1, 2, 3]}
# 首先，对比两个字典，数值是一样的，但是，由于字典是可变的，不满足 同一代码块下的缓存机制。所以，首先二者的地址一定不同，
# 其次 ，对于字典中的可哈希的元素，那么，他们最终指向的地址是一致的。对于不可哈希的元素，指向的地址也不一致。
# 谈到这里，那么注意一下深浅copy，对于不可哈希的变量，那么里面的不可哈希的元素，指向的地址： 深copy 是不同的， 但是浅copy是一致的，可以同步修改。
result1 = v1 == v2
result2 = v1 is v2
print(result1)
print(id(v1),id(v1['k1']),id(v1['k2']),id(v2),id(v2['k1']),id(v2['k2']))
print(result2)           # 对比两个字典的存储地址。 （这是深copy）一定要注意，对于可变的数据类型，不可哈希，那么他们的地址一定是不同的。
print()

# 16.看代码写结果并解释原因
# 这样的话，两个都是True,因为直接赋值，相当于用两个变量指向了同一个地址段。
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = v1

result1 = v1 == v2
result2 = v1 is v2
print(result1)
print(result2)

# 17.看代码写结果并解释原因
#
v1 = {'k1': 'v1', 'k2': [1, 2, 3]}
v2 = v1

v1['k1'] = 'wupeiqi'
print(v2)

# 18.看代码写结果并解释原因
# 为什么v2不变呢，因为v2里面的 v2[-1.txt]还是指向原来的存储地址，我们只是改了v1指向的存储地址。元素可哈希，我们只是简单改了v1的地址，但是对于v2没有影响。
v1 = '人生苦短，我用Python'
# print(id(v1))
v2 = [1, 2, 3, 4, v1]
v1 = "人生苦短，用毛线Python"
print(v2)
# print(id(v2[-1.txt]),id(v1))
#  改一下：
v2[-1]=v1
print(v2)
# 给给我们的提示，在利用不可哈希的数据类型存储数据时，如果存储变量。一定要注意，多关注一下存储机制以及深浅copy

# 19.看代码写结果并解释原因
#
info = [1, 2, 3]
userinfo = {'account': info, 'num': info, 'money': info}

info.append(9)
print(userinfo)   # 肯定发生变化了，因为指向的地址的内容发生变化了。

info = "题怎么这么多"
print(userinfo)             # 还是不变，因为指向的地址不变

# 19.看代码写结果并解释原因
#
info = [1, 2, 3]
userinfo = [info, info, info, info, info]

info[0] = '不仅多，还特么难呢'
print(info, userinfo)          # 第一个元的肯定改了，第二个元素也改了，因为指向的地址的内容发生了变化。

# 20.看代码写结果并解释原因
#
info = [1, 2, 3]
userinfo = [info, info, info, info, info]

userinfo[2][0] = '闭嘴'
print(info, userinfo)           # 第一个发生了变化，第二个也发生了变化，总而言之，就是地址内的内容发生了变化。全都改了。

# 21.看代码写结果并解释原因
#
info = [1, 2, 3]
user_list = []
for item in range(10):
    user_list.append(info)

info[1] = "是谁说Python好学的？"

print(user_list)                # 十个全变了，因为里面的地址变了

# 22.看代码写结果并解释原因
#
data = {}
for i in range(10):
    data['user'] = i
print(data)        # 最后输出了9，因为里面存储的地址里面的内容都变了，同时，

# 23.看代码写结果并解释原因
#
data_list = []
data = {}
for i in range(10):
    data['user'] = i
data_list.append(data)
print(data)

# 24.看代码写结果并解释原因
#
data_list = []
for i in range(10):
    data = {}
data['user'] = i
data_list.append(data)
print(data_list)

# 25. 我也来整个活儿：
data=[]
dic={}
for i in range(10):
    dic['user']=i
    data.append(dic)
print(data)
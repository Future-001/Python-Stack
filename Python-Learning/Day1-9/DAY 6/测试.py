# import copy
#
# li=[1.txt,2,3,[22,33]]
# li2=copy.deepcopy(li)
#
# print(li,id(li),li2,id(li2))
# li[-1.txt].append(666)
# print(li,id(li),li2,id(li2))
#
# print(li[-1.txt],id(li[-1.txt]),li2[-1.txt],id(li2[-1.txt]))
# print(li[0],id(li[0]),li2[0],id(li2[0]))
#
# li[0]='修改后'
# print(li[0],id(li[0]),li2[0],id(li2[0]))

# v1 = {'k1': 'v1'}
# v2 = {'k1': 'v1'}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(id(v1),id(v2))
# print(result2)           # 对比两个字典的存储地址。 （这是深copy）一定要注意，对于可变的数据类型，不可哈希，那么他们的地址一定是不同的。
#

# v1 = {'k1': 'v1', 'k2': [1.txt, 2, 3]}
# v2 = v1
#
# v1['k2'][0] = 'wupeiqi'
# print(v2)

# v1 = '人生苦短，我用Python'
# v2 = [1.txt, 2, 3, 4, v1]
#
# v1 = "人生苦短，用毛线Python"
#
# print(v2)
# v2[-1.txt]=v1
# print(v2)

# info = [1.txt, 2, 3]
# userinfo = {'account': info, 'num': info, 'money': info}
#
# info.append(9)
# print(userinfo)   # 肯定发生变化了，因为指向的地址的内容发生变化了。
#
# info = "题怎么这么多"
# print(userinfo)             # 还是不变，因为指向的地址不变

# info = [1.txt, 2, 3]
# userinfo = [info, info, info, info, info]
#
# info[0] = '不仅多，还特么难呢'
# print(info, userinfo)

# info = [1.txt, 2, 3]
# userinfo = [info, info, info, info, info]
#
# userinfo[2][0] = '闭嘴'
# print(info, userinfo)    # 第一个发生了变化，第二个也发生了变化，总而言之，就是地址内的内容发生了变化。全都改了。


# 21.看代码写结果并解释原因
#
# info = [1.txt, 2, 3]
# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1.txt] = "是谁说Python好学的？"
#
# print(user_list)

# 22.看代码写结果并解释原因
#
# data = {}
# for i in range(10):
#     data['user'] = i
# print(data)

# 23.看代码写结果并解释原因
#
# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
# data_list.append(data)
# print(data)

# 24.看代码写结果并解释原因
#
# data_list = []
# for i in range(10):
#     data = {}
# data['user'] = i
# data_list.append(data)
# print(data_list)

data=[]
dic={}
for i in range(10):
    dic['user']=i
    data.append(dic)
print(data)
# 1.txt.请列举所有数据类型中具有的方法并为每一个写一个示例【md文件】

# 今日作业
# 1.txt.看代码写结果
#   肯定是两个都加上6，因为v2中存放了v1的数据的地址，直接对该地址进行了数据改动
v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]

v1.append(6)
print(v1)
print(v2)

print()
# 2.看代码写结果
#  都输出带有222
v1 = [1,2,3,4,5]
v2 = [v1,v1,v1]

v2[1][0] = 111
v2[2][0] = 222
print(v1)
print(v2)

# 3.看代码写结果，并解释每一步的流程。
#  肯定是追加了6，7，8，9  指向了同一个地址，对那片地址中的元素进行了修改
v1 = [1,2,3,4,5,6,7,8,9]
v2 = {} # 空子典

for item in v1:
    if item < 6:
        continue
    elif 'k1' in v2:
        v2['k1'].append(item)
    else:
        v2['k1'] = [item]   # 这里增加了列表。
print(v2)

# 4.简述深浅拷贝？
# 深copy： 在内存中新开辟了一段存储空间，常量指向同一片存储空间，不可哈希变量指向不同的空间
# 浅copy 内存中新开辟了一段地址，其中的元素指向了同一片存储空间。如果对其中的可哈希变量畸形了修改，那么不是同步的，但是
#                   对与不可哈希内部的元素进行了修改，是同步的

# 5.看代码写结果
#  反思：两题都做错了，True
#  由于这是一个不可变的数据类型，在同一代码块的缓存机制中，他们使用了同一个内存地址。所有都是一致的
import copy

v1 = "alex"
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1 is v2)
print(v1 is v3)

# 稍微修改一下，应该就是 False
import copy

v1 = ["alex",'name']
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1 is v2,id(v1[0]),id(v2[0]))
print(v1 is v3,id(v3[0]))
# 6.看代码写结果
#
import copy

v1 = [1,2,3,4,5]
v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1 is v2)
print(v1 is v3)

# 7.看代码写结果
#
import copy

v1 = [1,2,3,4,5]

v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1[0] is v2[0])
print(v1[0] is v3[0])
print(v2[0] is v3[0])
#
# 8.看代码写结果
#
import copy

v1 = [1,2,3,4,5]

v2 = copy.copy(v1)
v3 = copy.deepcopy(v1)

print(v1[0] is v2[0])
print(v1[0] is v3[0])
print(v2[0] is v3[0])

# 9.看代码写结果
#
print()
import copy

v1 = [1,2,3,{"name":'武沛齐',"numbers":[7,77,88]},4,5]

v2 = copy.copy(v1)

print(v1 is v2)   # 肯定false

print(v1[0] is v2[0])  # True
print(v1[3] is v2[3])   # true

print(v1[3]['name'] is v2[3]['name'])   # true
print(v1[3]['numbers'] is v2[3]['numbers'])
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])

# 10.看代码写结果
#
print()
import copy

v1 = [1,2,3,{"name":'武沛齐',"numbers":[7,77,88]},4,5]

v2 = copy.deepcopy(v1)

print(v1 is v2)    # False

print(v1[0] is v2[0])    # true
print(v1[3] is v2[3])       # false

print(v1[3]['name'] is v2[3]['name'])    # true
print(v1[3]['numbers'] is v2[3]['numbers'])           # false
print(v1[3]['numbers'][1] is v2[3]['numbers'][1])         # true

# 补充题；
# 1.txt.输入一个数，判断它是不是水仙花数  每位的三次方加起来等于他
num = input('请输入一个纯数字>>> ')
count = 0
if num.isdecimal():
    for i in num:
       count+=int(i)**3
    if count == int(num):
        print('是水仙花数')
    else:
        print('NO')
else:
    print('输入有误，请重新输入')

#  2. 请用python代码实现 li=[['_','_','_'],['_','_','_'],['_','_','_'],['_','_','_']]
print()
print([['_']*3]*4)
# 用for很常规，不管了

#  3.请删除下面列表中含有 周 字的元素
print()
li =['周扒皮','周星星','周树人','黎明','周']
# 方法一：倒叙删除

# for i in range(len(li)-1.txt,-1.txt,-1.txt):
#     if '周' in li[i]:
#         li.pop(i)
# print(li)

# 方法二： 重建一个列表
l =[]
for i in li:
    if '周' in i:
        l.append(i)
for i in l:
    li.remove(i)
print(li)

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

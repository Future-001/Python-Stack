# 1.txt.请将列表中的每个元素通过 "_" 链接起来。
users = ['李少奇','李启航','渣渣辉']
print('_'.join(users))

# 2. 请将列表中的每个元素通过 "_" 链接起来。
users = ['李少奇','李启航',666,'渣渣辉']
# 注意到一个点，就是666不是字符串，所以不能直接 join
# print('不信我们看一下结果：',"_".join(users))   报错了
j=0
for i in users:
    users[j]=str(i)
    j+=1
print(users)
print('_'.join(users))
# 或者采用加法 s+=s+'_"+i 但是会多出一个_ 记得删除

# 3. 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
v1 = (11,22,33)
v2 = [44, 55, 66]
v2.extend(v1)  # 或者采用append
print(v2)
#
# 4.请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
v1 = (11,22,33,44,55,66,77,88,99)
v2 = [44,55,66]
v2.extend(v1[::2])
print(v2)
#
# 5.将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
# extend() 也是一种方法
info = {'k1':'v1','k2':'v2','k3':'v3'}
key_list = []
value_list = []
for k,v in info.items():
    key_list.append(k)
    value_list.append(v)
print(key_list,value_list)

print(list(info.keys()))
print(list(info.values()))
# 6.字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# a. 请循环输出所有的key
for i in dic.keys():
    print(i)
# b. 请循环输出所有的value
for i in dic.values():
    print(i)
# c. 请循环输出所有的key和value
for i,j in dic.items():
    print(i,j)
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic.setdefault("k4","v4")
print(dic)
dic['k5']='v5'
print(dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1']='alex'
print(dic)
# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
dic['k3'].append(44)
print(dic)
# g. 请在k3对应的值的第 1.txt 个位置插入个元素 18，输出修改后的字典
dic['k3'].insert(1,18)
print(dic)

# 7.请循环打印k2对应的值中的每个元素。
info = {
    'k1':'v1',
    'k2':[('alex'),('wupeiqi'),('oldboy')],
}
print(info['k2'],type(info['k2']))
for value in info['k2']:
    print(value,type(value))

# 8.有字符串"k: 1.txt|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1.txt,'k1':2....}
info={}
msg="k: 1.txt|k1:2|k2:3 |k3 :4"
for i in msg.split('|'):
   a,b=i.split(':')
   print(a,b)
   info[a.strip()]=int(b)
   info.setdefault(a.strip(),int(b))
print(info)

# 9.写代码
#
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
dic={'key1':[],'key2':[]}
li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
for i in li:
    if i>66:
        dic['key1'].append(i)
    else:
        dic['key2'].append(i)
print(dic)

# 10.输出商品列表，用户输入序号，显示用户选中的商品
# 商品列表：
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
# """
# 要求:
# 1.txt：页面显示 序号 + 商品名称 + 商品价格，如：
#       1.txt 电脑 1999
#       2 鼠标 10
# 	  ...
count=1
for i in goods:
    print(count,i['name'],i['price'])
    count+=1

"""
改进的版本：
for i in range(len(goods)):
    print(i+1.txt,goods[i]['name'],goods[i]['price'])
    
    
再次改进：
for index,dic in enumerate(goods):
    print(inedx+1.txt,dic['name']['price'])
"""

# 2：用户输入选择的商品序号，然后打印商品名称及商品价格

while 1:
    select=input('请输入你想选择的商品序号：(退出请按q)>>>')
    if select.isdecimal():
        if int(select) in range(len(goods)+1):
            print('你选择的商品是{}，价格为{}'.format(goods[int(select)-1]['name'],goods[int(select)-1]['price']))
            break
        else:
            print('输入错误，请重新输入')
    elif select.upper()=='Q':
        break
    else:
        print('输入错误，请重新输入')
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
# """
# 11.看代码写结果
#
v = {}
for index in range(10):
    v['users'] = index
print(v)
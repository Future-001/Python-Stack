#!/usr/bin/env python
# -*- coding:utf-8 -*-
""""""
# 1.txt.请获取 "刘伟达"
info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
print(info['name'])

# 2. 请输出所有键
info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
for i in info.keys():
    print(i)
print()

print(' way 2')
for i in info:
    print(i)

# 3. 请输出所有键和值

v = "1.txt+3"
a,b = v.split('+') # [1.txt,3]
print(a,b)

a,b = (1,3,)
print(a,b)

info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
for i in info.items():
    print(i)

for k,v in info.items():
    print(k,v)

# 3. 请输出所有键和值,并让用户输入 name/age/gender/hobby，根据用户输入输出对应的值。
info = {"name":'刘伟达','age':18,'gender':'男','hobby':'同桌'}
while 1:
    get = input('请输入你要查询的内容：（name/age/gender/hobby）>>>')
    # if (get in info.keys())=='True':
    if get in info:
        print(info[get])
        break
    else:
        print('非法输入，请重新输入！')

# 4. 给你一个空字典，请在空字典中添加数据: k1:1.txt,k2:2,k3:3
info = {}
info2={'k1':1,'k2':2,'k3':3}
info.update(info2)
print(info)
"""info['k1'] = "1.txt"
info['k2'] = 2
info['k3'] = 3
print(info)
"""

# 5. 给你一个空字典，请让用户输入：key，value，将输入的key和value添加到字典中。
info = {}
key=input('请输入键名：')
value=input('请输入值：')
temp=dict(key=value)
info.update(temp)
print(info)

# k = input('请输入key：')
# v = input('请输入value：')
# info[k] = v
# print(info)

# 6. 给你一个空字典，请一直让用户输入：key，value，将输入的key和value添加到字典中，直到用户输入 N ，则表示不再输入。
info = {}
while 1:
    key=input('请输入键名：')
    value=input('请输入值：')
    temp=dict(key=value)
    info.update(temp)
    print(info)
    select=input('是否继续？ y/n >>>')
    if select.upper()=='Y':
        continue
    elif select.upper()=='N':
        break
    else:
        print('非法输入！')
"""
info = {}
while True:
    k = input('请输入key：')
    if k == 'N':
        break
    v = input('请输入value：')
    info[k] = v
print(info)
"""

# 7. 请用代码实现
"""
    message = "k1|v1,k2|v2,k3|123......." # ,k3|123

    info = {'k1':'v1','k2':'v2','k3':'123'}
"""
message = "k1|v1,k2|v2,k3|123...."
message=message.strip('.')
for item in message.split(','):
    v1,v2=item.split('|')
    info[v1]=[v2]
print(info)

"""
info = {}
message = "k1|v1,k2|v2,k3|123"
for item in message.split(','): # ["k1|v1","k2|v2","k3|123"]
    v1,v2 = item.split('|')
    info[v1] = v2
print(info)
"""


# 8. 数据类型嵌套：int/bool/str/list/tuple/dict
li = [11,22,33,True,[11,2],(11,2,[11,22],33,),{'k1':'v1','k2':(11,22,3)}]
info = {
    'k1':'v1',
    'k2':True,
    'k3':1,
    'k4':(11,22,33),
    'k5':[11,22,33],
    'k6':{'kk':'vv'},
    1:{'kk':'vv'},
    False:{'kk':'vv'},
    # [11,2]:{'kk':'vv'}, # 不可哈希           unhashable type: 'list'
    # print('总结： 键一定要是不可变的（可哈希）的类型才能使用，不然出错了。')
    (11,2):{'kk':'vv'},
    # {'k1':'v2'}:{'kk':'vv'}, # 不可哈希
}

print(info)
for i in info.items():
    print(i)


data = [1, 2, {'k1': 1, 'k2': 2, 'k3': (11, 22, 33), 'k4': [1, (12, 3, 4), 2]}, 93]
# 获取3
print(data[-2]['k4'][1][1])
# 在k4对应的列表第0个位置插入一个
data[-2]['k4'].insert(0,9)
print(data)

# 9. 创建出一个用户列表，然后让用户输入用户名和密码进行登陆。
user_list = [
    {'user': 'alex', 'pwd': '123'},
    {'user': 'oldboy', 'pwd': '123'},
    {'user': 'lishaoqi', 'pwd': '1123'},
    {'user': 'liqihang', 'pwd': '123'},
    {'user': 'xxx', 'pwd': '123'},  # N
]
s=True
while se:
    name=input('请输入用户名:>>>')
    pawd=input('请输入密码：>>>')
    code='Nalc'
    your_code=input('请输入验证码')
    if your_code.upper()==code.upper():
        for i in range(len(user_list)):
            if user_list[i]['user']==name and user_list[i]['pwd']==pwd:
                print('登录成功！')
                s=False
                break
            elif i==len(user_list)-1:
                print('账号或密码错误')
    else:
        print('验证码错误 ')


"""
    user_list = [
        {'user':'alex','pwd':'123'},
        {'user':'oldboy','pwd':'123'},
        {'user':'lishaoqi','pwd':'1123'},
        {'user':'liqihang','pwd':'123'},
        {'user':'xxx','pwd':'123'}, # N
    ]

"""
# 构建用户列表

"""
user_list = []
while True:
    u = input('请输入用户名：') # N
    if u == "N":
        break
    p = input('请输入密码：')
    # user_info = {}
    # user_info['user'] = u
    # user_info['pwd'] = p
    user_info = {'user':u,'pwd':p}
    user_list.append(user_info)
"""

"""
user_list = [{'user': 'alex', 'pwd': '123'}, {'user': 'oldboy', 'pwd': '123'}, {'user': 'lishaoqi', 'pwd': '123'}]
username = input('请输入用户名：') # oldboy
password = input('请输入密码：') # 123
message = "登陆失败"
for item in user_list:
    if item['user'] == username and item['pwd'] == password:
        message = '登陆成功'
        break
print(message)
"""

# 10. 有序
# 有序：元组/列表
# 无序：字典（py3.6之后字典就是有序了）
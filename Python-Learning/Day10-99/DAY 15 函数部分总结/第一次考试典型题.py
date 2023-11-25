# 有一个列表入下：
l =[
    {'name':'张三','hobby':'抽烟'},
    {'name':'里斯','hobby':'睡觉',},
    {'name':'里斯','hobby':'看小说',},
    {'name':'张三','hobby':'打游戏',},
    {'name':'小二','hobby':'看西游记',},
    {'name':'张三','hobby':'看bilibili',},
    {'name':'小董','hobby':'金瓶梅',},
    {'name':'张三','hobby':'复联4',},
    {'name':'小董','hobby':'打篮球',},
]
# 将其转变为   l2= [{"name":"张三","hobby_list":['抽烟','打游戏','看bilibi‘，'复联4'},,,]这种类型
# 第一种，直接法
l1 = []
for i in l:
    for j in l1:
        if i['name'] in j['name']:
            j['hobby_list'].append(i['hobby'])
            break
    else:
        l1.append({'name':i['name'],'hobby_list':[i['hobby']]})
print(l1)

# 方法二  构建特殊的数据结构
'''
dic = {'alex': {'name’：‘zhangsan','hobby_list':[',,,,']}, ...........}
'''
dic = {}
for i in l:
    if i['name'] not in dic:
        dic[i['name']]={'name':i['name'],'hobby_list':[i['hobby']]}
    else:
        dic[i['name']]['hobby_list'].append(i['hobby'])
print(list(dic.values()))

# 1.txt.有如下文件，a1.txt，里面的内容为：
with open('a1.txt',encoding='utf-8',mode='w') as f:
    f.write(""""
老男孩是最好的学校，
全心全意为学生服务，
只为学生未来，不为牟利。
我说的都是真的。哈哈
""")
    f.flush()
# 分别完成以下的功能：
# a,将原文件全部读出来并打印。
with open('a1.txt',encoding='utf-8',mode='r') as f:
    for line in f.readlines():
        print(line)
# b,在原文件后面追加一行内容：信不信由你，反正我信了。
with open('a1.txt',encoding='utf-8',mode='a') as f:
    f.write('信不信由你，反正我信了。')
# c,将原文件全部读出来，并在后面添加一行内容：信不信由你，反正我信了。
with open('a1.txt',encoding='utf-8',mode='r+') as f:
    print(f.read())
    f.write('\n信不信由你，反正我信了')

# d,将原文件全部清空，换成下面的内容：
with open('a1.txt',encoding='utf-8',mode='w') as f:
    content="""
    # 每天坚持一点，
    # 每天努力一点，
    # 每天多思考一点，
    # 慢慢你会发现，
    # 你的进步越来越大。
    """
    f.write(content)
    f.flush()

# 2.有如下文件，t1.txt,里面的内容为：
file = open('t1.txt',encoding='utf-8',mode='w')
content="""葫芦娃，葫芦娃，
一根藤上七个瓜
风吹雨打，都不怕，
啦啦啦啦。
我可以算命，而且算的特别准:
上面的内容你肯定是心里默唱出来的，对不对？哈哈
"""
file.write(content)
file.close()

# 分别完成下面的功能：
# a,以r的模式打开原文件，利用for循环遍历文件句柄。
with open('t1.txt',encoding='utf-8',mode='r')  as f:
    for l in f:
        print(l)    # l是str数据类型
# b,以r的模式打开原文件，以readlines()方法读取出来，并循环遍历 readlines(),并分析b,与c 有什么区别？深入理解文件句柄与 readlines()结果的区别。
    f.seek(0)
    print(f.readlines())
    f.seek(0)
    for line in f.readlines():
        print(line)
# c,以r模式读取‘葫芦娃，’前四个字符。
    f.seek(0)
    print(f.read(4))
# d,以r模式读取第一行内容，并去除此行前后的空格，制表符，换行符。
    f.seek(0)
    content=f.readline()
    print(content.strip())
# e,以a+模式打开文件，先追加一行：‘老男孩教育’然后在从最开始将 原内容全部读取出来。
with open('t1.txt ',encoding='utf-8',mode='a+') as f:    # a+ 就是追加和读操作
    f.write('老男孩教育')
    f.seek(0)
    print(f.read())

# 3.文件a.txt内容：每一行内容分别为商品名字，价钱，个数。
with open('a.txt',encoding='utf-8',mode='w') as f:
    content = """apple 10 3
tesla 100000 1.txt
mac 3000 2
lenovo 30000 3
chicken 10 3 
"""
    f.write(content)

# 通过代码，将其构建成这种数据类型：[{'name':'apple','price':10,'amount':3},{'name':'tesla','price':1000000,'amount':1.txt}......] 并计算出总价钱。
# 方式一， 但有一个缺点，原来的内容没有删除。。。。
# f = open('a.txt',encoding='utf-8',mode='r+')  #  r+ 是读取后追加。。。。一定要注意先读后写和先写后读
# l = []
# for i in f.readlines():
#     dic = {}
#     i=i.strip()
#     i=i.split(' ')
#     dic['name']=i[0]
#     dic['price']=int(i[1.txt])
#     dic['count']=int(i[2])
#     l.append(dic)
# l=str(l)
# f.write(l)
# f.close()

import os
with open('a.txt',encoding='utf-8',mode='r') as f,\
    open('a副本.txt ',encoding='utf-8',mode='w') as f1:
    l = list()
    sum=0
    for i in f.readlines():
        dic = {}
        i = i.strip()
        i = i.split(' ')
        dic['name'] = i[0]
        dic['price'] = int(i[1])
        dic['count'] = int(i[2])
        price=dic.get('price')
        sum+=price
        l.append(dic)
    l = str(l)
    f1.write(l)
os.remove('a.txt ')
os.rename('a副本.txt ','a.txt ')

# 4.有如下文件：
content="""alex是老男孩python发起人，创建人。
alex其实是人妖。
谁说alex是sb？
你们真逗，alex再牛逼，也掩饰不住资深屌丝的气质。
"""
# 将文件中所有的alex都替换成大写的SB（文件的改的操作）。
with open('文件改',encoding='utf-8',mode='w') as f:
    f.write(content)
    f.flush()
with open('文件改',encoding='utf-8',mode='r') as f,\
     open('文件副本',encoding='utf-8',mode='w') as f1:
     msg = f.read()
     f1.write(msg.replace('alex','SB'))
os.remove('文件改')
os.rename('文件副本','文件改')


# 5.文件a1.txt内容(升级题)
with open('升级题',encoding='utf-8',mode='w') as f:
    content = """name:apple price:10 amount:3 year:2012
name:tesla price:100000 amount:1.txt year:2013
"""
    f.write(content)
    f.flush()
# .......
# 通过代码，将其构建成这种数据类型：
# [{'name':'apple','price':10,'amount':3,year:2012},
# {'name':'tesla','price':1000000,'amount':1.txt}......]
# 并计算出总价钱。

with open('升级题',encoding='utf-8',mode='r') as f,\
     open('升级副本',encoding='utf-8',mode='w') as f1:
    sum=0
    li = []
    for i in f.readlines():
        dic={}
        i=i.strip()
        i=i.split(' ')
        print(i)
        for j in i:
            a, b = j.split(':')
            if b.isdecimal():
                dic[a]=int(b)
            else:
                dic[a] = b
        sum+=dic.get('price')
        li.append(dic)
    f1.write(str(li))
    print('sun= ',sum)

# 6.文件a1.txt内容(升级题)

# 通过代码，将其构建成这种数据类型：

with open('升级题1',encoding='utf-8',mode='w') as f:
    content = """序号 部门 人数 平均年龄 备注
                 1.txt python 30 26 单身狗
                 2 Linux 26 30 没对象
                 3 运营部 20 24 女生多
"""
    f.write(content)
    f.flush()
# [{'序号':'1.txt','部门':Python,'人数':30,'平均年龄':26,'备注':'单身狗'}, ......]
with open('升级题1',encoding='utf-8',mode='r') as f,\
     open('升级副本1',encoding='utf-8',mode='w') as f1:
    l1 = f.readline()
    l1 = l1.strip()
    l1 = l1.split(' ')
    li = []
    i = 0
    l2 = f.readlines()
    while i<len(l2):
        dic = {}
        temp = l2[i]
        temp = temp.strip()
        temp=temp.split(' ')
        for j in range(len(l1)):
            dic[l1[j]] = temp[j]
        li.append(dic)
        i+=1
    f1.write(str(li))

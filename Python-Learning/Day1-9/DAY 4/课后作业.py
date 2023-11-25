# 今日作业
#
# 1.txt.简述解释性语言和编译型语言的区别？
#
# 2.列举你了解的Python的数据类型？
#
# 3.写代码，有如下列表，按照要求实现每一个功能。

# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# 计算列表的长度并输出
count = 0
for i in li:
    count+=1
print(count)
print(len(li))
# 请通过步长获取索引为偶数的所有值，并打印出获取后的列表
print(li[::2])
# 列表中追加元素"seven",并输出添加后的列表
li.append('seven')
print(li)
# 请在列表的第1个位置插入元素"Tony",并输出添加后的列表
li.insert(1,'Tony')
print(li)
# 请修改列表第2个位置的元素为"Kelly",并输出修改后的列表
li[1]='Kelly'   # 还是注意一下切片时候的添加元素与 索引更改元素的区别
print(li)
# 请将列表的第3个位置的值改成 "太白"，并输出修改后的列表
li[2]='太白'
print(li)
# 请将列表 l2=[1.txt,"a",3,4,"heart"] 的每一个元素追加到列表li中，并输出添加后的列表
l2=[1,"a",3,4,"heart"]
for i in l2:
    li.append(i)
print(li)
# 请将字符串 s = "qwert"的每一个元素添加到列表li中，一行代码实现，不允许循环添加。
li.extend('qwert')
print(li)
# 请删除列表中的元素"ritian",并输出添加后的列表
li.remove('ritian')
print(li)
# 请删除列表中的第2个元素，并输出删除元素后的列表
del li[1]
print(li)
# 请删除列表中的第2至第4个元素，并输出删除元素后的列表
#  listname.pop()
del li[1:4]
print(li)

# 4.请用三种方法实现字符串反转 name = "小黑半夜三点在被窝玩愤怒的小鸟"（步长、while、for）
name = "小黑半夜三点在被窝玩愤怒的小鸟"
print(' way one:')
print(name[-1::-1])
print('way two: ')
name2=name.split()      # 默认按照空格分割，如果没有空格，将字符串看成是列表的一个元素
print(name2)
name3=''
for i in range(len(name)-1,-1,-1):
#   name2[-where]=i    字符串是不可变的变量！！！！赋值错误
#     name2[-where]=i        默认按照空格分割，如果没有空格，将字符串看成是列表的一个元素 超界
    name3+=name[i]
print(name3)
print('way Three: ')

name4=''
i=len(name)-1
while i> -1:
    name4+=name[i]
    i-=1
print(name4)

# 5.写代码，有如下列表，利用切片实现每一个功能

li = [1, 3, 2, "a", 4, "b", 5,"c"]
# 通过对li列表的切片形成新的列表 [1.txt,3,2]
print(li[:3])
# 通过对li列表的切片形成新的列表 ["a",4,"b"]
print(li[3:6])
# 通过对li列表的切片形成新的列表 [1.txt,2,4,5]
print(li[::2])
# 通过对li列表的切片形成新的列表 [3,"a","b"]
print(li[1:-1:2])
# 通过对li列表的切片形成新的列表 [3,"a","b","c"]
print(li[1:-1])
# 通过对li列表的切片形成新的列表 ["c"]
print(li[-1:-2:-1],type(li[-1]))
print(li[-1:])   # 如果不写 ： 那么，取出来的元素直接是一个字符串
print(li[-2],type(li[-2]))
# 通过对li列表的切片形成新的列表 ["b","a",3]
print(li[-3::-2])

# 6.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
users = ["武沛齐","景女神","肖大侠"]
# 0 武沛齐
# 1.txt 景女神
# 2 肖大侠
j=0
for i in users:
    print(j,i)
    j+=1

# 7.请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
#
# 1.txt 武沛齐
# 2 景女神
# 3 肖大侠
le=len(users)
i = 1
while i<=le:
    print(i,users[i-1])
    i+=1

# 8.写代码，有如下列表，按照要求实现每一个功能。
#
lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1.txt"]], 89], "ab", "adv"]
# 将列表lis中的"k"变成大写，并打印列表。
lis[2]=lis[2].upper()
print(lis)
# 将列表中的数字3变成字符串"100"
lis[1]='100'
print(lis)
# 将列表中的字符串"tt"变成数字 101
lis[3][2][1][0]=101
print(lis)
# 在 "qwe"前面插入字符串："火车头"
lis[3].insert(0,'火车头')
print(lis)
print()

# 9.写代码实现以下功能
goods = ['汽车','飞机','火箭']
# 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
# 0,汽车
# 1.txt,飞机
# 2,火箭
# 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
print('你可选项的商品有：{}'.format(goods))
# print('你可选择的商品有：'+goods)      此处错误，只有字符串能实现运算
i=0
for t in goods:
    print('你可选择的商品有： \n%d,' %(i)+t)
    i+=1
# 下面代码报错，表示索引超出了范围
# while 1.txt:
#     select = input('请输入你的选择：')
#     if goods[int(select)] in goods:         # 注意，这样的话，返回的是一个字符串，True or False 但是在索引的时候，已经超界了，就会出错
#         print('你选择的商品是'+goods[int(select)])
#         break
#     else:
#         print('输入错误，请重选输入')
# print()
while 1:
    select = input('请输入你的选择：')
    if select.isdecimal():
        if int(select )<len(goods):
            if goods[int(select)] in goods:
                print('你选择的商品是' + goods[int(select)])
                break
            else:
                print('输入错误，请重新输入！')
        else:
            print('输入错误，请重选输入')
    else:
        print('输入错误，请重选输入')
print()
# 10. 请用代码实现
#
li = "alex"
li=list(li)
# 利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
print(li)
print('_'.join(li))
print()

# 11. 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
lite=list()
for i in range(101):
    if i%2==0:
        lite.append(i)
    else:
        pass
print(lite)
print()

# 12.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
lite2=[]
for i in range(51):
    if i%3==0:
        lite2.append(i)
print(lite2)
# 13.利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
li=[]
# [48,45,42...]
for i in range(51):
    if i%3==0:
        li.insert(0,i)
print(li)
print()
# 14.查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
j=0
for i in li:
    li[j]=li[j].strip()
    j+=1
print(li)
j=0
lin=[]
for i in li:
    if i.startswith('a'):
        lin.append(i)
    j+=1
print(lin)
for i in lin:
    print(i)

# 15.判断是否可以实现，如果可以请写代码实现。

li = ["alex",[11,22,(88,99,100,),33],"WuSir", ("ritian", "barry",), "wenzhou"]
# 请将 "WuSir" 修改成 "武沛齐"
i=0
while i<len(li):
    if li[i]=='WuSir':
        li[i]='小猪佩奇'
    i+=1
print(li)

# 请将 ("ritian", "barry",) 修改为 ['日天','日地']
a=['日天','日地']
li[-2]=a
print(li)

# 请将 88 修改为 87
# 元组不支持修改。所以不可行。

#  请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
li.remove("wenzhou")
print(li)
li.insert(0,'文周')
print(li)

#   为什么需要列表list？
#       现有数据类型太少了。int bool str
#       并且str中操作后（索引，切片）仍然是str,存储的数据太单一啦
#       功能： 列表是一个容器，可以承载任意数据类型的数据。存储大量的数据。  name=[12,'nae',['sgoa',10]]
print('========================列表list的定义：======================')
li_1=[13,'kevin',['谁不爱呢','他是我偶像啊',13,True]]
li_2=list('abcde')  # 每个字母对应list中的一个元素  底层使用了for循环。 ’‘内是可迭代的字符串类型
print(li_1,li_2)

print(' 有序的  按照顺序输出(索引切片）,  可变的 -- 可以在本身上进行修改- ')
print(li_1[2],type(li_1[2]))
print(li_2[:2:2],li_1[-1::-2],type(li_1[-1::-2]))

print('===========list是可变的:增删改查=================')
print('========增加=========')
print(' .append(str) 追加，加在末尾')
li=['张柏芝',['冠希哥',18,'小姑娘'],'谁不爱呢']
print(li.append('是不是'))    # 注意，执行完操作后，原来的的列表已经发生变化了，他的返回值为空
print(li,'\n')

print('  .insert(where,str)   效率较低')
li.insert(1,'name')
print(li,'\n')

print('   .extend()   追加数据的最小元素，例如，一个字符串，一个列表的等')
print('同时：如果输入是一个字符串，将该字符串拆为最小的单元，即一个个字母，如果是一个列表，拆违列表的每一项')
li.extend(['我也喜欢',100,[29,'你的名字']])
print(li,'\n')
li.extend('abcd')
print(li,'\n')

li = [1,2,3]
li.extend("abc")
print('extend() 的具体代码理解：')
for i in 'abcd':
    li.append(i)
print(li,'\n')

print('=========删========')
print('   .pop()   有返回值，返回值是删除的内容。  默认删除的是最后一个，也能够通过索引删除指定位置的元素。 ')

msg=list('你好啊')
msg.append([102,'喜欢'])
print(msg)
msg.insert(1,['test',1287])
print(msg)
msg.extend('暗号改了')
print(msg)

msg.pop()
print(msg)
print(msg.pop(1))
print('按照位置删除：第几个元素。',msg)
print('注意一下列表中的索引的位置写法 ')

print(' ======== .remove(name) =======按元素名删除')
msg.remove('啊')
print(msg)
#  如果元素不存在报错。

print('=======del===========')
print("""
支持索引、切片删除 del listname[star: end :step]
删除整个容器 del listname """)
del msg[2]
print(msg)
del msg[:3:2]
print(msg)
del msg
print('看看里面还剩下什么:')
print("name 'msg' is not defined")

print('   .clear()   用于清空list  ')
li = [1,2,3,43]
li.clear()
print(li)
print()

print('=========================改=======================')
print('=============基本都是按照索引和切片去改就可以了===========')
li=['name',1029,['123','try again',123]]
print(li)
li[0]=[100,[1002,'name']]
print(li)
li.pop(2)
print(li)


l2 = [1,2,3,4,66,7]

l2[:2:]=['迭代进去的元素','步长连续时,能多','能少','shima']
print(l2)
l2[:3:2]=['迭代进去的元素','当步长不为1时，不能多不能少']
print(l2)

# ====================================== 面试题:===================================
li = [1,2,3,4,"abc",5]
li[0:2] = "ABC"    # 注意，都是切片的 迭代增加。。。。
print("""""
这就是典型的那个问题，如果采用切片： 迭代进入的元素，采用连续步长可以多也可以少，但是步长不连续时，不能多不能少。""")
print(li)
print()
# 索引
# 切片
# 步长 ---  你取几个,就放几个  不能多不能少
li=[1,2,3,[1,2,3],'水杯']
li[:3:2]='n' ,'a'
print(li)
print('多个列表直等价输入：')
a,b=[12,3],[4,5,6]
print(a,b)
a,b=b,a
li.append([a,b])
print(li)
print()

print('=========================查=======================')
print('================按照索引查询:  &&&&    for 循环  =============== ')

for e in li:
    print(e)


print('===================列表的嵌套:======================')
li = ["水杯","衣服","鞋子","书","电脑","屁",["手机","钥匙",["身份证","银行卡"]],]

l2 = li[6]
l3 = l2[2]
print(l3[0])

li[6] =["手机","钥匙",["身份证0","银行卡0"]]
li[6][2] = ["身份证1","银行卡1"]
print(li[6][2][0])

li.remove('衣服')
print(li)
print()

"""
列表：
.reverse()
反转。主要用于对列表进行反转输出。
.sort(reverse=True)
从大到小, 支支持数字类型的
.sort(reverse=False)
从小到大。
"""

li = [1,2,3,{1:34,'name':'zhangsan '}]
li.reverse()
print(li)
li=[3,56,2,5,2,1]
print(list(set(li)))
print(li)
li.sort(reverse=False)
print(li)


print(' =========================   tuple 元组的初识  ======================= ')
tu1=('1.txt')
print(tu1,type(tu1))
tu1=(1,)
tu2=()
print(tu1,type(tu1),type(tu2))

# 他是什么?
# 元组  tuple
# tu = ("1.txt")  # ()  每个元素都以 逗号隔开
# tu1 = (1.txt)
# 小括号中一个元素的时候没有逗号就括号中元素的本身
# 小括号中一个元素的时候有个逗号就是元组
# 空的小括号就是元组
# print(type(tu1))

print("""

# 元组有序:
#     索引,切片,步长
# 元组不可变数据类型""")

# tu = (1.txt,2,3)
# print(tu[1.txt])

# 元组只能查看不能修改   -- 元组和列表和相似,元组是不可修改的

# 他能干啥?
# 存储一些你不想让别人修改的数据  - 元组容器 存储一些任意类型

# 在哪干?
# 在配置文件中,程序中  为了防止误操作修改一些数据

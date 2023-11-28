# 数据类型的分类：
# 可变的（可哈希） ：  list  dict  set
# 不可变（不可哈希）：int bool str tuple

# 字典
#  因为list存储的数据之间关联性不强，用于存储大量数据，数据的查询速度很快，比列表快。
# 字典是什么？   dict
print("""字典，dict   {}  键(一定是不可变的数据类型，要唯一，不然会被覆盖）：值一定要一一对应""")
print("""字典3.5版本及之前是无序的，3.6x会按照建立字典的顺序排列，学术上不认为是有序的。3.7x都是有序的""")
print('以空间换时间')
print()
print('===============================定义字典的几种方式=========================')

print('======方式一======')
dic={'name':[1,2,3],
     'age':18,
     'address':'yunnan'}
print(dic)

print('======方式2======')
dic=dict(键='与数值一一对应',one=1,two=2,three=3)  # dict expected at most 1.txt argument
# dic=dict(’键‘='与数值一一对应',one=1.txt,two=2,three=3)   错误，
print(dic)

print('======方式3======')
dic=dict({'张三':1,
          '里斯':2})
print(dic)
print('======方式4======')
dic=dict([('one',1),('two',2),('Three',3)])

print(dic)
print('==========字典的定义方式很多，可以之间 鼠标左键 + ctrl==========')
print('总结来说，就是对于字典而言 {}一一对应，dic() 里面可以利用 =  {}，[]等方法定义')
print()

print('字典和列表，元组的大致总结')
# li=list(1.txt,2,3)  list expected at most 1.txt argument
li=list((1,2,3))
print(li,type(li))

ty=([1,2,3])
print(ty,type(ty))
ty=([1,2,3],)
print(ty,type(ty))
print()

# s="{'a':1,'b':2}"
# print(dict(s))        目前所学的知识点，字典不能转换的

print('===============================字典的使用：增删改查=========================')
print('========增========')
print("直接增加：dict_name[键名]=‘键值'  ")
dic={'a':'b','b':'c'}
dic['c']='d'
print(dic)
print('如果键名重复，就会覆盖原结果，进行改操作有则改之，无则增加')
dic['c']='b'
print(dic)

print(' .setdefault(键名,键值)  有则不变，无责增加')
dic=dict(键名='键值',one=1,two='2')
print(dic)
dic.setdefault('张三','zhangsan')

print(dic)
print(dic.setdefault('张三',1))
print('返回的是键名：')
print('可以查看字典中是否存在该键名：  dicname.setdefault[键名]  ,如果存在返回的是键值,不存在则报错，',dic['one'])  # 直接写dic[one]就错了，

print(' 另一种增加方式 .update(element)   有则更新，无责增加 ')
info={'明天':'会更好','世界':'很美丽'}
print(dic.update(info))

print('========删 pop del clear========')
dic=dict([('美羊羊','喜喜'),('懒洋洋','沸羊羊')])
dic.setdefault('村长','灰太狼')
dic.setdefault('熊大','熊二')
print(dic)

print('pop需要指定元素删除，没有该键，报错，返回值是删除键的值 ')
print(dic.pop('村长'))
print(dic)

print('del删除')
del dic['熊大']
print(dic)

dic.clear()
print(dic)

print('========改========')
print('方式一： 就是利用增里面的，有则改之，无则增加')
dic=dict(one=1,a=1,名字='time')
dic['a']='珍惜'
print(dic)

print('方式二：  .update()  update的优先级别很高，如果和原键值有重复，那么直接修改， 没有重复，直接增加')
dic2=list([('我喜欢','周星驰'),('红烧鸡翅','我喜欢吃'),('a','存在着')])
dic.update(dic2)
print(dic)
print()

print('========查========')
print('只能通过键获取键值，不能通过键值获取键 ')
print('方式一： dic[键] ')
dic = {1: 2, "a": "a1"}
print(dic[1])

print('方式二  get(键，返回的是他们对应的内容，不存在，不报错。)')
print(dic.get('a','你不是个傻子，是个包子'))
print(dic.get(1,))

print('对键值进行一定的操作。当然，字符类型一定要一致才可以进行操作。')
dic={'a':1}
dic['a']+=5
print(dic.get('a'))

print('for 循环打印的是字典的 键')
dic = {1: 2, "a": "a1"}
for i in dic:
    print('返回的是键',i)
    print(dic[i],type(i))

print()

print('=========================================课上练习========================================')
dic = {"1":1,"2":2,"3":3,"4":4}
# # 删除"2"  2种方式
print(dic.get('2'))
del dic['2']
print(dic)

print(dic.pop('1'))
print(dic)
dic.setdefault('5',5)
print(dic)

# a=dict([('喜羊羊','美羊羊'),('小红','光头强'),{'5':'修改后'}])  # dictionary update sequence element #2 ，
# 这里错误的原因是：你输入的是列表的形式，那么他只是将字典{}识别为了一个键，但是没有与之对应的数值，所以错误了

a=dict([('喜羊羊','美羊羊'),('小红','光头强'),{'键后值前','5'}])  # dictionary update sequence element #2
# 上述代码中，{}的内容没有明显的键值关系。
dic.update(a)
print(dic)

a=dict([('喜羊羊','美羊羊'),('小红','光头强'),{'修改后,长度长，直接键前值在后','5'}])
# 对于字典的更新，需要两个键值对及以上
# dic.update(a,b)    update expected at most 1.txt argument
dic.update(a)
print(dic)

print("现在自己的理解： 如果 update 字典，如果是上述类型的，"
      "那么当{}时，寻找是否和原字典有相同的键，有，修改，但是当第一个长度过长，那么直接增加")

a= {'text':1,
    '3':"修改"}
dic.update(a)
print(dic)
print()

print('字典返回的是键名：')
li=[]
dic = {"1.txt":1,"2":2,"3":3,"4":4}
for key in dic:
    li.append(key)
print(li)

print('  dicname.keys()    for 循环返回键名，但是注意：  不能进行索引  ')
for i in dic.keys():   # 高仿列表，就是将列表中的键名取出来，类似单独成一个列表去了,但是数据类型是 dict_keys的
    print(i,type(i))
dic_l=dic.keys()
print(dic_l,type(dic_l))   # dict_keys(['1', '2', '3', '4']) <class 'dict_keys'>

print('  dict_name.values()    for 循环返回键值，但是注意：  不能进行索引  ')
for i in dic.values():
    print(i,type(i))

dic_l2=dic.values()
print(dic_l2 ,type(dic_l2 ),'\n可以对他进行类型转换为列表',list(dic_l2 ),type(list(dic_l2 )))

print('items()  返回的是全部的键值对 ,只用一个变量去取键值对，返回的是元组类型的数据。')
for key,value in dic.items():
    print(key,value,type(key),type(value))

for i in dic.items():
    print(i,type(i))

print('==================================拆包问题：==========================================')
a,b=('go',1)
print('is a ',id(a))
print('id b',id(b))

a,b=b,a
print('is a',id(a))
print('is b',id(b))
print(' 拆包问题，直接交换了存储地址，应该说，将变量指向的内存地址进行了交换，对原来的地址中的内容没有任何变化 ')

a,_,c='你好啊'
print(a+c)

a,b=[1,'更换']
print(a,b,type(a))

a,b={'a':1,'b':2}
print(a,b)
a,b=b,a
print(a,b)

print('==========================time 函数的使用=============================')
dic = {"1":1,"2":2,"3":3,"4":4}
import time
s='2'
t=time.time()
if s in dic.keys():
    pass
print('字典的速度',time.time()-t)
print('对比列表的速度 :')
li=list('1234')
s='2'
t=time.time()
if s in li:
    pass
print(time.time()-t)
print('数据少的时候看不出来差距')
print()


# 字典是无序的,我现在
dic = {"电脑":15000,"手机":8000,"耳机":4000,"老婆":1111}
# 1 电脑
# 2 手机
# 3 耳机
# 4 老婆

for i in range(len(dic)):
    print(i+1)

count=1
for i in dic.keys():
    print(count,i)
    count+=1

print('=======================枚举 =======================')
li=[1,2,3,4,5]
for i,k in enumerate(li):       # 第二个参数不写默认就是0,那么输出就是一个元组，
    print(i,k)

for i in enumerate(li):
    print(i,type(i))

dic={'1':1,'2':2,'3':3}
for i,k in enumerate(dic):     # 取到的是键
    print(i,k,type(k))

print('==================================================字典的嵌套====================================')
dic = {
    101:{1:["周杰伦","林俊杰"],2:{"汪峰":["国际章",{"前妻1":["熊大","熊二"]},
                                  {"前妻2":["葫芦娃","木吒"]}]}},
    102:{1:["李小龙","吴京","李连杰"],2:{"谢霆锋":["张柏芝","王菲"]},
         3:["alex","wusir","大象","奇奇"]},
    103:{1:["郭美美","干爹"],2:{"王宝强":{"马蓉":"宋哲"}}},
    201:{1:["凹凸曼","皮卡丘"],2:{"朱怼怼":{"杨幂":"刘恺威"}}}
}

print(dic[101][2]['汪峰'][1]["前妻1"])
# ['国际章', {'前妻1': ['熊大', '熊二']}, {'前妻2': ['葫芦娃', '木吒']}]
# {'前妻2': ['葫芦娃', '木吒']}
# ['葫芦娃', '木吒']
print(dic[101][2]['汪峰'][2]['前妻2'][1])
print(dic[103][2]["王宝强"]["马蓉"])

home1 = dic[102][3][2]
# {1: ['李小龙', '吴京', '李连杰'],
# 2: {'谢霆锋': ['张柏芝', '王菲']},
# 3: ['alex', 'wusir', '大象', '奇奇']}
# print(home1)


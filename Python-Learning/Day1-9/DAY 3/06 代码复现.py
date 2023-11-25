# while else 结构
# 格式化输出
# 内容回顾 % 占位符后面接上数据类型， 最后占位符输出

# 整数
print(2**0)
print('===============数据类型转换================')
#数据类型的转换：
# i=100
# s='00193' #回省略相应的0
# b=False
# print(int(s))
# print(str(i))
# print(bool(i))
# print(int(b))
# print(str(False))        #bool类型转化为str就是普通的True或False
# print(bool(s))
# print(bool(''))


# 进制转换，
# 14 十进制，转化为二进制：

# 128 64 32 16 8  4 2 1.txt
# print(2**0)
# print(2**1.txt)
# print(2**2)
# print(2**3)
# print(2**4)
# print(2**5)
# print(2**6)
# print(2**7)
#
# num=7  # 8421  00000111
# # .bit_length()   十进制转换为二进制所占用的位数。
# print(num.bit_length())

# bool
print('===========bool==========')
print(bool(-10))       # 0是False,其余为真。
print(type(str(True)))
print(int(False))

print('==========str============')
print('功能： 用于存储少量数据：')
'''
只要用引号引用起来的都是字符串。
#那么
啊搜狗
se
'''
name='alex,meet,do . if d'
# 索引  0123456...    从左到右
#     -7 -6 -5 -4 -3 -2 -1.txt     从右到左
print('一定要注意，顾头不顾尾这个问题，在取终止位置的时候比较重要。')
a=name[2]
b=name[3]
print(a+b)
print(name[2:5])     # 顾头不顾尾     ，还可以使用步长     [起始位置：终止位置：步长：]
print(name[2:5:2])

print(name[:100])    # 切片超出了终止位置不会报错
# print(name[100])       索引超出了终止位置会报错

print(name[::])
print(name[::-1])    # 输出也是从右往左的，一定要记住
print(name[-7:0:-1])     # 一定要注意，他是顾头不顾尾的，所以，0的位置取不到，那个位置最好空着就可以了。
print(name[:0:-1])
print(name[-3:])  # 默认步长为1，所以是向后输出的

name = "周扒皮，王菲，陈冠希，张柏芝，谢霆锋，周星驰，李亚鹏"
a=name[3:6]
b=name[8:10]
c=name[1:3]
print(a,b,c)


print('=================一些常用的字符串操作=====================')
print('大小写问题：')
name='Alex, mette'
res=name.upper()
print('upper() 的返回值')
print(name.upper())
# 这两行代码是等价的，因为直接进行操作，输出的就是返回值‘
print(res)

print('  id()函数的作用：  返回数据在内存中的真实地址。')
print(id(name))
print(id(res))
print(id(1))

name2='MeTTe TAO'
print(name2.lower())

print('大小写转化主要应用场景：  验证码，不论大小写')
yzm='KEVIN带着98K,他好帅啊！'
your_yzm=input('请输入验证码：  Kevin带着98k,他好帅啊！\n  >>>>>')
if your_yzm.upper()==yzm:
    print(your_yzm.upper())
    print("对于大小写的转化，注意一个问题，在遇到中文字符以及其他符号时会忽略，判断之后的内容。")
    print('太正确了！')
else :
    print('你是煞笔吧，这都猜不对')

print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print('================= 以什么字母开头和结尾的问题，对于字符串，别忘记还可以切片和索引==========================')
print('# 针对大小写比较敏感。返回 布尔数值')
print(name.startswith('a'))  # 针对大小写比较敏感。
print(name.upper().startswith('A'))
name='treue'
# 两种切片方式
#  strname[start:end:step].startswith(’字符')
print(name[:4:2].startswith('te'))

# 第二种方式   strname.startswith('str',start,end)
print(name.startswith('reu',1,4))

print(name.endswith('e'))

print('===============计算字符出现的次数====================')
#  strname.code('str')
code='asglcgasgaes'
print(code.count('a'))
print(code.count('ag'))
print(code.count('asg'))

print('================replace======================')
print('有返回值，返回值就是结果。并不会改变原来字符串的数据。默认从左开始，全部替换')
# print(strname.replace('str','str',count))
print(code.replace('a','f',2))

print('===================去除空格等操作====================')
print('默认去除空格，换行，tab等')
msg=""" \n  \t  ke  
   \t   v
    \nin 
"""
print(msg)
print('只能去除开头和末尾的空行和空格等。')
print(msg.strip('\n'))
print(msg.strip('n'))   #该函数主要用于去除空格等操作。

print('=================字符串转化为列表（返回值是列表）：  分割操作================')
name='alex.mak,morto'
print('默认以空格分割：')
print(name.split(','))

print('==============字符串的格式化输出方法==================')
print(' 第一种  占位符 ')
while 1:
    name=input('请输入姓名：')
    age=input('请输入年龄:')
    sex=input('请输入性别：')
    num=input('请输入学号：')
    msg = """  ******** Resume *********
    Name=%s
    age=%s
    sex=%s
    num=%s
    """ % (name, age, sex, num)
    print(msg)
    again=input('是否继续？y or n : ')
    if again.upper()=='N':
        break

print()
print(' 第二种:  {}顺序输入 ')
name='Alex{},Kevin{}'    #按照顺序输入
print(name.format('马上结婚了','很想结婚，但是没女朋友'))
print()
print(' 第三种：{1.txt}  按照索引位置取填充  ')
name='Alex{1.txt},Kevin{0},黎明也是{1.txt}'
print(name.format('马上结婚了','很想结婚，但是没女朋友'))

print(' 第四种 :  {a}   strname.format(a="马上结婚" ,b="想结婚，但是没女朋友")    '
      '指名道姓填充本质也是按照索引')
name='Alex{b},Kevin{a},黎明也是{b}'
print(name.format(a="马上结婚" ,b="想结婚，但是没女朋友"))

print('=======================is系列=========================')
print('返回布尔数值')
num1='666'
print('isdigit()主要用于判断是不是纯数字，但是优缺点',num1.isdigit())
num2='②'
print('此类数据识别错误',num2.isdigit())
print(num2.isdecimal())
num3='keb,,,v33'
print('主要用于识别是不是字母和中文,不能识别特殊符号。',num3.isalpha())
print(num3.isalnum())
num4='kaein1234男童'
print('主要用于识别字母，数字，中文',num4.isalnum())
print()

print('===================for==============')
s='selx,si,namu.meaun.do,suone.thing ol '
print('str的长度是：',len(s))
print('len(strname)获取数据的长度，除了 Int bool两种类型')
count=0
while count<len(s):
    print(s[count])
    count+=1
print('上例等同于在for中使用如下代码：')
for i in s:
    print(i)
print(
    """""
# for 关键字
# i 变量
# in 关键字    
# s 可迭代对象  
int - bool    不适用 'bool' 'int'   object is not iterable
"""
)
for a in 'alex':
    print(a)
    pass
    ...  # 这只是正常说这一行代码不再执行了。其后的正常执行。
print('pass 和 ...都是掠过的意思')
print('ex' in 'alex' )   #返回值是bool类型。

print(a)

print('==================面试大坑 range(start,end,step)=============')
for i in range(0,15,2):
    print(i)
for i in range(100,-11,-1):
    print(i)
for i in range(4):
    print(i)

print('=======================join======================')
print('将列表转化为字符串类型：')
# s1=['李荣浩','张柏芝','陈冠希',24]          #expected str instance, int found
s1=['李荣浩','张柏芝','陈冠希']
s2="+".join(s1)
print(s2)
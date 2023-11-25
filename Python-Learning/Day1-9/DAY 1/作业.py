# 1.txt.操作系统的作用?
# 操作系统是一个软件，主要用于将计算机的硬件以及软件调动起来，从而能够执行相应的程序。

# 2.python是什么类型的语言?
# 解释性语言，即编译一句然后执行一句，开发效率高，但是执行效率低

# 3.解释一下你理解的编译型,和解释型语言
# 编译型：将写好的程序直接全部编译之后在执行，开发效率低，执行效率高
# 解释性：代码逐行编译运行，执行效率低，开发效率高

# 4.补充代码,实现以下功能:
#
value ='alex'
print(value) # 输出结果是 alex

# 5.简述变量命名规范
# 字母数字下划线，不能以数字开头，不与关键字重名

# 6、用print打印出下面内容：
content='''
文能提笔安天下,
武能上马定乾坤.
心存谋略何人胜,
古今英雄唯是君.
'''           # 利用''' '''         """"""可以进行换行输出
print(content)

# 7.name = input(">>>") name变量是什么数据类型？用代码实现
# input的数据类型都是字符串型的数据，
name = input(">>>")
print(name,type(name))

# 8.补充代码
#
name = "周杰伦"
name1 = "林俊杰"
name2 = name
name = "张学友"    # 字符串的加法运算(就是进行字符串的拼接）以及乘法运算（就是重复多少次）
print(name,name1,name2)
print(name+name1,name*3)
# 结果: 张学友,林俊杰,周杰伦

# 9.简述你了解的if条件语句的基本结构
# if condition:  else         elif:

# 10.设定一个固定年龄比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。
age=66
get_age=input('please input your age:')
if int(get_age)>age:
    print("oversize")
elif int(get_age)<age:
    print('minimal')
else:
    print("Nice,younger")

# 11.提⽰⽤户输入⿇花藤. 判断⽤户输入的对不对. 如果对, 提⽰真聪明, 如果不对, 提⽰你 是傻逼么
tecent = input('请输入  麻花螣：')
if tecent=='麻花螣':
    print('great！')
else:
    print('fuck,you are the bitch')

# 12.让用户输入 姓名,年龄 然后输出以下结果:
user_name=input('请输入姓名：')
user_age=input("请输入年龄：")
user_sex=input("请输入性别：")
print('我叫%s, 我今年 %s 岁，我的性别爱好是 %s,今天看到了1%%' % (user_name ,user_age ,user_sex))
print("我叫 ",user_name ,"我今年",user_age, "岁，我的性别爱好是", user_sex)
print("我叫 "+user_name +"我今年"+user_age+"岁，我的性别爱好是"+user_sex)

# 比较容易忘记的两种方式。
print('我叫 ',user_name ,'我今年',user_age, '岁，我的性别爱好是', user_sex)
print('我叫 '+user_name +'我今年',user_age+ '岁，我的性别爱好是'+ user_sex)


# 我叫:Alex 我今年:18岁
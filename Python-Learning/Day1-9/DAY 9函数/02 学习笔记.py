"""
======================================= 昨日内容回顾 ====================================
1. 文件操作：
        三部曲：
            打开文件 open()  path encoding mode
            操作文件，对文件句柄
            关闭文件
2.  读 写 追加
   r r+ rb r+b  w w+ wb w+ a a+ ab a+b
   read(element)
   readline()
   readlines()
   for 对文件句柄，解决大文件内存问题
   tell()
   seek()    seek（0，2） 从头到尾，记住了哈。
   flush()

with open as f

3. 文件改的操作：
    五部曲：
        打开一个只读文件和一个只写文件
        读出源文件
        写入新文件
        删除源文件
        重命名写入文件

======================================= 今日大纲 ===================================
函数的初识：
            # 不用 len , 利用 count计数，写代码太low了，重复代码太多，，，，代码的可读性太差了
            def fc_name(element):
                    函数体
            调用方法：  fc_name(传入参数)
            定义： 以功能为导向。完成某种功能。 登录，注册，len
            要注意一个函数就只有一个功能，随调随用
            优点： 减少代码的重复性，增强了代码的可读性。

函数的结构与调用：
            def fc_name():
                函数体

               def 关键字，定义函数
               meet 函数名，与变量命名设置相同"，具有可描述性
               函数体： 一定要有缩进，尽量不要出现 print
            只有出现  函数名()  函数才会被执行

函数的返回值：
            执行函数后，执行得到的结果。
            return 功能：
                        直接结束函数。
                        给函数外部返回一个值，如果没有反沪指，那么返回值为空
                        如果return返回多个元素，那么以元组的形式，返回给函数的执行者。

                    总结：
                        在函数中，终止函数，
                        可以给函数的执行者返回值：   单个值：  单个值，      多个值： 元组的形式 （多个值，）

函数的参数：
            盘活这个函数
            将一些参数传入函数中，使其能实现某种功能
            实参： 函数执行传入的参数      meet('女')
            形参：  接收的参数形式的参数           def meet(sex)

            函数的传参： 实参，形参
                    实参：
                        位置参数，按照位置传入参数，从左至右，一一对应
                        关键字参数：  参数太多了的时候，直接利用关键字，在传输实参的时候，可以利用关键字传入参数
                                        meet (age = '23’，skill ='nice',high ='167')
                        混合传参：  位置参数一定要在关键字参数前面。。。。。

                    形参：
                        位置参数，位置一定与实参一一对应，从左到右
                        默认值参数：
                                设定好之后，只要设置完之后，就不变，除非你手动去改
                                用于形参处，设定好默认参数
                                           def  meet( age,skill,sex='女')  会按照顺序覆盖。
                                           可以去看看 open 的，里面mode 默认读，你可以对其进行覆盖，
                                                    但是原函数是不变的。
                                设置的意义：经常使用的才设置。
                                小心一点： 在使用默认参数时，注意一下 万一位置不对应，没有关键字
                                            有的地方被覆盖了，导致后面彼得参数没传进去就报错

三元运算符
 a = b if 1>2 else c

 一点疑问的解答：
def make_average():
    li = [1,2,3,4]
    def average(new_values):
        print(locals())
        return new_values

    return average
avg = make_average()
print(avg(11))
print(globals())    # 没有继续使用 li 那么这个空间中就没有了 li 这个列表
print(avg(12))   正常来说，我们知道，函数执行完毕，会释放局部名称空间，但是如果函数是嵌套函数，
                你返回了 嵌套的内层函数的地址。
一旦调用了外层函数，那么在函数执行完毕之后，全局名称空间中已经有了 嵌套的 内层函数的地址，
        此时他已经相当于一个全局名称空间去了
对于调用的函数中的一些变量，如果继续使用，形成闭包，不继续使用，那么，函数执行完毕，会被释放空间

下面的例子也能说明：
def make_average():
    li = [1.txt,2,3,4]
    def average(new_values):
        print(locals())
        return new_values
    average(18)
    return 'nice'
print(make_average())
print(globals())   函数执行完毕，没有返回继续使用的地址等，那么 全局名称空间中就没有了 average 函数的地址。不能继续使用了。

"""
#  函数的初识：   用 陌陌软件为例：
def meet():
    print('打开tantan ')
    print('左滑一下')
    print('右滑一下')
    return '妹子一枚' ,123,[2,3,5,7]        # 没有返回值，那么返回值为空
    print('找美女')
    print('悄悄话')
    print('约吗？')
    # return

"""
def 关键字，定义函数
   meet 函数名，与变量命名设置相同"，具有可描述性
   函数体： 一定要有缩进，尽量不要出现 print 
"""

#  函数什么时候执行？
#  函数名() 只有出现了这个。才会执行函数。
meet()
print()

ret = meet()
print(meet(),type(ret))

def momo(weight,high,sex,age,skill):              # 形参
    print('打开默默')
    print('进行筛选：性别 %s ，年龄 %s 技术 %s' %(sex,age,skill))
    print('你传进来一些参数啊，不传我没有办法筛选啊')
    return {'name':'slg'},'性别 %s 年龄 %s ' % (sex,age)
momo(145,170,sex='女',age='23',skill='great')
ret = momo(145,170,sex='女',age='23',skill='great')
# 实参    按照位置传入参数，从左至右，一一对应  有了等号，就是关键字传入参数
# 混合参数 ： 位置参数一定要在关键字参数前面
print(ret)
print()

# 写一个函数，接受两个int 的参数，函数的功能是将较大的数值返回
def max(a,b):
    c = 0
    if a>b:
        c=a
    else:
        c=b
    return c
# 三元运算符简写  return c = a if a>b else b
print(max(15,68))     # 返回值一定要输出或者返回给一个变量

print()
# 三元与运算符： 简单的 if else
a = 10
b =20
c = a if a>b else b
print(c)

# 传入两个字符串参数。将两个参数拼接完成后的结果返回
print()
def cat(s1,s2):
    return s1+s2
a='sjosgl'
b='slgoeiunh'
print(cat(s1=a,s2=b))    # 关键字传参

# 写一个函数，检查传入列表的长度，保留前两个长度的内容，并将内容返回给调用者
print()
def ex_len(l1):
    # count = 0
    # for i in l1:
    #     count+=1.txt
    # return l1=l1[:2] if count>2 else l1
    return l1 [:2]
li = [1,{'slg',24,5},34,67,8]
print(ex_len(li))

print()
def func():
    count =1
    while 1:
        count+=1
        print(count)
        return         # 一定要注意，这是结束函数
func()

# 对文件进行批量修改
import os
def files(path,old_content,new_content):
    with open(path,encoding='utf-8') as f,\
         open(path+'.bak',encoding='utf-8',mode='w') as f1:
        for i in f:
            i=i.replace(old_content,new_content)
            f1.write(i)
    os.remove(path)
    os.rename(path+'.bak',path)

files('文件批量改的操作.txt','asb','kevin')
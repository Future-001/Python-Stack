# 1.txt，使⽤循环打印以结果:
#
# *
# ***
# *****
# *******
# *********
for i in range(1,6):
    print("*"*(1+2*(i-1)))

# 2,使用while循环打印以下结果:
#
# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *
for i in range(11,1,-1):
    print('*'*(i-1))



# 7.看代码写结果并解释原因(以下看代码写结果,一定要自己先思考.在验证!)
#
# v1 = {'k1':'v1','k2':[1.txt,2,3]}
#
# v2 = {'k1':'v1','k2':[1.txt,2,3]}
#
#
# result1 = v1 == v2
#
# result2 = v1 is v2
#
# print(result1)
#
# print(result2)
# 8.看代码写结果并解释原因
#
# v1 = {'k1':'v1','k2':[1.txt,2,3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2["k1"] + v1["k1"])
# 9.看代码写结果并解释原因
#
# v1 = '人生苦短，我用Python'
#
# v2 = [1.txt,2,3,4,v1]
#
# v1 = "人生苦短，用毛线Python"
#
# print(v2)
# 10.看代码写结果,并解释原因
#
# info = [1.txt,2,3]
# userinfo = [info,info,info,info,info]
# info[0] = '不仅多，还特么难呢'
# print(info,userinfo)
# 11.看代码写结果,并解释原因
#
dic1 = {"k1":5,"k2":10}
dic2 = dic1.copy()    # 这是浅copy
dic2["k1"] = 1
print(dic1["k1"] + dic2["k1"])   # 注意，对于字符串数据类型，是不可变的，那么修改的话，直接将其原来的数值进行了修改，对k1指向了不同的地址。

# 12.念数字给出一个字典. 在字典中标识出每个数字的发音. 包括相关符号. 然后由用户输入一个数字. 让程序读出相对应的发音(单纯的打印即可,不考虑个十百)
#
# 例如: 7.5 输出: qi_dian_wu
dic = {'0':'ling',
    '1.txt':'yi',
    '2':'er',
    '3':'san',
    '4':'si',
    '5':'wu',
    '6':'liu',
    '7':'qi',
    '8':'ba',
    '9':'jiu',
    '.':'dian',
}
for i,j in dic.items():
    print(i,j)
while 1:
    i = input('请输入>>> ')
    if i.isdecimal():
        if i in dic:
            print(dic[i])
            break
        else:
            print('输入非法，请重新输入.')
    else:
        print('输入非法，请重新输入.')


# 13.敲七游戏.从1开始数数.遇到7或者7的倍数要在桌上敲⼀下.编程来完成敲七.给出⼀个任意的数字n. 从1开始数. 数到n结束.把每个数字都放在列表中,
# 在数的过程中出现7或者7的倍数(不包含类似于17,27，这种数).则向列表中添加⼀个'咣'
import random
li = []
n=random.randint (1,100)
for i in range(1,n):
    if i%7==0:
        li.append('咣')
    else:
        li.append(i)
print(li)
# 例如, 输⼊10 # lst = [1.txt, 2, 3, 4, 5, 6, '咣', 8, 9, 10]






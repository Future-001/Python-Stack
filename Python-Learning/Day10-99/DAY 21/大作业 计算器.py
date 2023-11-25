# 计算两个数的乘法和除法  化繁为简。简单计算

# 计算一个表达式所有的乘法和除法


# 1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))
#           - (-4*3)/ (16-3*2) )等类似公式的计算器程序
# 不要用拿什么计算， eval   先匹配小括号的内容，先计算乘除法，后计算 加减法。
#  要求用循环，用正则，尽量去调用函数。
data='1-2*((60-30+(-40/5)*(9-3*5/3+12/3*99/4*2998+14*568/14))-(-4*3)/(16-3*2))'
#  采用下面这个的话，后面带了 (( 稍微麻烦了一些，不好计算。
# 乘除法的正则
result = 0
import re
# print(re.findall('[(]'))
# while True:
#     ret = re.findall('[(][^()]+[)]', data)
#     print(ret)
#     for i in ret:
#         ret1 = re.findall('-?\d+?(?:[*/]\d+)+',i)
#         # 如何每一部分都只出现一次呢？ 还有的最多出现一次呢？
#         print(ret1)
#         break   # 有点问题，应该先算两个数字之间的运算。


def move_multimod(data):
    ret = re.findall('[(][^()]+[)]', data)
    # print(ret)
    for i in ret:
        k=i
        while 1:
            ret1 = re.search('-?\d+(\.\d+)?[*/]-?\d+',i)
            if ret1:
                ret1=ret1.group()
                # print(ret1)
                if '*' in ret1:
                    a,b=ret1.split('*')
                    res = float(a)*float(b)
                elif '/' in ret1:
                    a, b = ret1.split('/')
                    res = float(a) / float(b)
                i=i.replace(ret1,str(res))
            else:
                break
        data = data.replace(k, f'{i}')
    return data


data = move_multimod(data)    # 1-2*((60-30+(-8.0)*(9-5.0+296802.0+568.0))-(-12.0)/(16-6.0))
print('去除括号内的乘除法',data)

def add_sub(data):
    ret = re.findall('\([^()]+\)',data)
    print(ret)
    for i in ret:
        k=i
        while 1:
            ret1 = re.search('-?\d+(?:\.\d+)?[-+]\d+(?:\.\d+)?',i)
            # print(i)
            if ret1:
                ret1=ret1.group()
                # print(ret1)
                if '+' in ret1 and not ret1.startswith('+'):
                    a, b = ret1.split('+')
                    r = float(a)+float(b)
                elif '-' in ret1 and not ret1.startswith('-'):
                    a, b = ret1.split('-')
                    r = float(a) - float(b)
                elif ret1.count('-')==2:  # ['(-2378962.0-1.2)']
                    ret1= ret1.replace('(','').replace(')','')
                    # print(ret1)
                    # print(ret1.split('-'))    分割出来了一个空格空白符？  不太对劲的样子。
                    _,a,b=ret1.split('-')
                    r = float(a) + float(b)
                    r=-r
                i=i.replace(ret1,str(r))
            else:
                break
        data = data.replace(k,i)
        # print(data)
    return data

data = add_sub(data)     #  1-2*((60-30+(-8.0)*(297374.0))-(-12.0)/(10.0))
print('去除括号内的加减法',data)
# data = '1-2*((60-30+(-8.0)*(297374.0/(234*129)))-(-12.0)/(10.0))'  # 这种的里面可能还有一点问题
#  接下来就是去除括号，然后计算乘除法后，在进行加减法的计算。
def kuohao(data):
    ret = re.findall('\([^(]+?[*/][^)]+?\)',data)   #  这样还是会漏，还是用search把
    print(ret)
    # for r in ret:
    #     r1 = re.search('\(-?',ret)
    # while True:
    #     ret = re.search('\(')
    for j in ret:
        if '*' in j:
            a,b=j.split('*')
            res =float(a[1:-1]) * float(b[1:-1])
        if '/' in j:
            a,b=j.split('/')
            res =float(a[1:-1]) / float(b[1:-1])
        data=data.replace(j[1:-1],str(res))
    print(data)
    return data

data = kuohao(data)

def rm_kuohao(data):
    while 1:
        ret = re.search('([+-])?(\(-?\d+(?:\.\d+)?\))', data)
        if ret:
            print(ret.group())
            if ret.group(1)!='-':
                tem = ret.group(2).replace('(','').replace(')','')
                print(tem)
                data=data.replace(ret.group(),tem)
                print(data)
            elif ret.group(1)=='-':
                tem = float(ret.group(2).replace('(', '').replace(')', ''))
                print(tem)
                if tem>0:
                    data = data.replace(ret.group(), str(-tem))
                elif tem<0:
                    data = data.replace(ret.group(),str(+tem))
                else:data=data.replace(ret.group(),'')
                print(data)

        else:
            break
    return data
data = rm_kuohao(data)
data = add_sub(data)
print(data)
data = rm_kuohao(data)
print(data)
data = add_sub(data)
print(data)


r = re.search('([-+])?(\d+)[*/][(]-(\d+\.\d+)[)]',data)
print(r.group(2))
print(r.group(3))
print(r.group())
ret = float(r.group(2))*float(r.group(3))
data=data.replace(r.group(),'+'+str(ret))
print(data)
print(eval(data))


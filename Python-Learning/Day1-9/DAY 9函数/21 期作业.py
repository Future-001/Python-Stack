# 将函数部分知识点，整理到自己笔记中。（搞明白课上讲的案例。）
#
# 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回。
def new_result(s):
    li = []
    li.append(s[1::2])    # 返回值位空
    return li
s = (1,2,3,'name',45,[2,'kevin',{'price':199}])
print(new_result(s))

# 写函数，判断用户传入的一个对象（字符串或列表或元组任意）长度是否大于5，并返回真假。
def length(s):
    return len(s)>5
print(length(s))

# 写函数，接收两个数字参数，返回比较大的那个数字。
def max(a,b):
    return  a if a>b else b
print(max(a = 3 ,b=6))
print(max(3,8))
print(max(6,b=3))   # 位置参数一定要在关键字参数之前


# 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历。用户通过输入这四个内容，然后将这四个内容传入到函数中，
# 此函数接收到这四个内容，将内容根据"*"拼接起来并追加到一个student_msg文件中。
def conjunction(age,sex,name,degree):
    return name+'*'+age+'*'+sex+'*'+degree
# name,age,sex,degree =input('请输入姓名，年龄，性别，以及学历')
with open('student_msg',encoding='utf-8',mode='w') as f:
    dic =dict(name=None,age=None,sex=None,degree=None)
    for i in dic:
        dic[i]=input('请输入 {}>>> '.format(i))
    print(dic)
    f.write(conjunction(name=dic["name"], age=dic["age"], sex=dic["sex"], degree=dic['degree']))
    f.flush()




# 写函数，在函数内部生成如下规则的列表 [1.txt,1.txt,2,3,5,8,13,21,34,55…]（斐波那契数列），并返回。
# 注意：函数可接收一个参数用于指定列表中元素最大不可以超过的范围。
def qbnq(max):
    li = [1,1]      # 这样其实不太智能了
    if max<1:
        return '输入错误，请重新输入'
    else:
        if li[-1]<max:
            li.append(li[-1]+li[-2])
        else:
            return li
print(qbnq(1))


# 写函数，验证用户名在文件 data.txt 中是否存在，如果存在则返回True，否则返回False。（函数有一个参数，用于接收用户输入的用户名）
# def val(username):
#     with open('data.txt',encoding='utf-8') as f:
#         content = f.read()
#     return (username in content)
# 有缺陷
# print(val('lex'))

def val(username):
    with open('data.txt',encoding='utf-8') as f:
        li = ['order','username','pwd']
        l1 =[]
        for i in f:
            dic = {}
            i = i.strip()
            i = i.split('|')
            for j in range(len(li)):
                dic[li[j]] = i [j]
            l1.append(dic)
        result =''
        for t in l1:
            if username == t['username']:
                result = ' '
        return bool(result)
print(val('lex'))

# data.txt文件格式如下：
#
# 1.txt|alex|123123
# 2|eric|rwerwe
# 3|wupeiqi|pppp
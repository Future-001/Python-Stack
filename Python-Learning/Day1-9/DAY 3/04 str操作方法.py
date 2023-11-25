# upper  lower  忽略中文
# usage：  variable.upper()   variable.lower()
s1='Kevin, 零零七'
print(s1.upper(),type(s1.lower()))

i=0
while i<3:
    username = input("请输入账户名")
    passpord = input("密码")
    code = 'Awsl'
    your_code = input("请输入验证码,不区分大小写: ")
    if your_code.upper()==code.upper()  or   your_code.lower()==code.lower():
        if username=='111' and passpord =='1234':
            print("登录成功!")
            break
        else:
            print("账户或密码错误,请重新输入!")
            i+=1
            print("你还剩 %d 次机会" % (3-i))
    else:
        i+=1
        print("验证码错误,你还剩 %d 次机会" %(3-i))
else:
    print("错误次数过多,账号被封禁.")

# startswith  endswith
# usage:   variable.startswith('str',star_position,end_position),注意进行 +1操作
name_1='Kevin'
print(name_1.startswith('in',3,5))  # 返回bool数值

# replace
# usage：  variable.replace(self,old,new,count)
msg_1="Alex 是我的好大儿,Alex非常帅"
print(msg_1.replace('Alex','佩奇'))

# strip()  去除空格 空白,\n,\t
# usage:       variable.trip('str')
s11='\n \t Kevin'
print(s11)
s22=s11.strip()
print(s22)

# 去除指定的字符
# 注意：从前往后同时从后往前去除，如果碰到停下来的，那么就停止去除
# eg: print(s1.strip('Kn'))
# 输出结果是evakci
print(s11.strip('K'))      # 注意，因为s11首字母含有空格，他的起始位置就是空格的位置
print(s22.strip('Kin'))

# split 分割    字符串分割为  列表
# s1.split(指定分隔符,分割次数)
#
# 默认按照空格分隔，将其分割为list
# s1=':name:she:sei'
# print(s1.split(':'))
# 第一个字符是空字符，即''
msg_split='*name*to* *the'
print(msg_split.split('*'))

# join 联合  列表(其中的元素要求是字符串) 联合为字符串
# usage:    '运算符'.join(str)
name_join=['李荣浩','李白','年少有我']
print('+'.join(name_join))
test_1='李荣浩李白年少有我'
print('+'.join(test_1))   # 注意，他也是 迭代着 拼接到一起的

# count  统计某个字符串出现的次数
# usage:  variable.count('str')
print(test_1.count('李'))

#format  格式化输出
# 用法一       {}作为占位符
msg1="我的名字是{},今年{}岁了，性别是{}".format('大壮',18,'Male')
print(msg1)
# 用法二
msg2="我的名字是{0},今年{1}岁了，性别是{2}，我的名字再说一次，是{0}".format('大壮',18,'Male')
print(msg2)
msg3="我的名字是{na},今年{age}岁了，性别是{sex}".format(sex='Male',na='大壮',age=18)
print(msg3)

#  .isxxx()
# 常用
#     .isdecimal()
#     .isalpha()
#     .isalnum()
# 1.txt.有变量name = " aleX leNb " 完成如下操作：
name=' aleX leNb '
# 移除 name 变量对应的值两边的空格,并输出处理结果
print(name.strip())
# 将 name变量对应的值中所有的空格去除掉,并输出处理结果
# 方式一
print(''.join(name.split()))
# 方式二
print(name.strip(' '))
print(name.split())
# 注意， .split()  默认去除空格， 在指定去除字符后，如果去除的字符处于第一个或者最后一个， 那么分割开的列表存在着 ''空字符
name=name.split()   # 将字符串转化为列表。默认以空格分割
print("".join(name))          # 注意，列表没有 startswith属性
name=''.join(name)
# 判断 name 变量是否以 "al" 开头,并输出结果（用两种方式 切片+字符串方法）
print(name.startswith('al'))          # startswith('str',start,end)
print(name.startswith('al',0,2))
print(name[0:2].startswith('al'))
# 判断name变量是否以"Nb"结尾,并输出结果（用两种方式 切片+字符串方法）
print(name.endswith('Nb'))
print("本题给了一个很好的例子， endswith('str',start,end)  记住，采用倒序输出的时候，注意到起始位置，记住顾头不顾尾。同时，该函数没有反向步长")
print(name.endswith('Nb',-2,))
# print(name.endswith('Nb',-1.txt,-3))
# print(name.endswith('Nb',-3,-1.txt))

print(name[-1:-3:-1].endswith('Nb'))    # 这样判断就是False， 因为这样是倒序输出，从最后一个开始输出,别忘记反向步长
print(name[-1:-3:-1].endswith('bN'))
print(name[-2:].endswith('Nb'))

print(name)
print(name[-2:])
print(name[-3:-1])

# 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
print(name.replace('l','p'))
# 将name变量对应的值中的第一个"l"替换成"p",并输出结果
print(name.replace('l','p',1))          # 注意replace是从左到右替换的
# 将 name 变量对应的值根据 "l" 分割,并输出结果
print(name.split('l'))
# 将 name 变量对应的值全部变大写,并输出结果
print(name.upper())
# 将 name 变量对应的值全部变小写,并输出结果
print(name.lower())
# 请输出 name 变量对应的值的第 2 个字符?
print(name[1])
# 请输出 name 变量对应的值的前 3 个字符?
print(name[:3])
# 请输出 name 变量对应的值的后 2 个字符?
print(name[:-2:-1])       # 注意倒叙的时候就是从-1开始的，正序的话，最后一个是0 ，为了防止冲突，直接不写。
print(name[-1:-3:-1])      #注意倒序输出

# 2.有字符串s = "123a4b5c"
s = "123a4b5c"
# 通过对s切片形成新的字符串 "123"
print(s[:3])
# 通过对s切片形成新的字符串 "a4b"
print(s[3:6])
# 通过对s切片形成字符串s5,s5 = "c"
print(s[-1])
# 通过对s切片形成字符串s6,s6 = "2ab"
print(s[1:-2:2])
# 通过对s切片形成字符串s6,s6 = "cba"
print(s[-1:2:-2])
# 3.使用while循环字符串 s="你好世界" 中每个元素。
s="你好世界"
count=0
while count<len(s):        # len()  对 int bool 无效
    print(s[count])
    count+=1
print('方法二：')
for i in s:
    print(i)

# 4.使用while循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"(提示使用字符串方法中的格式化)
s='321'
i=0
while i<len(s):
    print('格式刷0：倒计时{}秒'.format(s[i]))
    print('格式刷1：倒计时 %s 秒' %(s[i]))
    print('格式刷2：倒计时 {0} 秒' .format(s[i]))
    print('格式刷3：倒计时 {a} 秒' .format(a=s[i]))
    i+=1
else :
    print('出发！')

# 5.使用for循环对s="321"进行循环，打印的内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"，"出发！"(提示使用字符串方法中的格式化)
print('for循环+格式刷')
for j in s:       # 注意一点，for循环从字符串中取到的已经是字符了。并不需要在进行不断地查询与切片
    print('格式刷0：倒计时{}秒'.format(j))
    print('格式刷1：倒计时 %s 秒' % (j))
    print('格式刷2：倒计时 {0} 秒' .format(j))
    print('格式刷3：倒计时 {a} 秒' .format(a=j))
print('出发！')

# 6.实现一个整数加法计算器(两个数相加)：
while 1:
    i=int(input('请输入加数：'))
    j=int(input('请输入被加数：'))
    print('sum=i+j=%d' %(i+j))
    print('sum=i+j={}' .format(i+j))
    print('sum=i+j={a}' .format(a=i+j))
    print('还需要计算吗？ y or n:')
    ans=input('>>>')
    if ans.upper()=='N':
        break
# 如：content = input("请输入内容:") 用户输入：5+9或5+ 9或5 + 9（含空白），然后进行分割转换最终进行整数的计算得到结果。(列表也支持索引)
content=input('请输入内容：')
tem=content.split()
print(tem)
tem=''.join(tem)    # 担心一个数会不会被分隔开输入了，例如 123 34 45+ 3485 4 2
print(tem)
tem=tem.split('+')   # 犯了一个错误，列表能够直接转换数据类型吗？  显而易见，可以
print(tem[0],tem[1])
print('{0}+{1}=%d'.format(tem[0],tem[1])  % (int(tem[0])+int(tem[1])))
# print(int(tem[0])+int(tem[1.txt]))

# 7.计算用户输入的内容中有几个 s 字符？\
# 如：content = input("请输入内容：") # 如abcassfsqfsafqsdzacsad
s=input('请输入内容：')
print(s.count('s'))

# 8.使用while循环分别正向和反向对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。
msg = "伤情最是晚凉天，憔悴厮人不堪言。"
while i<len(msg):
    print(msg[::])
    print(msg[-1::-1])

msg = "伤情最是晚凉天，憔悴厮人不堪言。"
i = 0
while i < len(msg):
    print(msg[i])

    i += 1
    print(msg[-i])

# 9.获取用户输入的内容，并计算前四位"a"出现几次,并输出结果。
s=input('请输入内容：')
print(s[:4].count('a'))

# 10.制作趣味模板程序需求：等待⽤户输⼊名字、地点、爱好，根据⽤户的名字和爱好进⾏任意现实 如：敬爱可亲的xxx，最喜欢在xxx地⽅⼲xxx (字符串格式化)
while 1:
    user_name = input('请输入姓名：')
    site = input('请输入地点： ')
    hobby = input('请输入爱好：')
    msg="""敬爱可亲的{1},最喜欢在%s地方干{0}""".format(hobby,user_name) % (site)
    print(msg)

# 11.判断⼀句话是否是回⽂. 回⽂: 正着念和反着念是⼀样的. 例如, 上海⾃来⽔来⾃海上
print(" 采用方式一 字符串相等 ：")
s=input('请输入：')
s1=s[-1::-1]
if s1==s:
    print('是回文！')
else :
    print('不是回文')
print('方法二：通过for判断每个字符是否都是相对应的。')
j=1
for i in s:
    if i==s[-j]:
        j+=1
    else :
        print('不是回文')
print('是回文')

# 12.输⼊⼀个字符串，要求判断在这个字符串中⼤写字⺟，⼩写字⺟，数字，其他共出现了多少次，并输出出来
#   .isupper()   islower()
content=input(' 请输入字符串:')
cap_count=0
num_count=0
min_count=0
for i in content:
    if i.isdecimal():
        num_count+=1
    if i.isalpha():
        if i.upper()==i:
            cap_count+=1
        if i.lower()==i:
            min_count+=1
print('大写字母数量是'+str(cap_count), '小写字母数量是{} 有{}个数字'.format(min_count,num_count) )

len=len(content)
i=0
count=0
while i<len:
    if content[i].upper()==content[i]:
        count+=1
print(count)

# 13.用户可持续输入（用while循环），用户使用的情况：
while 1:
# 输入A，则显示走大路回家，然后在让用户进一步选择：
    select=input('请输入选择 A B C：')
    if select.upper()=='A':
        print('走大路回家。')
# 是选择公交车，还是步行？
        select2 = input('请输入回家的方式：')
        # 选择公交车，显示10分钟到家，并退出整个程序。
        if select2 =='公交车':
            print('10分钟到家')
            break
        # 选择步行，显示20分钟到家，并退出整个程序。
        if select2 == '步行':
            print('20分钟到家')
            break
# 输入B，则显示走小路回家，并退出整个程序。
    elif select.upper()=='B':
        print('走小路回家。')
# 输入C，则显示绕道回家，然后在让用户进一步选择：
    elif select.upper()=='C':
        print('绕道回家。')
# 是选择游戏厅玩会，还是网吧？
        select3=input('游戏厅 or 网吧：')
        # 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
        if select3=='游戏厅':
            print('一个半小时到家，爸爸在家，拿棍等你。')
            continue
        # 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
        if select3=='网吧':
            print('两个小时到家，妈妈已做好了战斗准备。')
            continue
    print('输入错误，请重新输入！')

# 补充习题
# 获取用户两次输入的内容，并将所有的数据获取并进行相加，如：
"""
要求：
	将num1中的的所有数字找到并拼接起来：1232312
	将num1中的的所有数字找到并拼接起来：1218323
	然后将两个数字进行相加。
"""

num1 = input("请输入：") # asdfd123sf2312
num2 = input("请输入：") # a12dfd183sf23
# 请补充代码
for i in num1:
    if i.isdecimal():
        str1+=''.join(i)
        print(str1)
for i in num2:
    if i.isdecimal():
        str2 += ''.join(i)
        print(str2)
print(str1,str2)
print(int(str1)+int(str2))
# 1.txt.猜数字，设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了,然后继续让用户输入; 如果比66小，则显示猜测的结果小了,然后继续让用户输入;只有等于66，显示猜测结果正确，然后退出循环。
# while 1.txt:
#     num = int(input("请输入你理想中的数字："))
#     if num > 66:
#         print("你猜大了！")
#         continue
#     elif num<66:
#         print('你猜小了！')
#         pass
#     else:
#         print("好耶，你猜对了呢！")
#         break

# 2. 在上一题的基础，设置：给用户三次猜测机会，如果三次之内猜测对了，则显示猜测正确，退出循环，如果三次之内没有猜测正确，则自动退出循环，并显示‘大笨蛋’
#
count=0
while count<3:
    num = int(input("请输入你理想中的数字："))
    count+=1
    if num > 66:
        print("你猜大了！")
        continue
    elif num<66:
        print('你猜小了！')
        pass
    else :
        print("好耶，你猜对了呢！")
        break
else :
    print('错误次数过多，请稍后再试')


# 3. 判断下列逻辑语句的True,False
# not > and > or
# and 的输出规则， 前面为真，输出后一个 数字 或者 True False   #前面为假，直接输出False
# 前面是0，直接输出0，   后面含0(无比较），输出0
# 1.txt > 1.txt or 3 < 4 or 4 > 5 and 2 > 1.txt and 9 > 8 or 7 < 6
# True
# not 2 > 1.txt and 3 < 4 or 4 > 5 and 2 > 1.txt and 9 > 8 or 7 < 6
#  False

# 4.求出下列逻辑语句的值。
#
# 8 or 3 and 4 or 2 and 0 or 9 and 7
# 8   print (3 and 4) 前后都为真，直接为真，输出最大值。
print(8 or 3 and 4 or 2 and 0 or 9 and 7)
# 0 or 2 and 3 and 4 or 6 and 0 or 3
# 0 or 4 or 0 or 3   输出为4
print(0 or 2 and 3 and 4 or 6 and 0 or 3)

# 5.下列结果是什么？
#  a> b 的结果只是真和假，也就是只是 0 和1 ，所以在进行 and or 操作时，将他们当作零和1
# 6 or 2 > 1.txt
# 6
# 3 or 2 > 1.txt
#3
# 0 or 5 < 4
#False
# 5 < 4 or 3
# 3
# 2 > 1.txt or 6
# True
# 3 and 2 > 1.txt
# True
# 0 and 3 > 1.txt
# 0
# 2 > 1.txt and 3
# 3
# 3 > 1.txt and 0
# 0
# 3 > 1.txt and 2 or 2 < 3 and 3 and 4 or 3 > 2
# 2

# 6.使用while循环输出 1.txt 2 3 4 5 6 8 9 10
count=0
while count<10:
    count+=1
    print(count)

# 7.求1-100的所有数的和
sum = 0
for i in range(101):
    print(i,type(i))
    sum+=i
print(sum)

# 8.输出 1.txt-100 内的所有奇数 (奇数就是除以2余数不为0)
sum=0
for j in range(101):
    if j%2!=0:
        print('j=', j)
        sum += j
    else:
        continue

print(sum)

# 9.输出 1.txt-100 内的所有偶数 (偶数就是除以2余数不为1)
#
for x in range(101):
    if x%2==0:
        print(x)

# 10.求1-2+3-4+5 ... 99的所有数的和
#方法一
count=1
result=0
while count<100:
    if count%2==0:
        result=result-count
    else:
        result+=count
    count+=1
print('result=',result)

# 方法二
# range的方法也可以

# 11.简述ASCII、Unicode、utf-8编码英文和中文都是用几个字节?
# ASCII码中，全都是一个字节，gbk 英文字符和数字一个字节，中文两个字节，Unicode中，全部都是四个字节，
# utf-8 英文一个字节，欧洲2字节，中文三字节

# 12.简述位和字节的关系？
#  一个字节等于8bit

# 13. "老男孩"使用GBK占几个字节,使用Unicode占用几个字节?
#  GBK 占用8字节，Unicode占用20字节

# 14.猜年龄游戏升级版 要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，
# 就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。
# 方法一：
count=0
while count<3:
    age=int(input('请输入猫神的年龄：'))
    if age>66:
        print("你猜错了，请重来")
    elif age<66:
        print('你猜小了，重新试试把')
    else:
        print("恭喜你，猜对了")
        break
    count+=1
    if count==3:
        print('你还想继续玩吗？请输入y or n')
        ans=input()
        if ans.upper()=='Y':
            count=0
        else :
            break

# 方法二：
count=0
while 1:
    if count < 3:
        age = int(input('请输入猫神的年龄：'))
        if age > 66:
            print("你猜大了，请重来")
        elif age < 66:
            print('你猜小了，重新试试把')
        else:
            print("恭喜你，猜对了")
            break
    count += 1
    if count == 3:
        print('你还想继续玩吗？请输入y or n')
        ans = input()
        if ans.upper() == 'Y':
            count=0
        else:
            break

# 15. ⽤户登陆（三次输错机会）且每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）

code = 'alex'
count=0
while count<3:
    user_name = input('请输入用户名：')
    user_passpord = input("请输入密码：")
    your_code = input('请输入验证码：')
    if your_code == code:
        if user_name == 'kexin':
            if user_passpord=='110':
                print("登录成功！")
                break
        else :
            print("账号或密码错误，请重试，你还有 %d 次机会" % (2-count))
    else :
        print("验证码错误，请重试，你还有 %d 次机会" % (2-count))
    count+=1
else :
    print("错误次数过多，请稍后重试！")
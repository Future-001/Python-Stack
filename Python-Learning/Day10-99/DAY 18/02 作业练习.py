# 写函数，让用户输入用户名密码，将密码转化成密文，然后构建一个字典，字典的键为用户名，值为其对应的密码，将这个字典以json字符串的形式写入文件中。
import json,hashlib
dic = {}
username = input('请输入用户名： ')
pwd = input('请输入密码： ')
md_5 = hashlib.md5()
md_5.update(pwd.encode('utf-8'))
a = json.dumps(md_5.hexdigest())
dic[username]=a
print(dic.items())

# 利用递归寻找文件夹中所有的文件，并将这些文件的绝对路径添加到一个列表中返回（面试题，有点难，可先做其他）。
# 这个题应该可以做过了。，主要是判断 isdir or isfile 主要是通过递归，然后返回值的话是文件的绝对路径

# 写函数：用户输入某年某月，判断这是这一年的第几天（需要用Python的结构化时间）。
# 忘记了一个东西，忘记了什么呢？忘记了 datetime的一些用法
import datetime,time
print(time.localtime())  # 结构化时间。
def date(year,month,day):
    input_date = datetime.datetime(year,month,day)
    start = datetime.datetime(year,1,1)
    return (input_date-start).days +1
year = int(input('请输入年份: '))
month = int(input('请输入月份：'))
day  = int(input('请输入日：'))
print(date(year,month,day))
# 结构化时间可以通过这样取值：
#
# import time
# ret = time.localtime()
# print(ret)  # time.struct_time(tm_year=2019, tm_mon=6, tm_mday=28,
# tm_hour=15, tm_min=50, tm_sec=47, tm_wday=4, tm_yday=179, tm_isdst=0)
# 2019
# print(ret.tm_year)  # 2019

# 写函数，生成一个4位随机验证码（包含数字大小写字母）。
import string  # 没怎么用过
import random
all_chars = string.ascii_letters + string.digits
verification_code = ''.join(random.choice(all_chars) for _ in range(4))
print(verification_code)
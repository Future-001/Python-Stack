# 一、正则表达式练习
# 1、匹配整数或者小数（包括正数和负数）
# 2、匹配年月日日期 格式2018-12-6
# 3、匹配qq号
# 4、11位的电话号码
# 5、长度为8-10位的用户密码 ： 包含数字字母下划线
# 6、匹配验证码：4位数字字母组成的
# 7、匹配邮箱地址
# 8、1.txt-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-32))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
import re
ret = re.findall('\([^()]+?\)','-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-32))')
print(ret)
# 9、从类似9-25/3+7/399/42998+10*568/14的表达式中匹配出乘法或除法
# 10、从类似
# <a>wahaha</a>
# <b>banana</b>
# <h1>qqxing</h1>
# 这样的字符串中，
# 1）匹配出<a>,<b>,<h1>这样的内容
# 2）匹配出wahaha，banana，qqxing内容。(思考题)

# 自学以下内容，完成10、2)
ret = re.search("<(?P<tag_name>\w+)>\w+</\w+>","<h1>hello</h1>")
# #还可以在分组中利用?的形式给分组起名字
# #获取的匹配结果可以直接用group('名字')拿到对应的值
print(ret.group('tag_name')) #结果 ：h1
print(ret.group()) #结果 ：<h1>hello</h1>
#
# 二、使用listdir完成计算文件夹大小
# 三、根据以下需求，完成选课系统作业，5月4号晚上10点之前提交
# https://www.cnblogs.com/Eva-J/articles/9235899.html
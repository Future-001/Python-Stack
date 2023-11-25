# # 相关练习题
# # 1，"1-2*(60+(-40.35/5)-(-4*3))"
# # 1.1 匹配所有的整数
import re
res = re.findall('(\d+\.\d+)|(\d+)',"1-2*(60+(-40.35/5)-(-4*3))")
print(res)
res = re.findall('(?:\d+\.\d+)|(\d+)',"1-2*(60+(-40.35/5)-(-4*3))")
print(list(filter(lambda n:n,res)))

# # print(relx.findall('\d+',"1-2*(60+(-40.35/5)-(-4*3))"))

# # 1.2 匹配所有的数字（包含小数）
res = re.findall('\d+\.\d+|\d+',"1-2*(60+(-40.35/5)-(-4*3))")  # search 不太行，他只显示第一个符合条件的。
print(res)
# 下面的方法确实也不错。
# # print(relx.findall(r'\d+\.?\d*|\d*\.?\d+', "1-2*(60+(-40.35/5)-(-4*3))"))


# # 1.3 匹配所有的数字（包含小数包含负号）
# # print(relx.findall(r'-?\d+\.?\d*|\d*\.?\d+', "1-2*(60+(-40.35/5)-(-4*3))"))
print(re.findall('-?\d*\.?\d+', "1-2*(60+(-40.35/5)-(-4*3)).123"))
# 还有一些问题，那么，当出现 .234 也匹配上了，但是他是错的。 但是下面也出现了  123.   也被匹配上了。
# print(re.findall('-?\d+\.\d*', "1.+1-2*(60+(-40.35/5)-(-4*3))"))   怎么改呢，加括号成了优先显示了。
print(re.findall('-?\d+(?:\.\d*)?', "1-2*(60+(-40.35/5)-(-4*3))"))  # 这样好像可以了

#
#  注意通用化的方法。
# # 3，匹配一段你文本中的每行的时间字符串 这样的形式：'1995-04-27'
s1 = '''
时间就是1995-04-27,2005-04-27
1999-04-27 老男孩教育创始人
老男孩老师 alex 1980-04-27:1980-04-27
2018-12-08
3409++++++  11 =16
2010/04/15
'''
' 这里怎么做呢？    [1-9]\d{3}-([12]\d|0?[1-9])-([12]\d|3\d|0?[1-9}' \
'  如果中间的符号是任意的。：     [1-9]\d{3}(?P<sub>[^\d])(1[0-2]|0?[1-9])(?P=sub)([12]\d|3[0-2]|0?[1-9])                       '
print(re.findall('\d{4}[^\d]*?\d{2}[^\d]*?[1-2]\d|\d{4}[^\d]*?\d{2}[^\d]*?[3][0-1]|\d{4}[^\d]*?\d{2}[^\d]*?0[1-10]',s1))

print(re.findall('[1-9]\d{3}(?P<sub>[^\d])(?:1[0-2]|0?[1-9])(?P=sub)(?:[12]\d|3[01]|0?[1-9])','2019-2-1'))
# 不能用 ？？： 所以有问题。
# print(relx.findall('\d{4}-\d{2}-\d{2}', s1))
#
# # 4 匹配 一个浮点数
print(re.findall('\d+(?:\.?\d*)?','1.17'))

# # print(re.findall('\d+\.\d*','1.17'))
#
# # 5 匹配qq号：腾讯从10000开始：
print(re.findall('[1-9]\d{4}\d*','123456778df346557657234fghdf65745'))
# # print(re.findall('[1-9][0-9]{4,}', '2413545136'))
#
s1 = '''
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7459977.html" target="_blank">python基础一</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7562422.html" target="_blank">python基础二</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/9439483.html" target="_blank">Python最详细，最深入的代码块小数据池剖析</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/7738630.html" target="_blank">python集合,深浅copy</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8183203.html" target="_blank">python文件操作</a></p>
<h4 style="background-color: #f08080;">python函数部分</h4>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8241942.html" target="_blank">python函数初识</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8259929.html" target="_blank">python函数进阶</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8305011.html" target="_blank">python装饰器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423526.html" target="_blank">python迭代器,生成器</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8423937.html" target="_blank">python内置函数,匿名函数</a></p>
<p><a style="text-decoration: underline;" href="http://www.cnblogs.com/jin-xin/articles/8743408.html" target="_blank">python递归函数</a></p>
<p><a style="text-decoration: underline;" href="https://www.cnblogs.com/jin-xin/articles/8743595.html" target="_blank">python二分查找算法</a></p>

'''
# # 1,找到所有的p标签
print('<p>.*</p>',s1)

# # ret = relx.findall('<p>.*?</p>', s1)
# # print(ret)


# # 2,找到所有a标签对应的url
ret = re.findall("""<a.*?href="(.+?)".*?</a>""",s1)
print(ret,len(ret))

# # print(re.findall('<a.*?href="(.*?)".*?</a>',s1))


# 匹配一篇英文文章的 标题  例如： The Voice of China
r = re.compile('[A-Z].*')
print(r.findall('The Voice of China'))

#  匹配15位或18位的身份证号码
print(re.findall('[1-9]\d{14}(?:\d{2}[\dx])?','123456789123123'))

# 从下面算式中匹配出最内层小括号以及小括号内的表达式
s1 = '1-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-32))'
res = re.findall('.*?[(]{2}.*?([(].*?[)])[)].*',s1)
print(res)     # 简单的写法：    \([^()]+\)

# 从 9-25/3+7/399/42998+10568/14 中匹配出乘法或除法。  \d+[*/]\d+
s1 = '9-25/3+7/399/42998+10568/14'
print(re.findall('.*?(\d+/\d+(?:[/]\d+)*)',s1))



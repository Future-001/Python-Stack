# 关键词的查看
import keyword
print(keyword.kwlist)

help('keywords')

 #常量，  没有真正的常量，默认全部大写为常量
COUNT=1
print(COUNT)

COUNT+=1
print(COUNT)

#关于注释   #  单行注释
'''这是一个多行注释
可以实现对多行进行注释'''

# 当换行时候自动出现一个 \，
'这也是一个注释 ' \
'但是只能实现单行注释'

msg=''''
多行注释可以实现换行的输出，
例如这就是
一个很明显的
例子'''
print(msg)

m='那么单行注释可不可以呢？' \
  '答案就在这行代码里' \
  '尝试一下就知道了' \
  '从结果可以看出，他不能实现换行输出' \
  '那么我加上一个%n, ' \
  '是否可以呢？' \
  '明显也不能'
print(m)
# 按照索引取值,注意这只是针对字符串而言的。
# 对字符串进行索引切片出来的数据字符串类型,且切片出来数据与原存储空间没有任何关系
s1='Hello , my friend'
s2=s1[6]
print(s2,type(s2))

# 还可以从最后倒着取值
s3=s1[-3]
print(s3,type(s3))


# 按照切片取值
# 0在前，还有最后一个可以省略。切片中的最后一个取不到,尽量+1.txt
ss=s1[:6]
print(ss)
ss=s1[6:-1]    #最后一位无法读入,填成0与前面冲突,所以直接不写
print(ss)
ss=s1[6:]
print(ss)

#步长
s_test=s1[3:7:2]
print(s_test)
# 倒序
# 必须要有反向步长,不然报错 或者输出一片空白
s_test1=s1[-1:-7]
print(s_test1)

# 注意，倒序切片也是倒序输出的。
s_test1=s1[-1:-7:-2]
print(s_test1)
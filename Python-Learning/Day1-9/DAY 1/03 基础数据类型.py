# 常见的基础数据类型有哪些呢？
#  bool   int  str
#一定要注意   ‘’    ‘’‘  ’‘’   “”  ”“”“”“   引号引起来的内容都是属于字符串类型的数据

# 字符串之间的   +  和  * 运算
msg1='kevin'
msg2='hello'
print(msg1+msg2)#就是将两个字符串直接拼接起来,只能在字符串之间进行

#print(msg1*msg2)   该方法错误，字符串相乘只是说将字符串*一个数字，即将其复制多少遍然后拼接到一起
print(msg1*3)

#type函数

print(type(msg1),type(1))
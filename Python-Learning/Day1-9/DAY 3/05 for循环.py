# 将  '我叫Kevin,我最帅! '  分别用 while 和 for输出
s1='我叫Kevin,我最帅!'
# 成员运算, 只能从开头或者末尾同时查找，当碰到不符合的就停止下来，返回值是布尔类型
print('叫我' in s1)
print('!我' in s1)
print(len(s1))
i=0
# 内置len()函数，自动获取可迭代元素的总个数
while i<len(s1):
    print(s1[i])
    i+=1
print('--------------------------------')
for j in s1:
    print(j)


s11='老男孩'
print('老' in s11)
print('老孩' in s1)
print('老孩' not in s1)
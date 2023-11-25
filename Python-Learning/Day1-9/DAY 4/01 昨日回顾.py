for i in 'hello':
    if i=='hello'[1]:
        continue
    print(i)
print(i)
for j in '321':
    print('倒计时秒，仅剩下%s秒'% (j))
    print('倒计时{}秒'.format(j))
    print('倒计时{}秒'.format(j) + '仅剩下%s秒'% (j))
print(j)

# str
# 独有功能
# upper/lower
# replace
# strip/lstrip/rstrip
# isdigit
# split / rsplit
# 补充：
# startswith / endswith
# 共有功能
# encode   count

name = '李杰' # 解释器读取到内存后，按照unicode编码存储：8个字节。
v1 = name.encode('utf-8')
print(v1)
v2 = name.encode('gbk')
print(v2)

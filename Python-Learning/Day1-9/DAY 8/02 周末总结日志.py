v = 'ALEX'
v1 = v.upper()
print(v1)
v2 = v.isupper() # 判断是否全部是大写
print(v2)

v = 'alex'
v1 = v.lower()
print(v1)
v2 = v.islower() # 判断是否全部是小写
print(v2)


############ 了解即可
v = 'ß'
# 将字符串变小写（更牛逼）
v1 = v.casefold()
print(v1) # ss
v2 = v.lower()
print(v2)


obj = open('a.txt',mode='wb')

# obj.write('中午你'.encode('utf-8'))
v = '中午你'.encode('utf-8')
obj.write(v)

obj.close()

# seek(光标字节位置)，无论模式是否带b，都是按照字节进行处理。

obj = open('a.txt',mode='r',encoding='utf-8')
obj.seek(3) # 跳转到指定字节位置
data = obj.read()
obj.close()
print(data)

obj = open('a.txt',mode='rb')
obj.seek(3) # 跳转到指定字节位置
data = obj.read()
obj.close()

print(data)

# .5 文件内容的修改
with open('a.txt',mode='r',encoding='utf-8') as f1:
    data = f1.read()
new_data = data.replace('飞洒','666')

with open('a.txt',mode='w',encoding='utf-8') as f1:
    data = f1.write(new_data)
# 大文件修改

f1 = open('a.txt',mode='r',encoding='utf-8')
f2 = open('b.txt',mode='w',encoding='utf-8')

for line in f1:
    new_line = line.replace('阿斯','死啊')
    f2.write(new_line)
f1.close()
f2.close()
with open('a.txt',mode='r',encoding='utf-8') as f1, open('c.txt',mode='w',encoding='utf-8') as f2:
    for line in f1:
        new_line = line.replace('阿斯', '死啊')
        f2.write(new_line)

v = 'aleX'
print(v.capitalize())
print(v.count('a'))
print(v.find('e'))
print(v.index('X'))
print(v.casefold())
print(v.center(20,'*'))
print(v.rjust(10,'&'))
print(v.ljust(8,'$'))

# format的多种方式

# 。partition(element)  将字符串分为三份： 前面，后面，自己
print(v.partition('l'))

print(v.title())

print(v.zfill(15))


a = '12345'
b = 'aeiou'
table = str.maketrans(b,a)
v = 'adsqwoufjaadsfqwerasdfa;sjdfasfd'
# v = '1dsqw45fj11dsfqw2r1sdf1;sjdf1sfd'
result = v.translate(table)
print(result)
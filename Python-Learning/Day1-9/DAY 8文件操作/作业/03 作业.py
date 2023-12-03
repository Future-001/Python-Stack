# 11.简述文件操作的打开模式
# f = open(path , encoding =   , mode =)
# with open (                   0 ) as f :

# 12.请将info中的值使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
f = open('readme.txt' , encoding = 'utf-8'  , mode ='w')
info = ['骗子，','不是','说','只有',"10",'个题吗？']
f.write('_'.join(info))
f.close()

sum=''
for i in info:
    sum+=i+'_'
print(sum.strip('_'))

# 14.请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
info = {'name':'骗子','age':18,'gender':'性别'}
#
# # 1.txt. 请将info中的所有键 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。
with open('readme1.txt' , encoding = 'utf-8'  , mode ='w') as f,\
   open('readme2.txt' , encoding = 'utf-8'  , mode ='w') as f1:
    sum=''
    for i in info:
        sum+=i+'_'
    f.write(sum.strip('_'))
    l1=[]
    for j in info.values():
        l1.append(str(j))
        print(j,type(j))
    f1.write('_'.join(l1))

# # 2. 请将info中的所有值 使用 "_" 拼接起来并写入到文件 "readme.txt" 文件中。

# # 3. 请将info中的所有键和值按照 "键|值,键|值,键|值" 拼接起来并写入到文件 "readme.txt" 文件中。
l1 = []
for i,j in info.items():
    li = [str(i),str(j)]
    l1.append('|'.join(li))
print(l1)

# 15.写代码
#
# 要求：
#     如文件 data.txt 中有内容如下：
#     wupeiqi|oldboy|wupeiqi@xx.com
#     alex|oldboy|66s@xx.com
#     xxxx|oldboy|yuy@xx.com
#
#     请用代码实现读入文件的内容，并构造成如下格式：
#     info = [
#         {'name':'wupeiqi','pwd':'oldboy','email':'wupeiqi@xx.com'},
#         {'name':'alex','pwd':'oldboy','email':'66s@xx.com'},
#         {'name':'xxxx','pwd':'oldboy','email':'yuy@xx.com'},
#     ]
l1 = ['name','pwd','email']
data = []
with open('data.txt',encoding='utf-8',mode = 'r') as f,\
    open('data1.txt',encoding='utf-8',mode='w') as f1:
    for i in f.readlines():
        i=i.strip()
        i=i.split('|')
        dic = {
        }
        for j in range(len(i)):
            dic [l1[j]] =i[j]
        data.append(dic)

    f1.write(str(data))

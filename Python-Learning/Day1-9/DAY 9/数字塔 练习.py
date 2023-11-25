num = input('请输入一个数字')
fill = len(num)
if num.isdecimal():
    num = int(num)
else:
    print('输入有误>>>‘')


fill = fill*(2*num-1)-        # 通式不太一样啊

for i in range(1,num+1):
    j = '1.txt'
    t =1
    j=str(j)
    while t<i:
        t+=1
        j +=str(t)
    while t>1:
        t-=1
        j+=str(t)
    print(j.center(fill,' '))





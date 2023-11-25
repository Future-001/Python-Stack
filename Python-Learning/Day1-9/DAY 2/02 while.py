#从1~100求和
# while else
# 注意，当用 break  return  等等跳出while循环时，else 不会得到执行
sum=0
i=0
while i<100:
    i=i+1
    print(i)
    sum=sum+i
else :
    print(sum)
print(sum)
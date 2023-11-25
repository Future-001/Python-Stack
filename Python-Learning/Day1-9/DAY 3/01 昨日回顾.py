# while else
flag = input("请输入数字： ")
while int(flag):
    # 千万别忘记了，input返回值是字符串类型的，此外，如果break return跳出循环则不执行else.
    name=input("请输入你的姓名 ：")
    num=input("请输入你的学号： ")
    flag=input("重新输入： ")
else:
    print("sorry , error")

# 格式化输出 ————>  针对字符串
age=input()
address=input()
msg ='''---------start-------------
name = %s
age  =%s
address =%s
,save is 1.txt%%    #此处必须要用%%
''' % ('kevin',age,address)
print(msg)

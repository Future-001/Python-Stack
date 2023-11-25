#用户交互  input  返回的数据类型为字符串型
name=input("请输入姓名： ")
age=input("请输入年龄：")
tel=input("请输入电话号码： ")

print('姓名：'+name+' 年龄：'+age+' 电话：'+tel)
print(type(tel))

#流程控制语句 if

username=input("用户名：")
passpord=input("密码： ")
code="NtsL"
your_code=input("验证码： ")
if your_code==code:
    if username=='kevin':
        if passpord=='101':
            print(" success!")
        elif passpord=='100':
            print("error, think again!")
        else :
            print("end , error")
    elif username=='零零七':
        print("零零七代码正确，但是此时不是你的登录时间！")
else :
    print("验证码错误，请重试")

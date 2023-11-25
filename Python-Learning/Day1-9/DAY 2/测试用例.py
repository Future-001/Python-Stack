print(3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2)

print(3>1 and 4>3)

code = 'alex'
count=0
while count<3:
    user_name = input('请输入用户名：')
    user_passpord = input("请输入密码：")
    your_code = input('请输入验证码：')
    if your_code == code:
        if user_name == 'kexin':
            if user_passpord=='110':
                print("登录成功！")
                break
        else :
            print("账号或密码错误，请重试，你还有 %d 次机会" % (2-count))
    else :
        print("验证码错误，请重试，你还有 %d 次机会" % (2-count))
    count+=1
else :
    print("错误次数过多，请稍后重试！")
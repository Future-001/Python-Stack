flag=True
while flag:
    username = input('请输入用户名： ')
    passpord = input("请输入密码： ")
    code = 'aaaa'
    your_code = input("验证码:")
    if your_code == code:
        if username == 'tylor' and passpord == '1234':
            print('登录成功')
            #flag=False
            break
        else:
            print("账号或密码错误,请重新输入。")
    else:
        print('验证码错误，请重试')



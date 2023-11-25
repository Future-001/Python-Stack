def sign_in():
    with open('D:/Code Files/Python/Python-Learning/Class-code/DAY 13/register.txt',encoding='utf-8') as f:
        count = 3
        while 1:
            if count>0:
                user_name = input('请输入用户名>>> ')
                passport = input('请输入密码>>> ')
                count = count - 1
                f.seek(0)
                for j in f:
                    j = j.strip()
                    print(j)
                    # user,pwd=j.split('|')   为什么元组的拆包这里不行了呢
                    user,pwd=j.split('|')
                    print('我很好奇，你得到了什么',user,'这是密码',pwd)
                    if user_name==user and pwd==passport:
                        print('登录成功')
                        return True
            else:
                break
            print(f'登录错误，你还有{count}次机会')
sign_in()


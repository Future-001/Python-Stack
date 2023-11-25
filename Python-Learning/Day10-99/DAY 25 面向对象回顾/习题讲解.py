class User:
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
class Account:
    def __init__(self):
        self.user_list = []
        # 用户列表, 数据格式 [user对象,user对象....]
    def login(self):
        username = input('请输入用户名： ')
        passpord = input('请输入密码：')
        for user in self.user_list:
            if username == user.name and passpord == user.pwd:
                return True
    def register(self):
        username = input('请输入用户名： ')
        passpord = input('请输入密码：')
        passpord2 = input('请确认密码：')
        if passpord == passpord2:
            user = User(username,passpord)
            exist = False
            for usr in self.user_list:
                if usr.name == user.name:
                    exist = True
            if exist == False:
                self.user_list.append(user)
                return True
            else:
                print('用户已存在 ')
        else:
            print('您两次输入的密码不一致 ')
    def run(self):
        opt = ['登录','注册']
        while True:
            for index,item in enumerate(opt,1):
                print(index,item)
            num = input('请输入你要进行的操作； ').strip()
            if num == '1':
                ret = self.login()
                if ret :
                    print('登录成功')
                else:
                    print('登录失败')
            elif num == '2':
                ret = self.register()
                if ret:
                    print('注册成功')
                else:
                    print('注册失败')
            elif num.upper() == 'Q':
                break
if __name__ == '__main__':
    obj = Account()
    obj.run()

# 进阶，一次执行的注册行为在之后所有的执行中，都能正常登录。就是存储在文件里面。
# 利用反射简化  if 判断语句
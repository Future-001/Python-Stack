# from conf.setting import *
from conf import setting
from conf.setting import *
from lib.common import limit_time

usr = ''
status = False

def register():
    if status == False:
        print('欢迎来到注册页面')
        # usr_file_path = os.path.dirname(__file__)+r'\usr_file'
        while True:
            Exist_status = False
            usr = input('请输入注册用户名:')   # 保证用户名不要重复也是一个问题呢
            pwd = input('请输入密码:')
            f1 = open(setting.member_information_path, mode='rb')
            f1.seek(0)
            if usr.isalnum():
                while True:
                    try:
                        if usr in pickle.load(f1):
                            Exist_status = True
                            break
                    except EOFError:
                        break
                f1.close()
                if Exist_status == False:
                    if 6<=len(pwd)<=14:
                        f = open(setting.member_information_path,mode='ab')
                        f.seek(0,2)
                        md5 = hashlib.md5(usr.encode('utf-8'))
                        md5.update(pwd.encode('utf-8'))
                        pickle.dump(usr + '|' + str(md5.digest())+'\n', f)
                        f.close()
                        USR_PATH = os.path.join(setting.usr_file_path,f'{usr}')
                        if os.path.exists(setting.usr_file_path):
                            pass
                        else:
                            os.mkdir(setting.usr_file_path)
                        os.mkdir(USR_PATH)
                        return
                    else:
                        print('密码长度不符，请重试(6-14个字符)')
                else:
                    print('用户已存在')
            else:
                print('用户名不符合规范，请重新输入(只能包括数字或字母)')
    else:
        print('请先退出后再进行新帐号的注册！')

@limit_time(2)
def login():
    global status, usr
    if status==False:
        print('欢迎来到登录页面')
        with open(setting.member_information_path,mode='rb') as f :
            count = 3
            while True:
                if count>0:
                    f.seek(0)
                    usr = input("请输入用户名：")
                    pwd = input('请输入密码：')
                    md5 = hashlib.md5(usr.encode('utf-8'))
                    md5.update(pwd.encode('utf-8'))
                    while True:
                        try:
                            if usr+'|'+str(md5.digest())==pickle.load(f).strip():
                                print(f'登录成功，{usr}欢迎登录！')
                                status = True
                                return usr
                        except EOFError:
                            break
                    print('登陆失败，请重试！')
                    count = count -1
                else:
                    print('登录失败次数过多，请稍后重试！')
                    return
    else:
        print('您已登录！')

@limit_time(2)
def article():     # 取巧了，用户名直接变成了全局的。。。。
    # usr_file_path = usr_file_path # os.path.dirname(__file__) + r'\usr_file'  # 为什么无法获取到全局的地址。。。。不是很清楚
    if status:
        print(f'欢迎{usr}访问文章页面！')
        while True:
            choice = input("""1：创作文章
2:导入md文件
3:回到主页面
请输入你所要进行的操作；""")
            if choice.isdecimal():
                choice = int(choice)
                if choice == 1:
                    article_name=input('请输入文章名称：')
                    article_path =os.path.join(setting.usr_file_path,usr,'article')
                    if os.path.exists(article_path):
                        pass
                    else:
                        os.mkdir(article_path)
                    with open(article_path+'\{article_name}.txt', mode='wt', encoding='utf-8') as f:
                        content = input(f'请输入{article_name}中所要添加的内容：')
                        f.seek(0,2)
                        f.write(f'创作时间：{time.strftime("%Y-%m-%d %H:%M:%S")}'+'\n')
                        f.write(content+'\n')
                        f.flush()
                elif choice ==2:
                    path = input('请输入要导入文章的文件相对路径：')
                    # 试了一下，目前的能力 要么绝对，要么直接相对
                    md_name = os.path.basename(path)
                    import_path = os.path.join(setting.usr_file_path,usr,'article')
                    # path = os.path.dirname(md_name)
                    # old_file = os.path.join(path,md_name)
                    if os.path.exists(import_path):
                        pass
                    else:
                        os.mkdir(import_path)
                    with open(os.path.join(import_path,md_name), mode='wt', encoding='utf-8') as f,\
                            open(path,encoding='utf-8',mode='rt') as f1:
                        f.write(f'导入时间: {time.strftime("%Y-%m-%d %H:%M:%S")}'+'\n')
                        for line in f1:
                            f.write(line)
                        f.flush()
                elif choice ==3:
                    return
                else:
                    print('输入有误，请重新输入！')
            else:
                print('输入有误，请重新输入！')
    else:
        print('请登录后操作')

@limit_time(0)
def comments():
    if status:
        print(f'{usr}欢迎来到评论页面！')
        usr_list = os.listdir(setting.usr_file_path)
        for i,j in enumerate(usr_list):
            print(i,j)
        while 1:
            usr_num = input('请输入你要访问文章的用户序号：')
            if usr_num.isdecimal():
                usr_num = int(usr_num)
                if usr_num in range(len(usr_list)) :
                    usr_article = os.listdir(os.path.join(setting.usr_file_path,usr_list[usr_num],'article'))
                    print('文章内容如下： ')
                    for i,j in enumerate(usr_article):
                        print(i,j)
                    while 1:
                        choice_article = input('请输入你要评论的文章序号：')
                        if choice_article.isdecimal():
                            choice_article = int(choice_article)
                            if choice_article in range(len(usr_article)):
                                article_path = os.path.join(setting.usr_file_path,usr_list[usr_num],'article',usr_article[choice_article])
                                with open(article_path,encoding = 'utf-8',mode = 'r+')  as f:
                                    comment_exist = False
                                    for line in f:
                                        if '评论区:' in line:
                                            comment_exist = True
                                    if comment_exist == True:
                                        f.write('\n')
                                    else:f.write('\n评论区:\n')
                                    f.write(f'      {usr}:\n')
                                    content = input('请输入评论内容：')
                                    sensitive_word = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
                                    for i in sensitive_word:
                                        if i in content:
                                            content = content.replace(i,'*'*len(i))
                                    f.write('     \t'+time.strftime('%Y-%m-%d %H:%M:%S   ')+content)
                                return
                            else:
                                print('输入不符，请重新输入')
                        else:
                            print('输入非法，请重新输入')
                else:
                    print('输入错误，请重新输入！')
            else:
                print('输入错误，请重新输入')
    else:
        print('请登录后操作')
@limit_time(0)
def diary():
    if status:
        print(f'{usr},欢迎来到日记页面！')
    else:
        print('请登录后操作')
@limit_time(0)
def star():
    if status:
        print(f'{usr},欢迎来到收藏页面！')
    else:
        print('请登录后操作')

def run():
    global status,usr
    status = False
    function_list = [login,register,article,comments,diary,star]
    while True:
        choice = input ("""1. 登录
2. 注册
3. 访问文章
4. 查看评论
5. 查看日记
6. 查看收藏内容
7. 注销账号
8. 退出整个程序
请输入你想进行的操作；>>>""")
        if choice.isdecimal():
            choice = int(choice)
            if choice in range(1,7):
                function_list[choice-1]()
            elif choice == 7:
                status = False
                usr = ''
            elif choice == 8:
                status = False
                usr = ''
                return
            else:
                print('输入有误，请重新输入')
        else:
            print('输入有误，请重新输入')


import sys
# sys 练习：   sys.argv
# "D:\Code Files\Python\Python-Learning\Class-code\DAY 22\作业\注册表.txt"
# cmd   python xxx.py 登录所需要的文件 用户名 密码 cp  文件路径  目的地址。     一共五个命令，因为argv[1] 是python文件名
#  cp   rm   rename
# 继续行动。
import shutil
import os
print(sys.argv)
if len(sys.argv)>=6:
    with open(sys.argv[1], encoding="utf-8") as f:
        f.seek(0)
        for line in f:
            usr, pwd = line.strip().split('|')
            if usr == sys.argv[2] and pwd == sys.argv[3]:
                flag=True
                print('登录成功')
                break
    if flag:
        if sys.argv[4]=='cp' and len(sys.argv)==7:
            if os.path.exists(sys.argv[5]) and os.path.exists(sys.argv[6]):
                filename = os.path.basename(sys.argv[5])
                dsn = os.path.join(sys.argv[6],filename)
                shutil.copy2(sys.argv[5],dsn)
            else:
                print('文件路径不存在')
        elif sys.argv[4]=='rm'and len(sys.argv)==6:
            if os.path.exists(sys.argv[5]):
                if os.path.isfile(sys.argv[5]):
                    os.remove(sys.argv[5])
                else:
                    shutil.rmtree(sys.argv[5])
        elif sys.argv[4]=='rename' and len(sys.argv)==7:
            if os.path.exists(sys.argv[5]) and os.path.exists(sys.argv[5]):
                if os.path.isfile(sys.argv[5]):
                    os.rename(sys.argv[5],sys.argv[6])
                else:
                    # 文件夹的重命名
                    shutil.move(sys.argv[5],sys.argv[6],copy_function=shutil.copy2)
    else:
        print('登陆失败')
else:
    print('输入的命令无效')
#  练习一下二分查找，从有序列表中找到某个数。[1,2,3,4,6,7,18,24,44,66,78,88,98,99]   找88
l1 = [1,2,3,4,6,7,18,24,44,66,78,88,98,99]
key = int(input('请输入你要查找的数字: '))
length =(len(l1)-1)
l2 = l1
while True:
    n = int(length/2)
    if n>1:
        if key>l2[n]:
            l2 = l2[n:]
            length = n
        elif key<l2[n]:
            l2 = l2[:n]
            length = n
        else:
            print('zhaodaole')
            break
    else:
        if key in l2:
            break



# 定义一个圆形类，半径是这个圆的属性  r = 5,r=10  能够计算圆形的面积和周长。
from math import pi
class Circle:
    def __init__(self,r):
        self.r = r
        # self.周长=2*pi*r     # 不建议这么写，为什么呢？  因为 周长和 r 相关了，，，改了 r 后面的参数没改
    def s(self):
        self.area=pi*self.r**2
    def l(self):
        self.zc=2*pi*self.r
圆1 = Circle(5)
圆2 = Circle(10)
print(圆1.__dict__,圆2.__dict__,)
print(圆1.__dict__,圆2.__dict__,)

#  定义一个用户类，用户名和密码是这个用户的属性。实例化两个用户，不同用户名和密码
        # 1. 登录成功之后才创建相应的用户对象
        # 2. 修改密码方法，先输入匹配后修改。

def login(usrname,pwd,path):
    with open(path+r'\注册表.txt',encoding='utf-8') as f:
        for line in f:
            usr ,passpord = line.strip().split('|')
            if usrname==usr and pwd == passpord:
                print('登录成功')
                return True

name = input('请输入用户名 : ')
password = input('请输入密码 : ')
path = "/DAY 22面向对象\作业"
ret = login(name,password,path)

import os
class Usr:
    def __init__(self, name, pwd):
        self.name = name
        self.passpord = pwd

    def change(self):
        old_pwd = input('请输入原密码：')
        new_pwd = input('请输入新密码：')
        with open(path+r"\注册表.txt",encoding='utf=8',mode='rt') as f,open(path+r'\临时注册表.txt',encoding='utf-8',mode='wt')\
        as f1:
            f.seek(0)
            for line in f:
                usr_name ,pwd=line.strip().split('|')
                if usr_name==self.name and pwd==old_pwd:
                    self.passpord = new_pwd
                    info = self.name+'|'+self.passpord+'\n'
                    f1.write(info)
                elif usr_name==self.name and pwd!=old_pwd:
                    print('原密码输入错误 ')
                else:
                    f1.write(line)
        os.remove(path+r'\注册表.txt')
        os.rename(path+r'\临时注册表.txt',path+r'\注册表.txt')

if ret:
    Usr(name,password).change()
else:
    print("登陆失败，账号或密码错误 ")
# print(usr1.__dict__,usr2.__dict__)


#  利用 walk  计算文件夹的总的大小
import os
g = os.walk("D:\\Code Files\\Python\\Python-Learning\\Class-code\\DAY 18")
size = 0
for i in g:
    print(i)
    path,dir_list,name_list = i
    for name in name_list:
        abs_path = os.path.join(path,name)
        size+=os.path.getsize(abs_path)

print(size)

# 继续完成人狗大战，你是人，狗是npc, 你一个回合，狗一个回合，  狗掉的血是一个波动数值，闪避的概率。
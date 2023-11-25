"""
========================================= 昨日回顾 =========================================
super：
        遵循的是 mro 算法，只在新式类中能使用，python2中需要自己添加参数  (子类名,子类对象)
封装:
        广义封装，
        狭义封装：
                私有化： 方法名，实例变量，静态变量私有化
                特点： 只能在类的内部使用，不能再外部使用
                私有的静态变量和方法不能被子类继承。（主要从原理出发）

内置函数：
        property： 将一个方法伪装成属性，实他调用的时候不用加括号
                    @函数名.setter
                    @函数名.delter
        判断一个变量是不是可调用的=====>  其实就是判断这个变量后面能不能加括号：  类就可以  callable

反射:  没有任何一门语言的源码是不用反射写出来的。
    hasattr
    getattr
    字符串数据类型的变量名，采用getattr(对象，'变量名') 获取变量的之
                    对象： 一切皆对象，所有，不局限于实例化的什么对象。


=========================================  今日大纲 =========================================

"""

# 反射的例子
class File:
    lst = [('读文件','read'), ('写文件','write'),('删除文件','remove'), ('重命名文件','rename'), ('复制','copy')]
    def __init__(self,filepath):self.path = filepath
    def write(self):print('in write func')
    def read(self):print('in read func')
    def remove(self):print('in remove func')
    def rename(self):print('in rename func')
    def copy(self):print('in copy func')
f= File('absldfo')
while True:   # 省略去了很多不必要的东西了。
    for index, opt in enumerate(File.lst, 1):
        print(index, opt[0])
    num = int(input('请输入需要进行的操作:'))
    if hasattr(f,File.lst[num-1][1]):
        getattr(f,File.lst[num-1][1])()

# 作业： argv 那个题，那里的很多的  if 想办法改为反射。
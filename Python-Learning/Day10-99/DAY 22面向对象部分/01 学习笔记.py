"""
========================================= 昨日回顾 =========================================
递归练习：
        遍历文件夹下的所有文件
        斐波那契数列
        三级菜单
        文件夹的总大小

二分查找：
        只对有序列表排序：   中间化为两半。然后比较和两侧数据的大小，大的往左走，小的往右走
sys:
    sys.path
    sys.argv         在执行python脚本的时候，写在python之后的所有的内容，形成了一个列表。
    sys.modules      查看已经加载到内存中的所有模块。

os  模块：
        和文件 文件夹相关的
        和工作目录相关的
        和执行操作系统命令相关的

        walk  操作符，很有效。。。。
                返回一个生成器：   （path , dir_list,file_list)

logging模块：
        排错   数据分析       操作审计
        普通的输出（文件、屏幕）
        切分日志（时间、文件大小）

shutil 模块：
        和文件相关的功能
=========================================  今日大纲 =========================================
面向对象：
        python 一切皆对象
面向对象的初识：
    一种新的编程思路：
    一些概念：
    一些语法：

面向过程： 想要一个结果 写代码， 实现计算结果
面向对象：  人狗大战有哪些角色 角色的属性和技能  两个角色之间是如何交互的

复杂的，拥有开放式结局的程序 比较适合面向对象开发
        游戏

1. 定义一个模子，用来描述一个事物
2. 具有相同的属性和动作

类和对象的关系：
        类 是一个大范围，是一个模子， 约束了事物有哪些属性，但是不能约束具体的值
        对象： 是一个具体的内容，是模子的产物，遵循了类的约束，同时给属性赋上具体的值
类有一个空间，存储的是定义在类中的所有的属性
对象也有一个空间，存储的是定义在 class中的所有的属性的具体值


实例化所经历的步骤：
        1. 类名()   之后，开辟一个内存空间
        2. 调用 __init__ 把空间的内存地址作为 self（可以改) 参数，传递到函数内部.
        3. 所有的这一个对象需要使用的属性，都需要和 self 关联起来
        4. 执行完 __init__ 之后，self 的空间会被自动返回到调用处（实例化的地方)

看一看狗的例子：他到底是传递给了谁，谁只是代表了一个数值，谁是真正的属性。

对象的属性/实例变量
实例/对象 = 类名() ---> 实例化的过长

必要的一个参数  self (可以是别的名字)


目前的疑问：
        如何进行两个或者多个类别的类的组合？实现类中所有的参数能都互相调用呢？
        如何避免在类中重复传递参数，甚至可能传递错误参数？、
        类中的方法的使用还不太熟悉。需要尽量在熟悉一下。

        甚至于函数中的一些东西也不太理解，主要关于函数调用这块，
        具体看看例子：  超级搞笑的案例
                     23期作业

类的寻址顺序：  主类 --> 当前类 -->  主类中的其余类


另一种方法：
self.xxx=xx()
self.xxx.xxxx=self  那么下面的东西就可以调用上面的属性了。
别忘记def  return  self.xxx才能使用。
"""


class Person:   # 类的名字
    def __init__(self):  # 方法，  必须叫  __init__
        # 这个缩进需要执行，但是下面继续缩进的内容是不执行的，
        '必须叫这个名字，不能改变，所有在一个具体的人物出现之后拥有的属性# 都写在这里。 原本的字典是一个容器，这里的容器是 self'
        self.name = 'alex'
        self.sex = '不详'
        self.job = '搓澡工'
        self.level = 0
        self.hp = 250
        self.weapon = '搓澡巾'
        self.ad = 1
alex=Person()  # 会自动调用类中的  __init__ 方法，一定是叫 __init__
wusir = Person()   # wusir 就是对象，通过一个类获取一个对象的过长，-----实例化


#  存储的顺序， class  __init__  然后 Person() 创建一个空间存相关信息。然后最后，将结果返回给 alex
class Person1:   # 类的名字
    def __init__(self,name,sex,job,hp,weapon,ad):  # 方法，  必须叫  __init__
        '必须叫这个名字，不能改变，所有在一个具体的人物出现之后拥有的属性# 都写在这里。 原本的字典是一个容器，这里的容器时 self'
        self.name = name   # 对象的属性/实例变量
        self.sex = sex
        self.job = job
        self.level = 0
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
        # print(self)  # 和对象拥有相同的地址。

    def 搓(self,dog):  # 必要的一个参数
        print('哇哈哈',self.__dict__)  # self能取到之前所有的值。
        dog.dog_hp-=self.ad
        print('%s 给 %s 搓了澡，%s 掉了 %s 点血' %(self.name,dog.dog_name,dog.dog_name,self.ad))


小白=Person1('小白','不详','清洁工',100,'无',10)
# 小白.搓(柯基)   # 和里面搓的 self 地址是一样的

# 属性的增加
小白.money=1000000
print(小白)
print(小白.__dict__)
# 属性的删除
del 小白.money
print(小白.__dict__)
# 属性的修改
小白.name='小黑'
print(小白.name)
# 属性的 查看
print(小白.ad,小白.__dict__,小白.__dict__['ad'])

wu=Person1('wusir','male','搓澡工',1000,'搓',110)
print(wu) # 每一个对象对应的 self 的地址都不一样的，


class Dog:
    def __init__(self,name,kind,hp,ad):
        self.dog_name=name
        self.dog_kind=kind
        self.dog_hp=hp
        self.dog_ad=ad
    def 舔(self,person):
        person.hp -= self.dog_hp
        print('%s 舔 了 %s ，%s 掉了 %s 点血' % (self.dog_name, person.name, person.name, self.dog_ad))
柯基=Dog('小豆豆','柯基',1200,199)
print(柯基.dog_name)
柯基.dog_name='穆拉'
柯基.dog_kind='柴犬'
print(柯基.dog_name,柯基.__dict__)
小白.搓(柯基)   # 和里面搓的 self 地址是一样的
柯基.舔(小白)




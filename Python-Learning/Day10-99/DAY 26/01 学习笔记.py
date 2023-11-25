"""
=========================================  今日大纲 =========================================
super：
        super的功能是 用来找父类？  不太对，和父类没什么关系
        在单继承的中，super就是用来寻找父类。
        在多继承中：
            super 是按照 类名.mro() 顺寻去寻找当前类的父类。（主要在于广度优先，广度优先的C3算法。）
            super().方法名()    在python3中，不需要传递参数，自动会帮我们寻找当前类的 mro顺序的下一个类的同名方法
                                在python2中，需要我们主动传递参数，（当前类名，子类的对象).函数名()
                                            这样才能帮组我们调用到这个子类的mro书勋的下一个类的方法
                                            在python2 的经典类中，不支持用 super 寻找下一个类
                                python2的新式类   super(D,self).func()

封装：
        广义的封装：
                将属性和方法装起来，外面不能直接调用了，在外面要通过 类名.   进行调用
        狭义的封装：
                将属性和方法藏起来，外面完全不能调用，只能在内部偷偷调用(注意，方法名前面加上  __  也是私有的方法）
                当在类中，给一个名字（实例变量/属性)加上了 双下划线  __ 之后，就变成了私有的实例变量/对象属性。
                所有的私有的内容或名字都不能在类的外部调用，只能在类的内部使用了
            使用私有的三种情况：
                            不想让你看
                            能看不能改
                            只能通过我给的方式改。
                封装的语法：
                        私有的静态变量
                        私有的实例变量（属性)
                        私有的绑定方法
                私有的特点：
                        能不能在类的内部使用？外部使用？子类中使用？
                原理：
                        如何变形？
                        在那里定义的时候变形？
                类中变量的级别，那些是python支持的？
                        其它语言中的数据的级别都有哪些？在python中有哪些？
                        public:  共有的，类内类外都能进行使用，父类子类都能进行使用。 ====>  我们之前的都是共有的
                        protect:  保护的，类内能用，父类子类都能用，类外不能用 （python没有这个类型  C++ JAVA)
                        private： 私有的，只有类内能用，其他的地方都不能用

    所有的私有化，就是为了让用户不在外部调用类中的某个名字。
    如果完成私有化，那么这个类的封装度就更高了，类中的各种属性和方法的安全性也越高，但是代码越复杂

    加了双下划线的名字为什么不能从类的外部调用了？
                其实没有真正的隐藏，只是对原来的属性进行了变形。改为了   _类名__属性
                在类中的 self.__属性名其实是自动换为了  self._类名__属性    进行调用的
                在类的外部根本不能定义私有的变量   就是说在在外部 类名.__属性 = xxx 不是私有变量
    在子类中能调用父类的 私有变量吗？
            私有的内容不能直接被私有变量（方法） 调用，====>  名字都不一样了。
            注意我们之前的解释， self.__xxx()   其实是将  __xxx()   替换为了   _当前所在类名__xxx()
                            所以调用的时候，一定要看看有没有   self._类名__xxx()  这个方法或属性。


"""
# super 例子
class User:
    def __init__(self,name):
        self.name = name
class VIPUser(User):
    def __init__(self,name,level):
        # User.__init__(self,name)
        super(VIPUser,self).__init__(name)  # 这里 self已经被传递进去了
        self.levwl = level
西西 = VIPUser('西西',25)
print(西西.__dict__)

# 封装
import hashlib
class Usr:
    __country = 'China'   # 私有的静态变量  只能在内部调用
    def __init__(self,name,pwd):
        self.name = name
        self.__pwd = pwd   # 这就成为了私有变量，外部无法查看，只能在内部查看
    def __get_md5(self):
        md5 = hashlib.md5(self.name.encode('utf-8'))
        md5.update(self.__pwd.encode('utf-8'))
        return md5.hexdigest()
    def get_pwd(self):    # 主要是为了让用户只能看，不能修改
        return self.__get_md5()
    def change_pwd(self):   # 表示用户必须调用我们自定义的修改方式来进行变量的修改
        pass
    def country(self):
        return self.__country
alex = Usr('alex','sbsb')
print(alex.get_pwd())
# alex.__get_md5()   # 这个方法变成私有的了，也掉用不到


# 在子类中能否调用父类隐藏的变量或方法？
class Foo:
    def __init__(self):
        self.__func()
    def __func(self):
        print('in Foo')
class Son(Foo):
    def __func(self):
        print('in Son')
Son()

# class Foo:
#     def __func(self):
#         print('in Foo')
# class Son(Foo):
#     def __init__(self):
#         self.__func()
# Son()   # 报错，因为没有 _Son__func()

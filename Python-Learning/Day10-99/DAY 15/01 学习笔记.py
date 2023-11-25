"""
========================================= 昨日回顾 =========================================
装饰器：开放封闭原则，只是对装饰器进行修改的，没有对原函数修改。 本质： 闭包
def wrapper(f):
    def inner(*args,**kwargs):
    """"执行被装饰函数之前进行的操作""""
        ret=f(*args,**kwargs)
     """"执行被装饰函数之后进行的操作""""
        return ret
    return inner

.__name__
time.localtime()
time.strftime()

=========================================  今日大纲 =========================================
自定义模块： 本质就是    .py 文件 封装语句的最小单位
自定义模块： 实际上就是在定义 .py 文件
             模块中 出现了 for 循环，if结构，变量定义，函数定义，可执行语句 ， 只定义不执行。

python 文件的运行方式：        
                     脚本方式； 直接用解释器执行程序或集成化软件执行（黑框  pycharm 等）
                     模块方式（导入方式）： 被其它模块调用，为导入它的模块提供资源（变量，函数定义，类定义）
                                利用 import 导入文件名就可以了。
                                自定义模块被其他模块导入时，其中的可执行语句会立即执行（不一定是好事儿，），不可执行语句不执行
                                无法判断有没有不可执行的语句，例如函数定义
                     
                     python当中，提供了一种 判断自定义模块是属于开发阶段还是可以使用的阶段， __name__  ---->> 可执行语句可控了
                    直接出现在一个自定义模块当中：  脚本方式运行时，固定的字符串，    __mian__    \
                                                导入方式运行时： 如果在原自定义模块中写了 __name__ 那么，在调用\
                                                                该模块的 文件中，会显示你所调用的模块的名字。
                                                                        看实例
                            为了让在调用的时候，先不执行，我们采用：
                                        在自定义模块中  if __name__='__main__':
                                        同时，将可执行的语句封装为一个函数，直接在原函数 if判断后选择是否执行就可以了
  
        __name__ 属性的使用：
                      在脚本运行时： __name__ 就是 显示的本模块的名字
                      在模块调用时：  __name__显示的是你所调用的模块的名字  
              
         一旦进行了模块的调用： 就可以使用自定义模块了  例如 
                        import __init__module
                        __init__module.main()   就是所调用的模块名.所要调用的模块里面的那一部分        
 
系统自定义模块的调用： 我们自定义的模块，现在是在 同一路径下 可以找到，如果不在同一路径下，找不到了？      
                    但是，为什么系统的模块，例如 time os 可以直接用呢？
                    怎样进行调用的
                
                系统模块的调用顺序： 
                    内存中：   如果之前成功导入过某个模块，直接使用已经导入的模块
                    内置路径中： 安装路径  lib  第三方包
                    PYTHONPATH: 这也是 Import时候寻找模块的路径，但是用的很少，这才是系统路径，用了可能会冲突
                    sys.path : 这是一个路径的列表， 这就是当前函数所在的一些路径 ，动态的添加的
                        查看 sys.path 里面的内容  
                        
                    为了执行不在同一路径下的 自定义模块： 我们得修改 sys.ptah 里面的路径，得加入我们自定义的模块的路径  
                    例子如下： import sys
                              sys.path.append(r'一段路径')   这就可以进行模块的导入了
                               
                            但是有点low 啊，每次都得去寻找 绝对 路径，万一自定义模块在子目录中，这样输入太麻烦了，怎么操作呢

            __file__  : 查看当前模块(文件)所在的 绝对路径，
            使用 os 模块获取到当前文件的 父路径，
                    import os
                    os.path.dirname(__file__)
                    sys.path.append(os.path.dirname(__file__)+'\\aa')  假设有那么一个子文件夹，子目录
                            我的另一种方法：(还没想好，思路是 先找到父路径，然后根据 __name__ 还有但是得导入才有 name ....) 错了
                            sys.path.append(os.path.dirname(__file__)+__name__
 
导入模块的多种方式：
                import xxx  : 导入一个模块的所有成员  ，必须使用模块的名字作为前缀  
                import a,b,c :  一次性导入多个模块的成员
                 from xxx import xxx   例如： form functools import reduce   从某个模块中导入某些成员      
                 
                import xxx  和 from xxx import * 的区别：  
                        二者功能一样，但是使用有区别：   第二个直接使用成员名就可以了，
                        举例：  第一个;  在调用成员时候   必须是  模块名.成员名
                                第二个：  调用时候：  直接     成员名 就可以使用模块中的成员 ，但是可能命名冲突   
                            解决命名冲突的问题i::   
                                                import xxx
                                                避免同名
                                                别名 
                            使用别名：  alias（英文单词是 别名, 不是 as )    我们用的是 首字母和尾字母
                            from xxx import xxx as xxx  
                            
                            我们使用别名肯定是为了避免和其他的模块同名，肯定是要改的是   导入的模块的成员的别名
                            from xx import *.成员 as xx
                            给模块起别名：  import xxx as xxx 模块太长，写短一点啊。可以了
                
                from xxx import * 默认所有成员都可以被导入，
                                    但是成员太多呢？   
                                    我们利用 __all__ 生成  列表  列表里面是所有可以被外界使用的成员，
                                    也就是说，在原来的模块中，可以使用 __all__ 指定，本模块那些成员对外界是开放的，可以调用的， 
                                    注意  __all__ 列表里一定要是字符串
                                    注意  __all__ 只是对from xxx import * 起作用，别的导入方式不起作用

相对导入： 针对某个项目中的不同模块之间的导入， 
        给你一点实例理解一下：  具体看一看 x,y,xx.py文件
                    import sys
                    inport os 
                    第一种一个项目下的导入
                    sys.path.append(os.path.dirname(__file__)+'\DAY 13')  # 先将目录导入  然后就可以导入其中的模块了
                    太麻烦了，不用
                    
                    第二种： 相对导入
                    1.txt. 同级目录项目下： 
                    假设，DAY 15 下面有 三个文件夹，结构如下， x 文件夹（项目)，含有 y z 文件夹 里面分别由 yy zz 模块
                    在 zz  模块中导入 yy 模块 ：   from ..y import yy     ..y  从当前模块的包的父级包中导入 yy 模块
                    
                    2. 非同级目录下，需要先将项目的父路径加入路径
                    同理。我们要对 01 学习笔记模块导入 yy 模块
                    sys.path.append(os.path.dirname(__file__))    
                    from x.y import yy  # 因为此时 x 文件和 01 学习笔记模块 已经是同级项目了 
                     
                     错误写法：
                    sys.path.append(os.path.dirname(__file__)+'xx')    
                    from y import yy   # 不需要将 yy 模块的项目的父路径也导入进来 就可以了，然后 用  . 
                    
                    如果两次引用了  yy.zz.age  但是暴露了我们还引用了 zz 但是，      
                    
相对路径： 只有一种格式  from 相对路径 import xxx   包含了点号的一个相对路径
                . 表示的是当前路径  （就是含有这个模块的 文件夹）
                ..  表示的是父路径   （就是含有这个模块的 文件夹的父文件夹）
                ...  表示的是父路径的父路径   后面加点，父路径下面的子文件夹   
                
                                                                  
常用模块：  random
此模块提供了和随机数获取相关的方法：
        random.random() 获取【0.0,1.txt.0) 范围内的浮点数
        random.randint(a,b)   获取 【a,b】 中间的一个整数
        random.uniform(a,b)  获取 【a,b) 内的浮点数 b,可以取到也可以取不到，不一定的
        random.shuffle(x):  混洗 也就是将x 打乱，一定是可变的数据类型。
        random.sample(x,k)   从 x 中随机抽取 k 个数据以列表返回
        
#  * 的用法补充
a,b,*c=(1.txt,2,3,4,5)
print(a,b,c)
a,*b,c=[11,22,33,44,55]
print(a,b,c)

"""
# 模块的导入方式的执行模式：
import __init__module


# 直接导入就被执行了，那我先判断是不是还需要开发呢？
#  __name__    显示的是   __init__module
print(__name__)   # 但是这里还是会被执行，因为你只是显示了 你所调用模块的名字


print()
print(f'要使模块不执行，需要在模块中添加一部分东西 ，具体去看自定义模块把 ,加入了 if 判断之后，是不是就不执行啦  ')

#  所调用的模块名.所要调用的模块里面的那一部分
__init__module.main()

# 查看 sys.path 里面的内容
print()
import sys
print(sys.path)

# 在系统路径里面添加自定义模块的路径 这就可以了啊
# sys.path.append(r'D:\Code Files\Python\Python-Learning\Class-code\DAY 13')
# 利用绝对路径去找，有点low ，下面我们采用相对路径（动态）去找

print(__file__)   # 输出当前文件的绝对路径
# 使用os 模块获取 一个路径的父路径
import os
print(sys.path.append(os.path.dirname(os.path.dirname(__file__))+'\DAY 13'))  # 后面的 ' ' 里面可以加下属的文件夹

import 人事管理系统
print(人事管理系统.personnel())

print(sys.path)

# 控制了那些成员不让外界用
from __init__module import *
print(age1,age2)

# print(age3)出错了

import random
print(random.random())
print(random.uniform(0,2))
print(random.shuffle([1,2,3, 56]))
print(random.randint(1,7))
print(random.sample([1,2,3,'熟练工'],2))

#  * 的用法补充
a,b,*c=(1,2,3,4,5)
print(a,b,c)
a,*b,c=[11,22,33,44,55]
print(a,b,c)
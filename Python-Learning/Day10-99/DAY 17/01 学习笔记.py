"""
=========================================  今日大纲 =========================================
再说自定义模块：
模块是什么？
            抖音  20w行代码，全部放在一个 py 文件中：
                                        缺点：代码太多，读取代码 读取时间很长  代码不容易维护
            所以我们应该将其拆解为 好几个py文件，这些py 文件又有相同的功能，冗余，此时要将这些相同的函数提取出来  input print 等等功能
            time.time()f   os.path ....放在一个文件中，想用的时候，拿来就用
            类似这个py文件： 常用的相似的功能的集合

            模块就是一个 py 文件（ 常用的相似的功能的集合）

            # 作用：提高开发效率；便于管理和维护

    什么是脚本： 他其实就是一个 py 文件，长期保存代码的文件

模块的分类： 内置模块：python解释器自带的模块  time  os  sys hashlib 等等
           第三方模块：  pip install   例如 Beautiful_soup ,request , Django, flask 等等
           自定义模块：  自己写的一些 py 文件。

import 的使用
        直接利用 import ,模块就被执行了 ，除非  判断   __name__
        如果模块已经被加载到内存了，就不再重复执行。

        第一次导入模块流程：
                    1.txt.  在内存中开辟一块 要以调用的；模块命名的一个名称空间 ，注意 被导入的模块拥有单独的名称空间‘，\
                                互不影响的就是有同名变量的话，如果通过  import xxx   x. 同名不会影响
                                虽然导入的模块的 名称空间不是同一个，但是，在主函数中还是有模块里面函数的地址，但是
                                这个函数的地址 是从模块的原函数的地址拿过来的，二者地址是一个
                    2.   执行此名称空间中的所有可执行代码，将其中的所有变量与值的对应关系 加载到这个名称空间
                    3.    引用通过  模块名.   的方式，调用模块中的内容

复习一下上次的  __file__  sys.path.append()   os.path.dirname()       __all__

为模块起别名：  alias  简单便捷，有利于代码的优化    统一了一个接口。 比如连接不同的数据库 ，直接给他们起一个统一的名字，就不用每次都改了
                例如  .index()    str.index()   list.index()

import 的导入方法：   import xxx
                    from xx import *
                                二者区别：  后者不需要前缀，用起来更方便， 但是容易产生命名冲突，就近原则，覆盖同名变量

                    例如：  看一看 kevin  和 mette 中的例子

                    避免名称冲突的方法：   不用  import *   ；  起别名  ；   __all__=[]  但是 它一定配合 * 使用

py 文件的两种功能： 自己用： 脚本   别人用：  模块

__name__ == :       当作脚本使用的时候结果是     '__main__'
                    当作模块使用的时候 ，    模块名
                根据扮演的角色不同，可以得到不同的结果。
                        模块需要调试时，利用 if __name__ == '__main__': 然后执行代码
                        作为项目的启动文件：  待续

模块的搜索路径：
                三层：  从 内存中找，其次，从内置模块中找，最后，从 sys.path 中寻找
                解释器会自动地将一些内置内容（内置函数，内置模块）加载到内存中，
                绝对路径的引用：  sys.path.append(os.path.dirname(__file__))    from ..y.yy import *  注意 __call__

================================================================================================================
序列化模块：  将一种数据结构 转化成特殊的序列，然后还能转换回去 （ json 里面的元组注意)
为什么存在序列化?
        数据存储在文件中，是以 str （bytes)形式存储的， 比如字典。
        数据通过网络传输，（最终要转换为 bytes 类型，但是字符串才能和 byte 类型互换） , str 不能还原回去

序列化模块：

         json :
            将数据结构及转换为特殊的字符串，并且可以转换回去
             .dumps(element)   .dump(element,fp)   .loads(element)   .load(fp,element)

                            dic = { 'name': '太白','time': 'slkg'}
                            r = json.dumps(dic,ensure_ascii=False)
                            print(r,type(r))
                            print(json.loads(r),type(xxx))
                            主要用于网络传输，但是也可以读写文件

                            .dump()   .load()  一次只能写入或者读取一个数据结构

                一次写入文件多个数据，只能用 dumps(elem,fp)  以及  loads(fp,element)


        pickle :  将数据结构转换为字节串，并且无论何种数据结构，都可以转换回去
                    dumps  和  loads  只能用于网络传输。
                    dump    load  这个就可以 多次写入和多次读取出来  （用于文件的读取）
                                  多次读取，每次都是一行（特殊的行）
                                  可以读取 各种类型 ，例如函数名


总结：  json 主要用于将 其他数据类型转换为 str 进行网络传输，

===========================================================================================================

hashlib  模块：  包含很多的加密算法，  md5 , sha2566 sha512
用途：  密码加密，密文形式存储
        文件的校验：

用法： 将bytes 类型的字节转换为一定长度的 字符串。。。    可能会用到  .encode()
        不同的 bytes 用相同的算法一定不同， 相同的bytes 不同加密算法 一定相同   hashlib 不可逆（亦被破解）

        三步法：   .md5(xxx)  或者  .md5()    .update()
          .hexdigest()    .digest()    获取加密后的结果。
          获取加密后的结果，写入文件，对文件进行加密，然后登陆的时候可以验证一个东西是不是正确的。

        加盐方式：   salt
                        三部曲：    .md5(xxx.encode('utf-8')
                                  .update(x)    .hexdigest()

        sha 系列：
            随着sha 谢列数字越高，加密越复杂，越不容易破解，但是 时间越长

python  一切皆对象  Linux 一切皆文件
liunx 一切皆文件，无论下载什么视频，文件，软件等 都会带有一个 md5 数值，用于校验文件是否时可行的（例如 带病毒的或者完整的）
# 例如： 下载一个文件，安装之前，可以校验一下，  同时 ，md5 可以分着读取 还可以最终组合成为同一个校验码 ，但要注意 一个都不能少。

        s1 = '我是kevin,  我今年8岁了'
        r = hashlib.md5(s1.encode('utf-i8'))  r = r.update()


这里是不是就能对文件进行循环了呢，但是注意，是不是 1024字节了呢？ low 的方法是全部读取出来， 然后校验，
高大上的方法，就是 一次只读取一部分，最后进行了拼接

===============================================================================================================


"""
import hashlib
s1 = '我是kevin,  我今年8岁了'
r = hashlib.md5()
r.update(s1.encode('utf-8'))
print(r.hexdigest())

# ==========================================================================
# 可以分着读取一下：
ss ='活在当下 , 很不错的啊 ， 看看她怎么样 你觉得呢'
sha = hashlib.sha224()
sha.update(ss.encode('utf-8'))
print(sha.digest())

sha224 = hashlib.sha224()
sha224.update('活在当下 ,'.encode('utf-8'))
sha224.update(' 很不错的啊 ， '.encode('utf-8'))
sha224.update('看看她怎么样 你觉得呢'.encode('utf-8'))
print(sha224.digest())    # 就是可以分段进行加密，最后接到一起

# ====================================================================================================
# 加盐操作了：
sh1 = hashlib.sha256('我的梦想'.encode('utf-8'))
sh1.update(ss.encode('utf-8'))
print(sh1.digest())

# 动态加盐操作
sh2 = hashlib.sha384(ss[::2].encode('utf-8'))
sh2.update(ss.encode('utf-8'))
print(sh2.digest())

# ====================================================================================================
# 登录程序
import hashlib
import pickle

def wrapper(f):
    def inner(*args ,**kwargs):
        ret = f(*args ,**kwargs)
        return ret
    return inner

@wrapper
def register():
    print('欢迎来到注册界面： ')
    usr = input('请输入用户名: >>> ')
    pwd = input('请输入密码：>>> ')
    pwd = bytes(pwd ,encoding='utf-8')
    md5 = hashlib.md5(usr[::2].encode('utf-8'))
    md5.update(pwd)
    with open('信息表.txt' ,mode = 'ab') as f :
        f.seek(0,2)
        pickle.dump(usr +'| ' +str(md5.digest()) ,f)

        # f.write(usr+'|'+str(md5.digest()))
    return

@wrapper
def login():
    print('欢迎来到登录界面：')
    global status
    with open('信息表.txt',mode='rb') as f1:
        count = 3
        while 1:
            username = input('请输入登录账户名： >>> ')
            password = input('请输入登录密码： >>> ')
            # 进行动态加盐操作
            md_5 = hashlib.md5(username[::2].encode('utf-8'))
            md_5.update(password.encode('utf-8'))
            if count>0:
                f1.seek(0)
                while 1:
                    try:
                        if pickle.load(f1 )==username +'| ' +str(md_5.digest()):
                            print(f'欢迎登录，{username}')
                            return
                    except EOFError:
                        break
                print('登陆失败！')
                count = count - 1
            else:
                print('失败次数过多，请稍后再试 ')
                break



def home():
    print('请选择你要进行的操作： 1> 登录 2> 注册 3> 退出')
    l1 = [login ,register]
    global status
    status = False
    while True:
        choice = input('请输入你的选择>>> ')
        if choice.isdecimal():
            choice = int(choice)
            if choice in range(1 ,3):
                l1[choice-1]()
            elif choice==3:
                return
            else:
                print('输入非法，请重新输入 ')
        else:
            print('输入非法，请重新输入 ')
home()
"""
             # for j in f1:
            #     j = j.strip()
            #     usr,pwd=j.split('|')
            #     if usr==username and pwd == md_5.digest():
            #         print(f'登录成功，{usr}欢迎来到XXX')
            #         status = True
            #         return
            #     else:
            #         print('登陆失败，请重试！')
 """

# =======================================================================================
# 文件安全性校验
def file_check(file_path):
    with open(file_path,mode='rb') as f1:
        sha256 = hashlib.sha256()
        while 1:
            content = f1.read(1024)
            if content:
                sha256.update(content)
            else:
                return sha256.hexdigest()
print(file_check('pycharm-professional-2019.1.1.exe'))

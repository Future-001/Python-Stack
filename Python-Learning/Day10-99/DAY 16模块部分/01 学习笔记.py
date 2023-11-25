"""
========================================= 昨日回顾 =========================================
自定义模块：
模块的两种执行方式：
导入模块的几种方式
__name__      __file__      __all__     os.path.dirname(__file__)
import sys
sys.path 是列表
模块的匿名
相对导入：
random 模块    .random()    .randint(a,b)   .shuffle()    .uniform(a,b)    .sample(x,k)

=========================================  今日大纲 =========================================
常用模块的介绍：

time:
     获取时间戳和字符串形式的时间的一些方法，
     从格林威治时间（时间元年） 开始,从时间节点到现在的 s秒 数    time.time()
     获取格式化的事件对象： 、
                    time.gmtime(args)    GMT 时间：  使用默认的时间戳获取格式化事件对象
                            返回的是   格林威治时间（西区和东区）    都是9个时间对象组成
time.struct_time(tm_year=2023, tm_mon=10, tm_mday=19, tm_hour=13, tm_min=15, tm_sec=40, tm_wday=3, tm_yday=292, tm_isdst=0)
                    time.localtime()   获取自己时区的对象
                             如果往里面传参数，传的是 秒数，就是时间元年往后的秒数 从时间元年上面往后加

    格式化输出时间字符串
                    time.strftime('%Y-%m-%d %H:%M:%S',t)   (format,time)  默认是本地时间 lobaltime()
                                $ 里面的内容可以随机替换    将 某个时间 转换为某种格式
                    time.strptime(str,format)   将某个时间字符串解析为某种格式，格式必须一一对应，
                             # 格式必须一一对应  没指定，那么默认是 0
                            # 如果日期没有指定的话，没有 0 年 0 月 0 日  不能是 0 的话那么会被赋值为 1.txt
                    time.mktime(time-varible)  就是将一个时间转转化为时间戳（格林威治）

                    time.sleep(xxx)  暂停当前时间，睡眠 xxx 秒

datetime:   日期时间模块
            包含的是一些类，不是单纯的方法, date  time  timedelta
            date 类:
                    datetime.date(2010,10,8)    年月日   2010-10-8
                        既然是类，那么可以获取他的属性   datetime.date.year     .month   .day
            time 类：
                    datetime.time(10,48,59)    时 分 秒
                         也有相应的属性    .hour   .minute   .second
            下面有一个直接的二者的 总结的一类
               datetime 类 所有的属性了   主要用于数值计算   不要超界哈，一小时多久，一分钟多久

            timedelta:  时间的变化了  就是 时间变化量 差值
                    datetime.timedelta(days=0,hours=0,....)    # (days, hours....seconds, microseconds)
                    怎么进行数学运算：  创建时间对象,和  date  datetime timedelta 进行加减 即可
                                                只有这三个可以进行计算，time 不可以进行计算
                    时间变化量的计算，会产生进位或者借位  ,计算后的 数据类型是： 原来更大的 时间类型
                                        就算会超出去，他也不会变化 例如  2020-10-1.txt 加上 1.txt 天20 秒，不会显示 秒

os：
        os.remove('file_name')  记得可能要加路径 ， 绝对路径前面记得加 r
        os.rename(old_name,nex_name)
        删除目录：  必须是空目录才可以删除
                    os.removedirs('path') 路径一定要是字符串  不放在回收站当中
                如果目录不为空：
                    1.txt，先进入底层，删除最内层目录中的文件删完，然后再删除文件夹
                    2. 使用另一个模块  shutil   (shellutility)
                    import shutil
                    shutil.rmtree('path')

        和路径相关的操作，被封装到 os.path 模块当中去了。
         os.path.   去看看里面都有哪些函数
         os.path.dirname(file)  取到后面的文件所在的文件夹的 路径
                                不判断路径是否存在 os.path.dirname(r'/aa/bbb/ccc.txt')

        os.path.basename(file)    获取 文件名,就是取到最里面的文件的名字
                            os.path.dirname(r'/aa/bbb/ccc.txt')   --->  ccc.txt

        os.path.split('path')   将一个路径中 路径 和 文件名称 切分开 成为一个二元组

        os.path.join('pahtdir','path',...)   进行路径的拼接，可以拼上文件
                                os.path.join('d:\\','ccc','aaa','ddd.txt')

        os.path.abspath(path)  获取到一个路径的绝对路径   如果是  / 开头的路径默认是在当前盘符下，
                                如果不是 / 开头，就是当前的路径

        os.path.isabs(path)   是不是绝对路径
        os.path.isdir(path)    # 真实去找 后面看是不是目录  因为 文件名 可以是  a.data  或者  a.txt
        os.path.exists(path)   判断文件是否存在
        os.path.isfile(path)    看看是不是文件，真实去找了
        os.path.islink(path)    window 快捷方式的

sys:
      获取命令行方式运行的脚本后面的参数
      import sys
      sys.argv[where]   获取到传入的参数的列表   第零个参数是脚本名，第一个开始才是其中真正的参数
      print(sys.argv[1.txt])   #str 类型传入的参数

      # 有如下代码：
                import sys
                print('脚本名',sys.argv[0])
                print('第一个参数',sys.argv[1.txt])   # hello
                print('第二个参数',sys.argv[2])   # world
                arg1 = int(sys.argv[3])
                arg2 = int(sys.argv[4])
                print(arg1+arg2)    #  3
                在命令行中   执行 python sys.argv[10] hello world 1.txt 2

    sys.path  解释器找模块的路径
    sys.modules   返回系统以及加载的模块

判断一个东西后面加入加括号   c 类  s 方法  一般加括号
                        v 的话，属性，不用加括号

绝对路径： 从盘符开始定位的路径
相对路径： 从当前文件开始定位的路径

"""
import time
print(time.time())
print(time.gmtime())
print(time.gmtime(10))
print(time.localtime(10))
print(time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime(19)))
time.sleep(3)
print(time.strftime('%Y-%m-%d  %H:%M:%S'))
print(time.strptime('2000-08-24','%Y-%m-%d'))   # 格式必须一一对应  没指定，那么默认是 0
# 如果日期没有指定的话，没有 0 年 0 月 0 日  不能是 0 的话那么会被赋值为 1.txt

import datetime
print(datetime.date(2011,1,1).year)
print(datetime.date(2011,1,1).day)
print(datetime.time(18,1,1))
print(datetime.time(18,1,1).hour)
print(datetime.datetime(2011,1,1,18,1,1))
print(datetime.datetime(2011,1,1,18,1,1).hour)

d = datetime.timedelta(days=1,hours=11)
print(d)   # (days, seconds, microseconds)
# 如何进行计算
dt = datetime.datetime(2010,10,10)
print(dt - d)


# 练习： 计算某一年的二月份有多少天，
# 普通算法，看他是不是闰年  利用 timedelta  创建三月一号  ，然后输入年份 根据时间取减少一天就知道有多少天了
d1 = datetime.timedelta(days=1,hours = 1)
ye = input("请输入年份")
dat = datetime.date(int(ye),3,1)
print(dat  - d1)   #  不会显示小时的，数据类型就是大的操作数的类型
print((dat  - d1).day)

# ==========================================================================================
print(time.gmtime(4))
print(time.localtime(5))   # 只要加上了 移动的秒数，都是在格林威治的时间之下进行移动，只是更改一下时区。

print(time.strftime("%Y-%m-%d %H：%M:%S "))  # 后面的参数默认
print(time.strptime("1985-03-10","%Y-%m-%d"))
# print(time.strptime("21:06:80","%H:%M:%S"))    超界就错了



print(time.strptime("21:06:50","%H:%M:%S"))


c = datetime.date(1992,3,5)
print(c.day,c.year)

c = datetime.time(12,35,59)  # 超界一定错误
print(c.hour,c.second,c.minute)

c =datetime.datetime(1222,11,22,14,55,29)
print(c.year,c.month,c.second)

b = datetime.timedelta(days=366,hours = 10)
print(c+b)

c =datetime.timedelta(days=1,hours=1)
print(datetime.date(1991,2,1)+c)
print(datetime.date(1991,2,1)-c)  # 忽略了时间？  1991-01-31

c =datetime.timedelta(hours=1)
print(datetime.date(1991,2,1)-c)  # 忽略了时间  1991-02-01


# =======================================================================================
import sys

print(sys.modules)
print(sys.argv)  # 如果有的话，返回一个列表，列表第一个是程序名称
# print(eval("sys.argv[1.txt]+sys.argv[2]"))   # 必须在系统个运行框 里面 才起作用

import os
print(os.path)
print(os.name)
print(__file__)

import shutil
# shutil.rmtree('file1')
# os.remove('1.txt')

os.path.dirname(r'/aa/bbb/1111.py')     # 不判断路径是否存在
print(os.path.basename(r'/aa/bbb/1111.py') )    # 不判断路径是否存在  获取文件名就可以

print(os.path.abspath('/测试.py'))   # 如果以 / 开头，就是当前盘符下的路径
print(os.path.abspath('DAY 17/测试.py'))

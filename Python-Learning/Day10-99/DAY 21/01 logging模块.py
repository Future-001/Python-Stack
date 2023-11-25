"""
========================================= 昨日回顾 =========================================

=========================================  今日大纲 =========================================
logging  模块：
        为什么要写log：
                排除错误
                用于做数据分析
        购物商城 --- 数据库里
            什么时间买了什么东西
            哪些商品被加入购物车了
            一个用户什么时间在什么地点，登陆了购物程序
            搜索了那些信息，事件被展示出来了
            什么时候关闭了软件
            对哪些商品点进去看了？
        10w 用户：
            1w
            十几万条数据，购买相关的信息。那些要放在数据库里面呢？

        数据库是有限的，哪些数据要放呢？

需要用来做数据分析（大数据）的东西，需要写入 log 日志里面：
        看看某某人，某时间，做了什么事，或者查看故障，里面的哪一环节出现问题了。查看日志。
        1. 用来记录用户的行为 --- 数据分析
        2. 距离用户的行为 ----- 操作审计
        3. 排查代码当中的错误


# 一定要注意写 log  开发和运维。

写日志的模块， logging 模块 ，是内置模块
输出的内容是有等级的。   默认处理 warning 级别以上的所有信息。
logging.debug('debug message')      调试
logging.info('info message')        信息
logging.warning('warning message')  警告
logging.error('error message')      错误
logging.critical('critical message')    批判性的,关键的。

例如：
def cal_mul():pass
def cal_div():pass
def cal_add():pass
def cal_sub():pass
def cal_inner_bracker():pass
def main(exp):pass

logging.basicConfig(level=logging.DEBUG)

1. 无论你希望日志里打印什么东西，里面的内容是你自己写进去的。没有自动生成这回事儿
2. 日志的格式可以设置的：     logging.basicConfig
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[file_handler,],
    level=logging.ERROR
)

如果要输出到文件，加上 filename = 'xx.log'     默认追加行为，还可以该 filemode ='w'
同时可以设置输出的等级      level
乱码：  同时输出到屏幕和文件： 同时解决的。
fh = logging.FileHandler('xxx.log',encoding = 'utf-8')
sh = logging.StreamHandler()
同时在 logging.basicConfig中，删除 filename  ,在其中 hindlers = [fh,sh]   可以写多个，。这样就正常了。



                    logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有：

                    filename：用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
                    filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
                    format：指定handler使用的日志显示格式。
                    datefmt：指定日期时间格式。
                    level：设置rootlogger（后边会讲解具体概念）的日志级别
                    stream：用指定的stream创建StreamHandler。可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，
                    默认为sys.stderr。若同时列出了filename和stream两个参数，则stream参数会被忽略。

                    format参数中可能用到的格式化串：
                    %(name)s Logger的名字
                    %(levelno)s 数字形式的日志级别
                    %(levelname)s 文本形式的日志级别
                    %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
                    %(filename)s 调用日志输出函数的模块的文件名
                    %(module)s 调用日志输出函数的模块名
                    %(funcName)s 调用日志输出函数的函数名
                    %(lineno)d 调用日志输出函数的语句所在的代码行
                    %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
                    %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
                    %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
                    %(thread)d 线程ID。可能没有
                    %(threadName)s 线程名。可能没有
                    %(process)d 进程ID。可能没有
                    %(message)s用户输出的消息

日志的切分： 每次只需要上传一些就行了，比如最近的。
import time
import logging
from logging import handlers

sh = logging.StreamHandler()
rh = handlers.RotatingFileHandler('myapp.log', maxBytes=1024,backupCount=5)
fh = handlers.TimedRotatingFileHandler(filename='x2.log', when='s', interval=5, encoding='utf-8')
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
    handlers=[fh,sh,rh],
    level=logging.ERROR
)

for i in range(1,100000):
    time.sleep(1)
    logging.error('KeyboardInterrupt error %s'%str(i))

"""
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s[line: :%(lineno)d]-%(module)s:  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %p',
)
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
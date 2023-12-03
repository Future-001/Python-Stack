"""z--->x
做几个测试吧，相互引用，主要是练习 __all__
练习相对引用

# 这里报错的原因是： y 这个包的父级包没有被找到   attempted relative import with no known parent package
因为你都没有将他加入路径，所以找不到这个父级包

但是 xx.py 为什么可以呢？ 因为他将整个文项目的父级包加入进来了，所以可以执行，找得到 x 这个包了
"""
# import sys,os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from ..y import yy  # 同一个项目下，的导入       >>>>>  注意同名变量的问题

# 为了隐藏我的模块名， 相对导入方式

from ..y.yy import *
# 不再需要模块名作为前缀了, 但是注意，名称冲突啦但是，我们这 有 __all__

# 如果使用  from ..y import * 同名变量age2 出问题了。
age = 111
age2=999   # 注意冲突的问题
def zf():
    for i in range(5):
        print(f'z{i}={i + 1}')

# print(yy.age)   # 这样不会产生冲突
# print(yy.main())

if __name__ == '__main__':
    zf()
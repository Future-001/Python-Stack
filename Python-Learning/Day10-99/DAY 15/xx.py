"""  z--->x
做几个测试吧，相互引用，主要是练习 __all__
练习相对引用
"""
import os
import sys

age = 111
age2=999   # 注意冲突的问题
def xf():
    for i in range(5):
        print(f'x{i}={i + 1}')

if __name__ == '__main__':
    xf()

print()
print('相对路径的调用')

sys.path.append(os.path.dirname(__file__))  # 加入项目的父路径就可以了

from x.z import zz
# print(zz.zf())
# print(zz.yy.main())   # 这样错是不是出现一个问题，没有隐藏 yy 这个模块名啊，那相对路径没有被隐藏呢

# 改进  看zz 模块

# 上面的代码变为了
print(zz.zf())
print(zz.age)

print(zz.main())
print(zz.age1)
print(zz.age)   # 命名冲突啦，这就是问题
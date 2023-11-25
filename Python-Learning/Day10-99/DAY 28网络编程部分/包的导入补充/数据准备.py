"""
-glance
    -api
    -cmd
    -db

导入一个包（文件夹）相当于执行了这个包下的 __init__ 文件
并不是香断关于把这个包下的所有文件都导入进来了

要想导入某个文件夹下的文件：
import 后面必须是一个明确的文件或者方法。后面不能带.
方式一： import
import glance.api.cmd.xxx as xxx
方式二： from   这种方法后面的 import 后面不能带.
·               from 后面 .的前面必须是一个包
from glance.api import xxx


进阶：
就是之前说过的 包的互相导入（多重导入）
        利用 sys.path 一定好好查看一下。
        绝对导入：
        相对导入：     . 表示当前文件所在的父目录   .. 表示上一父目录
                缺陷： 相对导入的文件 不能运行，会报错。
                解决方法：import json
                当需要写一个功能，且功能不需要直接运行，而是被别人导入后使用的，那么这种情况下你的独立功能形成文佳佳
                文件夹内所有的文件都需要使用相对导入。

                当自己开发一个项目，这个项目有一些文件是需要直接运行额，这种情况不适合用相对导入。

"""

import os
os.makedirs('glance/api')
os.makedirs('glance/cmd')
os.makedirs('glance/db')
l = []
l.append(open('glance/__init__.py','w'))
l.append(open('glance/api/__init__.py','w'))
l.append(open('glance/api/policy.py','w'))
l.append(open('glance/api/versions.py','w'))
l.append(open('glance/cmd/__init__.py','w'))
l.append(open('glance/cmd/manage.py','w'))
l.append(open('glance/db/models.py','w'))
map(lambda f:f.close() ,l)


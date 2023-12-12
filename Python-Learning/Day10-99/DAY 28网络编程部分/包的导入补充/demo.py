import sys
import glance  # 这样只是执行了这个包下面的 __init__ 文件，不是相当于导入了所有的文件。
# 导入某个包下的文件 方式一  import xx as xx
# 方式二  from xxx import xxx
from glance.api import policy

# print(sys.path)
# print(sys.modules)

print(glance)
policy.get()  # from policy.py

glance.gg()  # glance下面的 __init__ 方法。

from glance.api.versions import t
t()

import glance.cmd
# glance.cmd.man()  # 这样的就不行了，没有这个路径在里面 ，就得用绝对导入了。
#  就是在各自的 __init__ 里面还得导入一下例如 在cmd的 __init__ 中进行import  glance.cmd.manager

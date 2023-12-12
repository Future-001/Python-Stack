def gg():
    print("大壮很受伤 from glance/__init__py",  __name__)


# import api
# demo 模块有了这俩就执行不成功为什么呢？因为在外面用了绝对导入了。所以不成功
# import cmd

# from glance import api   # 这样就成了绝对导入，但是里面的policy还是调用不到，还是得在a'pi的__init__ 中绝对导入。挺麻烦
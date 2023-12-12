import glance
# 我从这里直接调用glance ,在glance中的 __init__ 中调用 import cmd, 这样直接会报错
# 为什么呢？
    # 因为：这样此时查看demo2的 sys.path 看到他没有glance的路径，执行了导入glance,
#   执行 其中的 __init__ 模块，你从里面去调用api 或者cmd，是调用不到的，因为没有哪个路径在其中。就是sys.path里面没有导入。
    # 如果一个一个的 append 路径，这也太麻烦了。
            # 比如说，你在glance的文件中将路径加入到sys.path中，但是，之后的文件中，你只是导入了 api cmd之中的 __init__ 方法，
            # 如果想要执行其他文件，你还得在对应的文件夹下的 __init__ 方法中，将文件夹的路径i加入进来。。。。这丫太麻烦了


"""
========================================= 昨日回顾 =========================================
软件开发规范： 主逻辑函数   公共组件   启动函数
各种文件：  start.py  src.py(主逻辑的)    access.log(日志)       common.py  公共组件的
可能这些函数很多，所以需要再次进行 文件夹的创立，创建 start   src   log   common 文件夹

一般是这样的：     bin（启动文件）     conf（配置文件  setting.py  静态的路径，数据库链家设置等，变量，启动之前能设置，之后不能改变，只能引用）
                 core(放主逻辑的 login register diary)  db(数据库 文本数据)    lib(公共组件  装饰器，日志函数)
                 log 日志记录
=========================================  今日大纲 =========================================

https://www.cnblogs.com/jin-xin/articles/10903733.html
"""
import os
# os.mkdir('cnblog')
# l1 = ['bin','conf','log','core','lib','db']
# for i in l1:
#     path = os.path.join('cnblog', i)
#     os.mkdir(path)




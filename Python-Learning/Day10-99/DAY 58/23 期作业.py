# 整理笔记
#
# 官网查看内置过滤器 https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#built-in-filter-reference
#
# 使用过滤器完成加、减、乘、除的操作
#
# 自定义一个过滤器：
#
# 给定一个网址的字符串和它的名字，页面显示a标签
#
# 使用
# {{ 'www.baidu.com'|show_a:'百度'  }}
#
# 页面结果
# 百度
# <a href="http://www.baidu.com">百度</a>   点击可跳转

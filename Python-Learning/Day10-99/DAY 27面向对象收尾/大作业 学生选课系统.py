# 利用规范化目录结构完成一个学生选课系统。
# **角色：**学生、管理员。
#
# 功能分析：
#
# 用户登录之后就可以直接判断用户身份，是学生还是管理员。
# 学生登录之后有以下几个功能：
# 查看所有课程。
# 选择课程。
# 查看所选课程。
# 退出程序。
# 管理员登录之后有以下几个功能：
# 创建课程(需要记录日志)。
# 创建学生账号(需要记录日志)。
# 查看所有课程。
# 查看所有学生。
# 查看所有学生的选课情况。
# 退出程序。
# 课程属性：课程名，价格，周期，老师。
#
# 学生属性：姓名，所选课程。
#
# 管理员属性：姓名。
#
# 流程图： https://www.processon.com/view/link/5d283960e4b0878e40af9dd8
#
# 参考模板：src主逻辑文件。
#
# class Student:
#     def __init__(self,name):
#         self.name = name
#         self.courses = []
#
#     def show_courses(self):
#         '''查看可选课程'''
#         pass
#
#     def select_course(self):
#         '''选择课程'''
#         pass
#
#     def show_selected_course(self):
#         '''查看所选课程'''
#         pass
#
#     def exit(self):
#         '''退出'''
#         pass
#
# class Manager:
#     def __init__(self,name):
#         self.name = name
#
#     def create_course(self):
#         '''创建课程'''
#         pass
#
#     def create_student(self):
#         '''创建学生'''
#         pass
#
#     def show_courses(self):
#         '''查看可选课程'''
#         pass
#
#     def show_students(self):
#         '''查看所有学生'''
#         pass
#
#     def show_students_courses(self):
#         '''查看所有学生选课情况'''
#         pass
#
#     def exit(self):
#         '''退出'''
#         pass
#
#
#
# class Course:
#     def __init__(self,name,price,period):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.teacher = None
#
# def login():
# 	pass
# def main():
#     '''程序入口'''
# 	pass
# main()

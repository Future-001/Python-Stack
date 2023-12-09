# 文件的函数部分的东西：
#  员工信息表
# select 查询这个文件
# select name,age where age>20
# select name,age,job where age>20
# select name,age,job where age<20
# select name,age,job where age=22
# select name,age,job where name='alex'
# select name,age,job where job='IT'
# select name,age,job where phone='133'
# select *
# 文件处理 + input


# 周末大礼包——员工信息表
# 文件存储格式如下：
# id，name，age，phone，job
# 1,Alex,22,13651054608,IT
# 2,Egon,23,13304320533,Tearcher
# 3,nezha,25,1333235322,IT
#
# 现在需要对这个员工信息文件进行增删改查。
# 基础必做：
# a.可以进行查询，支持三种语法：
# select 列名1，列名2，… where 列名条件
# 支持：大于小于等于，还要支持模糊查找。//正则
# 示例：
# select name, age where age>22
# select * where job=IT
# select * where phone like 133
#
# 进阶选做：
# b.可创建新员工记录，id要顺序增加c.可删除指定员工记录，直接输入员工id即可
# d.修改员工信息
# 语法：set 列名=“新的值” where 条件
# #先用where查找对应人的信息，再使用set来修改列名对应的值为“新的值”
#
# 注意：要想操作员工信息表，必须先登录，登陆认证需要用装饰器完成
# 其他需求尽量用函数实现

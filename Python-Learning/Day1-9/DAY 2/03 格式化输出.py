# 建立一个公共的个人模板

# msg='''------info  of Kevin---------
# Name: Kevin
# Age : 18
# Job : teacher
# sex : male
# '''
name=input('姓名:')
age=input('age: ')
job=input('job:')
sex=input('sex: ')

msg='''------info  of %s---------
Name: %s
Age : %s
Job : %s
sex : %s
-------------end-------------''' %(name,name,age,job,sex)#传入的数据，可以改
print(msg)

# 如果想要进行格式化输出% ,而不是将其认为是占位符，需要用%%，第二个%进行转义输出
msg='My name is %s,age is %d ,and I`aved learned 1.txt%%' %('kevin',18)
print(msg)
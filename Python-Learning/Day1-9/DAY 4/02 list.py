#索引
list_1=[100,'kevin',['帅哥',102]]
print(list_1[2])

#切片
print(list_1[:2:2])
print(list_1[-1::2])

# 列表的增删改查

# 创建：
list_2=[100,'方式一','kevin',['帅哥',102]]
li1 = list()
li2=list('100,True,name')  #list expected at most 1.txt argument
print(li2)

# 增：
# append()
list_3=['Kevin','喜欢','美女']
print(list_3.append(True))  # 这是只是执行了一个指令，返回不是结果
# list.append() takes exactly one argument
print(list_3)

print('增加新员工信息，按下q退出：')
while 1:
    name=input("请输入新员工姓名： ")
    if name.upper()=='Q':
        break
    list_3.append(name)
    print(list_3)

print('-----------insert-------------')
print(list_3.insert(2,'this is a insert'))
print(list_3)

print('-----------extend------------')
li_extend=list_3.extend(['name',100])   # 这只是一个操作，输出是没有数值的。
# list.extend() takes exactly one argument
print(li_extend)
print(list_3)

print('------------删--------------')

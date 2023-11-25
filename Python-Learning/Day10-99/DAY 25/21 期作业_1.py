# 请使用面向对象实现栈（后进先出）
class Stack:
    def __init__(self):
        self.l = [1,2,3]
    def put(self,data):
        self.l.append(data)
    def get(self):
        yield self.l.pop()
l1 = Stack()
l1.put(4)
print(list(l1.get()))
l1.put(5)
print(list(l1.get()))
# 请用面向对象实现队列（先进先出）
#  和队列类似，只是改为了 pop(0) 区别不大

# 如何实现一个可迭代对象？
#      iter

# 看代码写结果
class Foo(object):
    def __init__(self):
        self.name = '武沛齐'
        self.age = 100
obj = Foo()
# setattr(Foo, 'email', 'wupeiqi@xx.com')   # 只是增加了一个属性，email  同时赋值了。
# v1 = getattr(obj, 'email')
# v2 = getattr(Foo, 'email')

# print(v1, v2)

# 稍作修改看一看呢
setattr(obj, 'email', 'wupeiqi@xx.com')   # 只是增加了一个属性，email  同时赋值了。
print(getattr(obj, 'email'))
if hasattr(Foo,'email'):
    print(getattr(Foo,'email'))
else:print('该属性不存在')

# 请补充代码（提：循环的列表过程中如果删除列表元素，会影响后续的循环，推荐：可以尝试从后向前找）
li = ['李杰', '女神', '金鑫', '武沛齐']
name = input('请输入要删除的姓氏：')  # 如输入“李”，则删除所有姓李的人。
for i in li[::-1]:
    if name in i:
        li.remove(i)
print(li)


# # 请补充代码
# 有如下字典，请删除指定数据。
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
info = [User('武沛齐', 19), User('李杰', 73), User('景女神', 16)]
name = input('请输入要删除的用户姓名：')
# # 请补充代码将指定用户对象在info列表中删除。
for i in info[::-1]:
    print(i.name)
    if name==i.name:
        info.remove(i)
    else:print(i.__dict__)


# 补充代码实现：校园管理系统。
# # !/usr/bin/env python
# -*- coding:utf-8 -*-   # 为了在python2里面也能正常运行
 # 其实还有一些问题，比如说重名了，什么的，就有点问题
class User(object):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    def __str__(self):  # 这就是私有变量
        return self.name

class School(object):
    """学校"""
    def __init__(self):
        # 员工字典，格式为：{"销售部": [用户对象,用户对象,] }
        self.user_dict = {}
    def invite(self, department, user_object):
        """
        招聘，到用户信息之后，将用户按照指定结构添加到 user_dict结构中。
        :param department: 部门名称，字符串类型。
        :param user_object: 用户对象，包含用户信息。
        :return:
        """
        if department not in self.user_dict:   # 别忘记get也可以实现类似的功能
            self.user_dict[department]=[]
        self.user_dict[department].append(user_object)
        return True
    def dimission(self, username, department=None):
        """
        离职，讲用户在员工字典中移除。
        :param username: 员工姓名
        :param department: 部门名称，如果未指定部门名称，则遍历找到所有员工信息，并将在员工字典中移除。
        :return:
        """
        if department != None:
            for i in self.user_dict:
                if i == department:
                   for usr in self.user_dict[i]:
                       if username == usr.name:
                           self.user_dict[i].remove(usr)
                           return True
        elif department == None:
            for _,usr_information in self.user_dict.items():
                for i in usr_information:
                    if username == i.name:
                        usr_information.remove(i)
                        break
            return True
    def run(self):
        """
        主程序
        :return:  利用return 实现是否成功入职或者离职
        """
        while True:
            for i,j in self.user_dict.items():
                for k in j:
                    print(i,k.__dict__)
            opt = ['招聘入职', '离职']
            for index, i in enumerate(opt, 1):
                print(index, i)
            choice = input('请输入你想进行的操作(Q退出)：')
            if choice == '1':
                username = input('请输入用户名：').strip()
                pwd = input('请输入密码：').strip()
                email = input('请输入邮箱：').strip()
                department = input('请输入所在部门：').strip()
                ret = self.invite(department,User(username,pwd,email))
                if ret :print('录入成功！')
                else:print('录入失败。')
            elif choice == '2':
                username = input('请输入用户名: ').strip()
                department = input('请输入所在部门：').strip()
                ret = self.dimission(username,department if bool(department) else None)
                if ret:print('员工信息删除成功 ')
                else:print('删除失败，请重试 ')
            elif choice.upper() == 'Q':
                break
            else:
                print('输入错误，请重新输入。')


if __name__ == '__main__':
    obj = School()
    obj.run()



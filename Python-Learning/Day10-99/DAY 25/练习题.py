"""
队列
栈
自定义pickle，利用pickle模块完成简化的dump 和load
pickle dump:  打开文件，dump进文件
pickle load:  打开文件。读取数据
对象=Mypicke('文件路径')
对象.load(0  拿到这个文件里面的所有的对象
"""
"""class Queue:
    l = [] #  这样写不行，因为这个静态变量是共享的。
    def __init__(self):
        self.list=[]
    def put(self,item):
        self.list.extend(item)
    def get(self):
        return self.list.pop(0)  # 这样效率最高
    def gets(self):
        print(iter(self.list).__next__())
a=Queue()
a.put('sb')
print(a.get())
a.gets()

# 假设你希望一个类之间的某个属性是各自的属性。不是共同的属性
# 那么我们需要将变量存储在对象的命名空间中，不能建立静态变量，
# 静态变量是所有的对象共享一个变量

class Stack:
    def __init__(self):
        self.list=[]
    def put(self,item):
        self.list.extend(item)
        print(self.list)
    def get(self):
        return self.list.pop()  # 这样效率最高
a=Stack()
a.put('you-art-sb--hh')
print(a.get())"""

# 代码的简化
class Data_Structure:
    def __init__(self):
        self.list=[]
    def put(self,item):
        self.list.extend(item)
    def get(self):
        return self.list.pop(0) if self.index==0 else self.list.pop()
class Queue(Data_Structure):
    def __init__(self):
        self.index=0
        Data_Structure.__init__(self)
a=Queue()
a.put('sb')
print(a.get())
class Stack(Data_Structure):
    def __init__(self):
        self.index=1
        Data_Structure.__init__(self)
a=Stack()
a.put('you-art-sb--hh')
print(a.get())

import pickle
class Mypickle:
    def __init__(self,path):
        self.file=path
    def dump(self,obj):
        with open(self.file,'ab') as f:
            pickle.dump(obj,f)
    def load(self):
       with open(self.file,'rb') as f:
           while True:
               try:
                   yield pickle.load(f)
               except  EOFError:
                   break


f1=Mypickle("D:\Code Files\Python\Python-Learning\Class-code\DAY 25\作业\Mypickle")
f1.dump('黑夜里咯，你看看')
for i in f1.load():
    print(i)
f1.dump('好好学习，天天向上')
f1.load()

# 仿照上面的东西，写一个  json
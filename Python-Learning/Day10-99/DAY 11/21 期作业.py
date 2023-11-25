# 列举
# str、list、dict、set
# 中的常用方法（每种至少5个），并标注是否有返回值。
#  str :  strip split  join count index find  startswith endswith  replace center
#   list : append  insert  update extend     remove pop  del clear
#   dict  :  setdefault   update  pop del clear get
#   set :   合并重复元素    intersection  union  & |  - difference


# 看代码分析结果

def func(arg):
    return arg.replace('苍老师', '***')

def run():
    msg = "Alex的女朋友苍老师和大家都是好朋友"
    result = func(msg)
    print(result)            # "Alex的女朋友***和大家都是好朋友"

run()

# 看代码分析结果

def func(arg):
    return arg.replace('苍老师', '***')

def run():
    msg = "Alex的女朋友苍老师和大家都是好朋友"
    result = func(msg)
    print(result)

data = run()       # 返回值是空的，因为没有给他传递
print(data)  # NONE

# 看代码分析结果
print()
DATA_LIST = []
def func(arg):
    return DATA_LIST.insert(0, arg)

data = func('绕不死你')      # 搓了搓啦，没有返回值的啊，，，，，，，DATA = DATA_LIST    ['绕不死我']
print(data)             #  错误了，因为他是没有饭hi之的啊，，，，，所以不就是空了吗。。。。。
print(DATA_LIST)    # 错误答案： 还是空的，因为局部变量无法改变全局变量的数值
# 实际上，被修改了。。。。。

# 看代码分析结果
print()
def func():
    print('你好呀')
    return '好你妹呀'

func_list = [func, func, func]

for item in func_list:
    val = item()    # 打印了 你好呀       # 别忘记传递的是地址就行了。。。。
    print(val)      # 输出了好你妹啊


# 看代码分析结果
print()
def func():
    print('你好呀')
    return '好你妹呀'

func_list = [func, func, func]

for i in range(len(func_list)):
    val = func_list[i]()
    print(val)


# 看代码写结果
print()
tips = "啦啦啦啦"
def func():
    print(tips)
    return '好你妹呀'

func_list = [func, func, func]

tips = '你好不好'        # 一定要记住，存储的是地址。。。。

for i in range(len(func_list)):
    val = func_list[i]()
    print(val)
# 又错了,就近原则呢。。。。。 先打印了 啦啦啦，然后打印了 好你妹啊
# 先打印了 你好不好。，然后打印了 好你妹啊


# 看代码写结果
# print()
# def func():
#     return '烧饼'
# def bar():
#     return '豆饼'
# def base(a1, a2):
#     return a1() + a2()
#
# result = base(func, bar)
# print(result)

# 看代码写结果
print()
def func():
    return '烧饼'
def bar():
    return '豆饼'
def base(a1, a2):
    return a1 + a2
result = base(func(), bar())
print(result)

# 看代码写结果
print()
v1 = lambda: 100
print(v1())   #  100

v2 = lambda vals: max(vals) + min(vals)
print(v2([11, 22, 33, 44, 55]))  # 66

v3 = lambda vals: '大' if max(vals) > 5 else '小'
print(v3([1, 2, 3, 4]))         # 输出的是 小


# 看代码写结果
print()
def func():
    num = 10
    v4 = [lambda: num + 10, lambda: num + 100, lambda: num + 100, ]
    for item in v4:
        print(item())

func()   # 输出了 20 110 110

# 看代码写结果
print()
for item in range(10):
    print(item)

print(item)  # 输出最后的一个 item

# 看代码写结果
print()
def func():
    for item in range(10):
        pass
    print(item)

func()        # 只输出一个 9

# 看代码写结果
print()
item = '老男孩'
def func():
    item = 'alex'

    def inner():
        print(item)

    for item in range(10):
        pass
    inner()
func()  # 输出 9

# 看代码写结果【新浪微博面试题】
print()
def func():
    for num in range(10):
        pass
    #  相当于 num =9
    v4 = [lambda: num + 10, lambda: num + 100, lambda: num + 100, ]
    result1 = v4[1]()
    result2 = v4[2]()
    print(result1, result2)

func()  # 109 109



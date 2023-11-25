
import os
def func1(path):
    dir_list = os.listdir(path)
    for i in dir_list:
        abs_path =os.path.join(path,i)
        if os.path.isfile(abs_path):
            print(abs_path)
        elif os.path.isdir(abs_path):
            func1(abs_path)

func1("D:\Code Files\Python\Python-Learning\Class-code\DAY 21")


# 计算文件的大小
def file_size(path):
    size = 0
    dir_list = os.listdir(path)
    for i in dir_list:
        abs_path = os.path.join(path, i)
        if os.path.isfile(abs_path):
            size+=os.path.getsize(abs_path)
        elif os.path.isdir(abs_path):
            ret = file_size(abs_path)
            size+=ret
    return size     # 通过调试，好像理解了是为什么
# 简单来说，遇到文件夹，那么文件夹里面执行 for 之后，返回了一个size, 是通过遍历执行文件夹里面的的文件后，得出了ret ,但是原来的循环里面还有
#  size ,他不为0

print(file_size("D:\Code Files\Python\Python-Learning\Class-code\DAY 21"))


# 求斐波那契数列的一些方法：
# 不用递归也可以做
def fb_shul(n):
    a, b = 1, 1
    while n>2:
        a,b=b,a+b
        n-=1
        if n==1 or n==2: return b
    return b
print(fb_shul(10))  # 1 1 2 3 5 8 13 21 34 55 89

# 方法二，但是我只递归一次
def fb_digui(n,a=1,b=1):
    if n>2:return fb_digui(n-1,b,a+b)
    else:return b

print('::::::::::::')
print('递归的结果： ', fb_digui(10))

# 生成器的方法：
def gen_fb(n):
    a,b=1,1
    if n==1 or n==2:yield b
    else:
        yield from(1,1)
        while n>2:
            a,b=b,a+b
            n-=1
            yield b
print(list(gen_fb(10)))


# 多级菜单的一个题目了
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
# def menu_index(menu):
#     flag=True
#     while flag:
#         for i in menu:
#             print(i)
#         key = input('请输入: ')
#         if menu.get(key):
#             dic= menu.get(key)
#             flag=menu_index(dic)
#             if not flag:
#                 flag=True
#         elif key.upper()=='B':return False
#         elif key.upper()=='Q':break
# menu_index(menu)


def menu_index2(menu):
    flag=True
    while flag:
        for i in menu:
            print(i)
        key = input('请输入: ')
        if menu.get(key):
            dic= menu.get(key)
            flag=menu_index2(dic)
            if not flag:return
        elif key.upper()=='B':return True
        elif key.upper()=='Q':return False
menu_index2(menu)
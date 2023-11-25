# 昨日回顾
dic={'a':1}
print(dic.setdefault('b'))     # 不会报错，返回的是None

dic = {"alex":56,"wusir":34,"太白":55,"宝元":{"a":1,"b":2}}
for em in dic:  # for字典 获取的键    em = "宝元"  a = 1.txt
    print("abc")
print(em)  #  "宝元"

# 让用户输入任意字符串，然后判断此字符串是否包含指定的敏感字符。

char_list = ['利奇航', '堂有光', '炸展会']
content = input('请输入内容：')  # 我叫利奇航  / 我是堂有光  / 我要炸展会

success = True

for v in char_list:
    if v in content:
        success = False
        break

if success:
    print(content)
else:
    print('包含铭感字符')

# 示例：
# 1.txt. 昨天课上最后一题
# 2. 判断 ‘v2’ 是否在字典的value中 v = {'k1':'v1','k2':'v2','k3':'v3'} 【循环判断】
# 3. 敏感字

print('========================= 集合 ============================')
print('无序，无重复')
print()

print('================定义方式==================')
print('=======方式一========')
s=set([1,2,'kevin','Mette'])
print(s,type(s))
print()

print('=========方式二-======')
s=set()
print(s,type(s))

# s={'name','lipy','do',1.txt,2,[2,6,7]}          元组是可哈希（不可变的），所以不能在其中加入可变的数据类型。
s={'name','lipy','do',1,2}
print(s,type(s))

"""
None
int
    v1 = 123
    v1 = int() --> 0
bool
    v2 = True/False
    v2 = bool() -> False
str
    v3 = ""
    v3 = str()
list
    v4 = []
    v4 = list()
tuple
    v5 = ()
    v5 = tuple()
dict
    v6 = {}
    v6 = dict()
set
    v7 = set()
"""

"""
================================ 集合的独有功能===================================================
add 增加元素，集合里面的元素是不可变的，集合是可变的。
update  其实字典里也有，迭代着增加。"""


print('=====================增=========================')
print('=======方式一==========')
s=set(['name','kevin',1,23,4,77,8,3])
print(s)
s.add('time')
print(s)

print('========方式二   可以看到无序性和不可重复性。==========')
s.update([4,2,77,9,5])
print(s)
print()

print('=====================删=========================')
print('=======方式一  .discard(element) ==========')
print(s.discard('t'))   #  删除集合中的 一个 元素，若不存在，不报错。

print('=======方式二  .remove(element) ==========')
s.remove('time')
print(s)

print('=======方式三 .pop()  随机删除==========')
print(s)
print(s.pop())
print()

print('=====================改和查，只能通过先删后加方式实现 =========================')
print()

print('=====================交集 并集 差集等=========================')
s=set(['name','大白','谁不爱呢'])
s1={'谁不爱呢','大白',1,2,3,4,'宏宝莱'}

print('=======交集  &  .intersection(s1)==========')
print(s & s1)
print(s.intersection(s1))

print('=======交集  |  .union(s1) ==========')
print(s | s1)
print(s.union(s1))

print('=======差集 -  .difference(s1)==========')
print(s-s1)
print(s.difference(s1))

print('=======反交集  .symmetric_difference()==========')
print(s.symmetric_difference(s1))

print('=======子集 < issubset() 和 超集 > .insuperset() ==========')
print(s<s1)
print(s.issubset(s1))

print(s>s1)
print(s.issuperset(s1))


'================================ 集合的独有功能   # len , for  无索引切片==================================================='

'================================ 嵌套问题 ==================================================='
# 1.txt. 列表/字典/集合 -> 不能放在集合中+不能作为字典的key（unhashable）   集合中的元素以及字典的Key都是可哈希的
# info = {1.txt, 2, 3, 4, True, "国风", None, (1.txt, 2, 3)}
# print(info)
# 2. hash -> 哈希是怎么回事？
# 因为在内部会将值进行哈希算法并得到一个数值（对应内存地址），以后用于快速查找。

# 3. 特殊情况
# info = {0, 2, 3, 4, False, "国风", None, (1.txt, 2, 3)}
# print(info)

# info = {
#     1.txt:'alex',
#     True:'oldboy'
# }
# print(info)

print("""===============================       is id ==      ==================================          """)
print(s is s1)
print(id(s),id(s1))
print(s==s1)

print('================== 代码块。内存的缓存机制 ======================')

print('================== 深浅copy    .copy()     copy.deepcopy()  ======================')







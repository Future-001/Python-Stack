# 看代码分析结果
func_list = []
for i in range(10):
    func_list.append(lambda :i)    # func_list = [0,1.txt,2,,,,9]
v1 = func_list[0]()
v2 = func_list[5]()
print(v1,v2)
# 输出的是 我还真的不理解...这里为什么是这个呢?不是很理解,一句话函数, 这里加入列表的元素是一个函数名
# 那么,我执行  懂了,我们这里列表添加的元素是 (lambda :i)的这一个地址,

print()
# 看代码分析结果【面试题】
def func(num):
    def inner():
        print(num)   # 闭包
    return inner

result = []
for i in range(10):
    f = func(i)
    result.append(f)         # 降低至加入了列表,但是,但是,但是,由于闭包,自由便来给你不会消失,那么,会导致,后面 Num
# 后面 Num的数值被修改了,
print(i)  # 9
print(result)  # 全是地址,而且不同呢
v1 = result[0]()     # 为什么是 0 ,因为 每次执行,都对每个 f 创建了一个不同的 Num,
# 由于 num不能被外部修改,那么,相当于创建了 9 个 num 而且互不影响
v2 = result[9]()
print(v1,v2)     # 输出了  NONE NONE 函数已经被执行完了...没有返回值了


# 求结果(面试题)
print()
v = [lambda :x for x in range(10)]
print(v)
print()
print(v[0])
print(v[0]())
print(v[9]())
print('错误看法: 输出是: v 是一个列表,里面元素是地址,并没有被执行,v[0] 是一个地址,最后的输出是: 一个嵌套的列表? 里面是 0 --9')
print(len(v))


# 实际的输出结果是: v是一个列表,但是列表中有很多地址,因为这个列表没有被执行,所以给,他会存储10个lambda的地址
#  对其中的元素取值,就是取第一个的一个地址,然后执行完成这个函数之后,x 变成了 9 ,最终返回输出的就是 9

print()
v = (lambda :x for x in range(10))   # 生成器表达式
print(v)    # v里面一定要记住，他是十个地址，但是这个地址 还没有被执行， 一旦执行后，里面输出的都是 9
# print(v[0])      为什么这两行错了呢？因为这是一个生成器。生成器可以对他进行取值，但是，没有这种形式，只有 next 或者 list for
# print(v[0]())
print(next(v))
print(next(v)())
# 为什么会做错了呢？因为什么？   这里对于生成器的认识还是不够，以为他是 和列表一样的
print('这就是生成器的妙用了吗？ 对比一下上一个错题')
while 1:
    try:
        print(next(v)())
    except StopIteration:
        break


print(f'\n注意区分一下 这')
def num():
	return [lambda x:i*x for i in range(4)]  # 列表推导式，里面存储了 四个地址。一旦执行，输出的i 都是 4 ，最后的都是4
print([m(2)for m in num()])   # 输出的是 ：这里输出的是 一个列表  [6,6,6,6]
# 返回的是一个列表啊， 注意了，和刚才那个题的区别，可以去看看 错题里面的东西


print()
# 有一个数组[34,1.txt,2,5,6,6,5,4,3,3]请写一个函数，找出该数组中没有重复的数的总和（上面数据的没有重复的总和为1+2=3)(面试题)
# 突然想到一个简化部分重复数字的方法：   set 但是还会保留部分元素啊
# gpt 提供的一个思路可以，记录下每个数字的出现次数，然后去计算，最终用列表得出一个数值

l1 = [34,1,2,5,6,6,5,4,3,3]
dic = {}
for j in l1:
    for k in str(j):
        if int(k) in dic:
            dic[int(k)]+=1
        else:
            dic[int(k)]=1
print(dic)
l2 =[]
for i,j in dic.items():
    if i in l1 and j==1:  # 两个条件，这样能避免 74 这种情况， 7 次数为1 ，但是不在列表里面
        l2.append(i)
print(sum(l2))


print()
# 上面的已经可以了，但是如果我增加了难度呢？
l1 = [87,99,34,1,2,5,6,6,5,4,3,3,55]
dic = {}
for j in l1:
    for k in str(j):
        if int(k) in dic:
            dic[int(k)]+=1
        else:
            dic[int(k)]=1
print(dic)
l2 =[]
for k in l1:
    if len(str(k))==1:
        if dic[k]==1:
            l2.append(k)
    else:
        status = True
        for t in str(k):
            if dic[int(t)]==1:
                pass
            else:
                if len(str(k))==dic[int(t)]:
                    break
                else:
                    status=False

        if status==True:
            l2.append(k)
print(l2)




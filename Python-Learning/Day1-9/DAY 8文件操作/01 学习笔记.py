""""
=====================================昨日回顾========================================
数据类型的补充：
        str:
        tuple:
            逗号的问题
            count,index
        list:
            sort   reverse   相加  与数字相乘
            循环列表的问题，删除元素的方法。
        dic:
            update 更新，增加值，修改值，创建字典，将一个字典的所有键值对覆盖添加到另一个字典
            dict.fromkeys(iterable,value)        # 面试经常考
            循环字典，删除元素的问题。

数据类型的转换问题：        0 {} [] set() none
编码的进阶：
        ASCII gbk unicode uft-8 big5.......二进制与文字的对应关系。   最核心的 Unicode
                                        与所有的编码方式都有一个对应关系。
        所有的编码方式（除去Unicode）不能互相识别。
        在内存中，所有的数据都是Unicode编码的（int bool str list dict tuple set)，除去 bytes 型。
                   但是 bytes  只能和  str 进行转换。。。。。。，
                   别的Unicode的数据类型必须要先转换成str 才能转化为bytes类型。

            str:  文字文本     bytes:  字节文本

=====================================今日大纲========================================

文件操作初识：
        1.  护士空姐少妇的联系方式.txt
        利用 python 代码写一个很 low 的软件取操作一个文件。
            文件路径： path
            打开方式：mode :   读，写，追加，读写，写读......
            编码方式：encoding   utf-8 , gbk, gb2312
        f1 = open(path,encoding='utf-8',mode='r)     #  encoding这里表示文件打开的编码方式
                                                        一定要与原来文件中内容的 编码方式一致。
        f1.read()    f1.close()

        open 内置函数，open底层调用的是操作系统的接口，
        f1 变量，f1,fh,file_handler,f_h  文件句柄  对文件进行的任何操作都得通过文件句柄
        encoding : 可以不写，默认的编码本： 操作系统的默认编码。
                                    encoding 的对用编码方式要与需要打开文件中内容的编码方式一致才能打开。
                windows: gbk
                linux: utf-8
                mac: utf-8
        f1.close()  关闭文件句柄

    打开文件错误的常见几种方式： ‘D:\Code’  ‘D:\\Code’ 再加上一个 \
                            因为原来的字符可能被识别为转义字符去了，所以再加上一个 \解决
                            r'D:\Code'   在路径前加上r 表示这是一个文件路径

    文件句柄三部曲：
        打开文件句柄，
        对文件句柄进行操作
        关闭文件句柄

常见的文件操作：
        读：
            r,rb(以bytes形式读出来),r+(读写）, r+b...
            .read(element)  默认全读
            .readline()   可以每次读取一行
            .readlines()    一次读取很多行，返回一个列表，每个元素后面都有一个换行符
            for  遍历其中的每一行元素
                    #  有了 readlines()为什么还需要 for 呢？
                                因为文件句柄相当于一个迭代器，当读取到这一行后，这一行就消失，
                    #  去下一行 进行读取，不占用内存    不然当数据过大时，用 列表就读取不出来。占用了很大的内存。

            rb: 操作的是非文本类型的文件，例如图篇等等
                注意，这样不需要 encoding 默认就用rb打开了

            r+ (读并追加）就是在读的基础上加上一个功能，但是不能创建一个新文件
                光标。输入的位置。。。。
                一定要先读再追加。错误示例如下：
                        # print('===============r+ (读并追加）先写再读结果呢？===================')
                        # f = open ( '我好喜欢',encoding='utf-=8',mode='r+')
                        # f.write('\n你喜欢吗')              # 为什么用换行符，光标输入。
                        # content = f.read()
                        # # 会将光标从第一个开始输入，覆盖原来的结果，出现问题了。同时还有一个问题
                        # #  而且，对于原来的字符，例如说英文字符 一个一个字节，但是中文一个三个字节，那字节就对不上了，替换不了，报错了
                        # print(content)
                        # f.close()

        写：
            w,wb,w+,w+b......
            .wirte()
              # 没有文件，创建文件。 # 如果文件存在，先清空后写入
              针对文件的清空，只有关闭了文件句柄再重新打开写入才会清空，如果句柄未关闭，可以继续写入。
              # 本来在文件中进行编码，是以字符串方式 Unicode，存储时利用bytes类型，涉
                            及到一次编码的转换问题，但是open 这个函数已经帮你弄好了

            wb: 对非文本类文件进行操作，不需要encoding
                例如以 bytes类型读出来，然后将其写入另一个文件，就实现了文件的复制与粘贴

        追加：
            a,ab,a+,a+b...........
            .write()   没有文件，创建文件，文件存在，追加内容



                        r+
                        读：默认从0的光标开始读，也可以通过 seek 调整光标的为位置。
                        写：从光标所在的位置开始写，也可以通过 seek 调整光标的位置。
                        w+
                        读：默认光标永远在写入的最后或0，也可以通过 seek 调整光标的位置。
                        写：先清空。
                        a+
                        读：默认光标在最后，也可以通过 seek 调整光标的位置。然后再去读取。
                        写：永远写到最后。



        其他模式：
                总结： 三个大方向
                读： r rb r+ r+b
                写： w wb w+ w+b
                追加： a,ab,a+,a+b
                相应的功能： 对文件句柄的操作 ：  .read()  .readline()  .readlines()  for  .write()
                其他：    .tell()  读之前一次，读之后一次，光标的位置变化。字节为单位 不用mode
                        .seek(where)  调整光标的位置，默认是0 字节单位。       不用mode
                        .flush()   强制刷新   可能某些内容没写进去，所以直接强制他保存。    不用mode

        打开文件的另一种方式；
                with open(path,enconding= ) as 文件句柄：

                不用手动关闭文件句柄，一段时间后关闭。
                一个with 可以操作多个文件句柄。

        文件的改的操作：
                将文件中含有某个元素全部替换为 x
                现存世界商各种对文件改的操作的五部曲：
                    以读的模式打开原文件
                    以写的方式创建一个新文件
                    将原文件的内容读出来修改成新内容（读出来的都是字符串啊，对字符串进行改操作。easy），写入新文件
                    将原文件删除
                    将新文件重命名成原文件
                import os
                os.remove()   os.rename
                用read读有一点low，因为read只能读写一部分内容。。。。。建议用for

"""
f1=open('D:\Code Files\Python\Python-Learning\Class-code\DAY 8\空姐少妇联系方式.txt',encoding='utf-8',mode='r')
content=f1.read()
print(content)
f1.close()

print()
print('============================  .read(element)  默认读，里面又字符就是读多少个字符=======================')
f_h=open('你最喜欢的',encoding='utf-8')   # mode 默认只读
content=f_h.read()
print(content,type(content))
f_h.close()

print('默认全读，里面加入参数就是按照字符读取，')
file=open('你最喜欢的 ',encoding='utf-8')      #  'gbk' codec can't decode byte
content=file.read(14)
print(content,type(content))
file.close()

print()
f=open('你最喜欢的',encoding='utf-8')
print('====================按照行读 .readline()   会多一行，以为会默认带一个换行符。===================')
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

print()
print('================按照行读 .readlines() 返回一个列表，列表中的每个元素是源文件的每一行====================')
f=open('你最喜欢的',encoding='utf-8')
l1 = f.readlines()
print(l1,type(l1))
f.close()

print()
print('===============for 循环读取  类似于上面对列表进行一个循环读取 f.readlines() ===================')
f = open('空姐少妇联系方式.txt ',encoding='utf-8')
for line in f:
    print(line)

#  为什么还需要 for 呢？  因为文件句柄相当于一个迭代器，当读取到这一行后，这一行就消失，去下一行 进行读取，不占用内存
# 不然当数据过大时，用 列表就读取不出来。占用了很大的内存。
# for i in f.readlines():
#     print(i)
f.close()

print()
print('===============rb 打开非文本类文件，例如图片等 不需要encoding ===================')
f = open('lena.jpg ',mode= 'rb')
content = f.read()
print(type(content))   # bytes  类型，太长了，不看了
f.close()

print()
print('===============文件的写，没有改文件名，默认增加在该目录下===================')
f = open('我好喜欢',encoding='utf-8',mode='w')   # 没有文件，创建文件。 # 如果文件存在，先清空后写入
# 本来在文件中进行编码，是以字符串方式Unicode，存储时利用bytes类型，涉及到一次编码的转换问题，但是open 这个函数已经帮你弄好了
f.write('随便写一点东西')
f.close()

# 首先，以 byte类型读出来，然后将其写入另一个文件，就实现了文件的复制与粘贴
print()
print('===============wb 主要操作非文本类的文件。例如图片？===================')
f = open('lena.jpg ',mode= 'rb')
content =f.read()
f.close()
f =open('美女.jpg',mode='wb')
f.write(content)
f.close()

print()
print('===============文件的追加===================')
f = open('追加',encoding='utf-8',mode='a')
f.write('大壮你是谁')
f.close()

print()
print('===============r+ (读并追加）就是在读的基础上加上一个功能，但是不能创建一个新文件，只能先读然后在追加===================')
f = open ( '我好喜欢',encoding='utf-=8',mode='r+')
content = f.read()
print(content)
f.write('\n你喜欢吗')              # 为什么用换行符，光标输入。
content = f.read()
# print(content)    这是读取不出来的。
f.close()

# print()
# print('===============r+ (读并追加）先写再读结果呢？===================')
# f = open ( '我好喜欢',encoding='utf-=8',mode='r+')
# f.write('\n你喜欢吗')              # 为什么用换行符，光标输入。
# content = f.read()
# # 会将光标从第一个开始输入，覆盖原来的结果，出现问题了。同时还有一个问题
# #  而且，对于原来的字符，例如说英文字符 一个一个字节，但是中文一个三个字节，那字节就对不上了，替换不了，报错了
# print(content)
# f.close()
print()
print('===============文件操作的其他功能===================')
print('========= .tell()  读之前一次，读之后一次，光标的位置变化。字节为单位===========')
f = open('你最喜欢的',encoding='utf-8')
print(f.tell())
content = f.read()
print(f.tell())
print(content)
f.close()

print()
print('========= .seek(where)  修改光标的位置。字节为单位===========')
f = open('空姐少妇联系方式.txt ',encoding='utf-8')
f.seek(15)
content = f.read()
f.flush()
print(content)
f.close()

print()
print('========= 打开文件的另一种方法 ===========')
with open('美女.jpg ',mode='rb') as f,\
    open('空姐.jpg ',mode='ab') as f2:
    content =f.read()
    f2.write(content)
    f2.flush()
print('优点是可以自动关闭文件，打开多个文件。缺点待续')


print('=============================文件改的操作============================')
"""    文件的改的操作：
                将文件中含有某个元素全部替换为 x
        现存世界商各种对文件改的操作的五部曲：
            以读的模式打开原文件
            以写的方式创建一个新文件
            将原文件的内容读出来修改成新内容，写入新文件         # 读出来的结果是字符串
            将原文件删除
            将新文件重命名成原文件"""
import os
with open('文件改的操作',encoding='utf-8',mode='w') as f1:
    content='alex太牛逼了 \n 我最喜欢的就是alex\n李白就是alex\n'
    f1.write(content)
    f1.flush()

with open('文件改的操作',encoding='utf-8',mode='r') as f1,\
    open('文件改(结果)',encoding='utf-8',mode='w') as f2:
    content = f1.read()
    f2.write(content.replace('alex','kevin'))
    f2.flush()
os.remove('文件改的操作')
os.rename('文件改(结果)','文件改的操作')


with open('文件改的操作',encoding='utf-8',mode='r') as f1,\
    open('文件改(结果)',encoding='utf-8',mode='w') as f2:
    for line in f1:
        new_line=line.replace('kevin','asb')
        f2.write(new_line)
# 一个疑问，文件的写每次都清空内容再写入，但是为什么这里没有呢，那是因为写入一次之后，文件句柄没有关闭，
    f2.flush()
os.remove('文件改的操作')
os.rename('文件改(结果)','文件改的操作')



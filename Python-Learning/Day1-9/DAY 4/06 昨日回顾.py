# #昨日回顾，自己去看看吧
# 1.txt.整型 整数 int
# 用于 计算和比较的
# 位制转换 2 ** 0 ~ 2 ** 7 == 2 ** 8 -1.txt
# 整除2 取余 余数 从下往上算 就是2进制的位数
#
# 2.布尔值 bool
# 用于 判断 转换
# 数字: 0 就是 False 非 0 就是 True ****
# 字符串: "" 空字符串就是 False 非空的字符串就是True ****

# 布尔值 True 数字 字符串
# 1.txt "True" print() 自动帮助咱们做了一些它认为比较友好的操作 repr 查看原生数据
# False 0 "False"
#
# 字符串:
# 索引 -- 准确定位 从左向右 0,1.txt,2,3 从右向左 -3,-2,-1.txt 变量名[索引值]
#
# 切片 -- 顾头不顾尾 变量名[起始位置:终止位置] 变量名[:终止位置] 默认为0 变量名[:] 从头到尾所有都获取
#
# 步长 -- 决定方向 默认是1 从左向右 ; 决定一次走几步
#
# 字符串方法 --- 字符串的类型.调用 才叫做字符串的方法
#
# 全部大写 upper
#
# 全部小写 lower 应用场景 验证码
#
# 以什么开头 startswith("a"，start,end) # 向计算机询问这个字符串是否是a开头
#
# 以什么结尾 endswith("x") # 向计算机询问这个字符串是否是x结尾
#
# 计数 count("a") # 向计算机询问这个a字符串出现了多少次
#
# 去掉头尾两边的空格和换行符 strip() 自己指定取出的内容
#
# 分割 split() 默认是以空格来分割,自己指定分割的元素(内容)
#
# 替换 replace() #两个参数 第一个旧的值(想要被替换的内容) 第二参数是新的(准备要去替换的内容,1.txt) # 指定替换的次数
#
# 格式化 format() :
#
# name = "{},{},{}"
# 顺序填充 format('a',"b",''c")
# name = "{0},{2},{1.txt}"
# 索引填充 format('a',"b",''c")
# name = "{a},{d},{f}"
# 关键字填充 format(f = 'a',d = "b",a = ''c")
# is 系列:
#
# isdecimal() 判断十进制 返回的是布尔值
# isalnum() 判断字母,中文,数字
# isalpha() 判断字母,中文
# for 循环
#
# s = "alex"
# for i in s:
# for 关键字
# i 是变量名 (可以人为修改名字)
# in 关键字
# s 可迭代对象 (int,bool不能进行迭代)
# for循环执行完后,在打印i这个变量的时候 值是???? 可迭代对象中最后一个元素
# 占位:
# pass 我占了 我不干事 过
# ...
# range() 范围
#
# python3中打印 range() 就是它本身
#
# python2中是列表
#
# range() 起始位置,终止位置,步长 --- 顾头不顾尾
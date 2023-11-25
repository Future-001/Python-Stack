#运算符
# not>and>or 从左到右

# and 的运用规则
# 如果：  第一个为真，则输出为第二个，
# 第一个为假，直接输出假   第一个为0，输出直接是0

# print(x or y)   x真（非零），则输出x,否则输出y
print(1 or 0)
print(0 or 1)

# int ---->  bool
i=16
print(bool(i))
i=-1
print(bool(i),type(i))
# bool ----->  int
print(int(True),int(False))

# int---->str   数字转为字符串无要求
age=189
print(str(age))
# str---->int
# name='kevin'     只能将纯数字字符串转化为整型数据。
name='0092'
print(int(name))

# 运算符
print((-1)**3)
# not>and>or
print(2>1 and 3<4 or 4>5 )
# and 的输出规则， 前后都是非零数字，输出后一个，如果有比较，前面为真，输出后面的结果，数字或者True False
# 前面或者后面含0(无比较），输出0
# 前面为假，直接 false
print ( 0 and 4>5)
print ( 4>5 and 0)
print (4 and 3)
print(3 and 0)
print(4 and 0>1)
print(2>1 and 4<3)
print(3>1 and 4<5)
print(2>1 and 3<4 or 4>5 )
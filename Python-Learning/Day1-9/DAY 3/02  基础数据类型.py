#  int 类型的数据
# 加减乘除,进制转换
i=10
# 有效的二进制长度   i.bit_length()
print(i.bit_length())

# print('name'.bit_length())
# 'str' object has no attribute 'bit_length'

# 2. bool    <------->     int
#    + True   1.txt  False  0
#    + 非零即为真
# 3. str   <------->     int
#    + str到int必须是纯数字组成
#    + int到str没有要求
#
# 4.    str     <------->    bool
#    + 非空即真。有空格也是真。
#    + bool转为str就是普通字符串的True  False   没有意义

test1=input()
print(int(test1))
test=' '
print(bool(test))
test2=102
print(str(test2))
print(bool(test2))
print(int(True))

print('----------------------')

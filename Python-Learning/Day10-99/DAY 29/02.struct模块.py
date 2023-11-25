import struct

num1 = 123456789   # 这个代表字节数。
num2 = 123456
num3 = 123
num4 = 1

ret1 = struct.pack("i",num1)  # 将一定长度的数据转换为某种类型x字节的二进制码，  i 代表整型。
print(ret1,len(ret1))
ret2 = struct.pack("i",num2)
print(ret2,len(ret2))
ret3 = struct.pack("i",num3)
print(ret3,len(ret3))

ret4 = struct.pack("i",len("你好，朋友们"))
print(ret4,len(ret4))
print(struct.unpack("i",ret4))  # 这个只是代表你收到了多少字节数

print(struct.unpack("i",ret1))
print(struct.unpack("i",ret2))
print(struct.unpack("i",ret3))
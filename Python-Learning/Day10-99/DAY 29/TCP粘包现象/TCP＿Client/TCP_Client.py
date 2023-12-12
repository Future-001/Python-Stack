import struct
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9011))
ret = sk.recv(1024).decode("utf-8")
if ret:
    print(ret)
sk.send("成功与客户端建立连接".encode("utf-8"))

while True:
    content = input(">>> ")
    content_b = content.encode("utf-8")
    # 这里一定要是这样，不然有问题，因为你要发送的是字节，只用Len(content)
    # 得出的是字符串的长度，但是不一定是字节的长度。一个汉字 3字节
    msg_len = struct.pack("i",len(content_b))
    sk.send(msg_len)
    sk.send(content_b)
    length = sk.recv(4)
    msg_length = struct.unpack("i",length)[0]
    msg = sk.recv(msg_length).decode("utf-8")
    print("server:",msg)


sk.close()
import socket
import struct

# 测试了32的测试端口，本端口是客户端。

sk = socket.socket()
sk.connect(("127.0.0.1",9101))

while True:
    content = input(">>>")
    content = content.encode("utf-8")
    msg_l=struct.pack("i",len(content))
    sk.send(msg_l)
    sk.send(content)
    print("<<< 发送成功 >>>")

    length = struct.unpack("i",sk.recv(4))[0]
    msg = sk.recv(length).decode("utf-8")
    print(">>>server: ",msg)

sk.close()
import struct
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9901))

while True:
    msg_length = (sk.recv(4)).decode("utf-8")  # 为什么是4 ，你发送的数据长度填充为4 ，转换为字节后，最大长度就是 4
    msg = sk.recv(int(msg_length)).decode("utf-8")
    print(msg)
    send_msg = input(">>>")
    if send_msg.upper() == 'Q':break
    send_length = str(len(send_msg)).zfill(4)
    sk.send(send_length.encode("utf-8"))
    sk.send(send_msg.encode("utf-8"))

sk.close()
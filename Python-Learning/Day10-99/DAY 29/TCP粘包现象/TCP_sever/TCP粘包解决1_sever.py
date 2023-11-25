import struct
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",9901))

sk.listen()

while True:
    conn, addr = sk.accept()
    print("连接成功")
    while True:
        send_msg = input(">>>")
        # 通过设置发送的消息的 长度来解决粘包问题，注意，发送的数据 最大长度  9999
        length = str(len(send_msg)).zfill(4)   # 字节啊，这样最大就是 9999了
        conn.send(length.encode("utf-8"))
        if send_msg.upper() == 'Q':break
        conn.send(send_msg.encode("utf-8"))

        recv_length = (conn.recv(4)).decode("utf-8")
        msg = conn.recv(int(recv_length)).decode("utf-8")
        if msg.upper() == "Q":break
        print(msg)
    conn.close()
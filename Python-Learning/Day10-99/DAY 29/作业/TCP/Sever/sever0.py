import socket
import struct
import random

sk = socket.socket()
sk.bind(("127.0.0.1",9018))

sk.listen()
color = [str("\033[31m"),str("\033[32m"), str("\033[33m"),
          str("\033[34m"), str("\033[35m"), str("\033[36m")]

while True:
    conn,addr = sk.accept()
    ret = conn.recv(1024).decode()
    i= random.randint(0,7)
    if ret:
        conn.send("server 连接成功".encode("utf-8"))
        print("client",addr, "连接成功")
        while True:
            try:
                print(color[i])
                length = conn.recv(4)
                msg_length = struct.unpack("i", length)[0]
                msg = conn.recv(msg_length).decode("utf-8")
                print(addr, "client:", msg)
                content = input(">>>  ")
                content_b = content.encode("utf-8")
                msg_len = struct.pack("i", len(content_b))
                conn.send(msg_len)
                conn.send(content_b)
            except ConnectionResetError:
                print(addr,"已断开连接，请重试")
                conn.close()
                break

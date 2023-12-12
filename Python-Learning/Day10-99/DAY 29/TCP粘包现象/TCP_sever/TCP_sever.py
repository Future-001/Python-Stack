import socket
import struct

sk = socket.socket()
sk.bind(("127.0.0.1",9011))
sk.listen()

while True:
    conn,addr = sk.accept()
    conn.send("成功与服务器建立连接".encode("utf-8"))
    ret = conn.recv(1024).decode("utf-8")
    if ret:
        print(ret)
    while True:
        length = conn.recv(4)
        msg_length = struct.unpack("i", length)[0]
        msg = conn.recv(msg_length).decode("utf-8")
        print(addr,"client:",msg)
        content = input(">>>  ")
        content_b = content.encode("utf-8")
        msg_len = struct.pack("i",len(content_b))
        conn.send(msg_len)
        conn.send(content_b)



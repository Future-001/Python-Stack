import socket
import os
import hashlib

secret_key = b'calvin_sb'

sk = socket.socket()
sk.bind(('127.0.0.1',9009))
sk.listen()

conn,addr = sk.accept()

get_s = os.urandom(16)
conn.send(get_s)

sha = hashlib.sha1(secret_key)
sha.update(get_s)
ret = sha.hexdigest()

res = conn.recv(1024).decode("utf-8")
if res==ret:
    print("客户端合法")
    conn.send("可以进行通信了".encode("utf-8"))
else:
    print("客户端非法")
    conn.send("不合法信息".encode("utf-8"))
    conn.close()
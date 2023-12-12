import socket
import time

server = ("127.0.0.1",9014)

sk = socket.socket(type=socket.SOCK_DGRAM)
t = time.time()
sk.sendto(time.strftime("%y-%m-%d %H:%M:%S",).encode("utf-8"),server)
ret = sk.recv(1024).decode()
if ret:
    print("server",ret)
    while True:
        content = input(">>> ")
        sk.sendto(content.encode("utf-8"),server)

        msg= sk.recv(1024).decode()
        print(msg)
else:
    print("服务器连接失败")
import socket
import random

sk = socket.socket(type=socket.SOCK_DGRAM)

sk.bind(("127.0.0.1",9014))
color = [str("\033[31m"),str("\033[32m"), str("\033[33m"),
          str("\033[34m"), str("\033[35m"), str("\033[36m")]
# msg,client_addr = sk.recvfrom(1024)

while True:
    msg, client_addr = sk.recvfrom(1024)
    i = random.randint(0, 7)
    print(color[i])
    print(client_addr ,"client 连接成功",msg.decode("utf-8"))
    sk.sendto("连接成功".encode("utf-8"),client_addr)
    while True:
        try:
            print(client_addr,":",sk.recv(1024).decode("utf-8"))
            msg = input(">>>")
            sk.sendto(msg.encode("utf-8"),client_addr)
        except ConnectionResetError:
            print(client_addr,"已断开连接")
            break

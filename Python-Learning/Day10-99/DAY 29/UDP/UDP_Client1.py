import socket
sk = socket.socket(type = socket.SOCK_DGRAM)

# sever = ("127.0.0.1",9002)
sever = ("127.0.0.1",9014)

while True:
    send_msg = input(">>>")
    if send_msg.upper() == "Q":break  # 客户端想退出，直接退出就行了。
    sk.sendto(send_msg.encode("utf-8"),sever)
    msg = sk.recv(1024).decode("utf-8")
    if msg.upper() == "Q":break
    print("server:", msg)

# recv 是收到消息，recvfrom 收到消息地址  但是我们已经有地址了
import socket
sk = socket.socket(type = socket.SOCK_DGRAM)

sever = ("127.0.0.1",9002)

while True:
    send_msg = input(">>>")
    if send_msg.upper() == "Q":break  # 客户端想退出，直接退出就行了。
    sk.sendto(send_msg.encode("utf-8"),sever)
    if sk.recv(1024).decode("utf-8").upper() == "Q":break
    print(sk.recv(1024).decode("utf-8"))

# recv 是收到消息，recvfrom 收到消息已经地址  但是我们已经有地址了
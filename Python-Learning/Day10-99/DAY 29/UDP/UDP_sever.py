import socket
sk = socket.socket(type = socket.SOCK_DGRAM)
sk.bind(("127.0.0.1",9002))

# 因为是无连接的，不需要进行监听了。

while True:
    recv_msg, client_addr = sk.recvfrom(1024)
    # if recv_msg.decode("utf-8").upper() == "Q": break    如果客户端想退出，他直接退出就行了，我们是没有连接的
    print(client_addr,"client:",recv_msg.decode("utf-8"))
    send_msg = input(">>>")
    # if send_msg.upper() == "Q": break    这里服务器端不能退出，因为他同时和多个客户端进行通信了。退出直接就没了。
    if send_msg.upper() != 'Q': sk.sendto(send_msg.encode("utf-8"), client_addr)



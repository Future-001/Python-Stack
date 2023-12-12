import socket
sk = socket.socket()   # 创建一个 sever 端的对象

# sk.bind(('10.17.52.81',9000))   # sk 存储的是： 申请操作系统的资源     给sever 端绑定一个地址
sk.bind(('127.0.0.1',9001))
print("sk: ",sk)  # <socket.socket fd=344, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9000)>

sk.listen()    # 开始监听（可以接收）客户端给我的连接了

"""  # 初级版本的
conn,addr = sk.accept()  # 建立连接 conn是连接，addr 是客户端地址  三次握手
# conn 存储了客户端与服务端的连接信息。
print("conn:", conn,"addr: ",addr)
conn.send(b'client num? please ')
msg = conn.recv(1024)
print(msg)
conn.close()  # 关闭和当前客户端的连接，四次挥手
"""



# 多客户端通信： && 多说几句
while True:   # 多客户端通信,不能并发通信，是有一定问题的。
    conn, addr = sk.accept()
    # conn: <socket.socket fd=404, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,
    #          laddr=('127.0.0.1', 9000), raddr=('127.0.0.1', 9309)>   这个是conn发送的连接。
    #  addr: ('127.0.0.1', 9309)
    print("conn:",conn,"addr:",addr)
    while True:   # 多说几句
        send_msg = input(">>> ")
        if send_msg.upper() =='Q':break
        conn.send(send_msg.encode("utf-8"))
        msg = conn.recv(1024).decode("utf-8")
        if msg.upper() == 'Q':break
        # print("conn:", conn2, "addr: ", addr, )
        print(msg)
    conn.close()

sk.close()   # 服务器断开整个服务。  归还申请的操作系统的资源
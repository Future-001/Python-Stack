import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9001))
# sk.connect(("127.0.0.1",9000))    #  建立连接 三次握手

msg = sk.recv(1024)
print(msg)
sk.send(b'client 1 this is ')

sk.close()    #  关闭连接， 四次挥手
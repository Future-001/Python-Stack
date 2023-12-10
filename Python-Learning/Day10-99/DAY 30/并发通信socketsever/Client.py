import socket

sk = socket.socket()
sk.connect(("127.0.0.1",9012))

while True:
    content = input("请输入:")
    sk.send(content.encode("utf-8"))
    res = sk.recv(1024).decode("utf-8")
    print(res)
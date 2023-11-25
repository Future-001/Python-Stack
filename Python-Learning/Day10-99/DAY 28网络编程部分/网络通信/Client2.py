import socket
sk = socket.socket()

sk.connect(("127.0.0.1", 9001))
while True:
    msg = sk.recv(1024).decode("utf-8")
    if msg.upper() == 'Q':break
    print(msg)
    send_msg = input(">>> ")
    if send_msg.upper == 'Q':break
    sk.send(send_msg.encode("utf-8"))


sk.close()
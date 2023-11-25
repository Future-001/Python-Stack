import struct
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9011))

while True:
    length = sk.recv(4)
    msg_length = struct.unpack("i",length)[0]
    msg = sk.recv(msg_length).decode("utf-8")
    print(msg)
    if msg.upper() == 'Q': break

    send_msg = input(">>>")
    if send_msg.upper() == 'Q':break
    send_msg_length = struct.pack("i",len(send_msg.encode("utf-8")))
    sk.send(send_msg_length)
    sk.send(send_msg.encode("utf-8"))

sk.close()
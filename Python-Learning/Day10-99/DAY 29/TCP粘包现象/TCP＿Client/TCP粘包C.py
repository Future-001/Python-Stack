import struct
import socket
import time

sk = socket.socket()
sk.connect(("127.0.0.1",9007))

time.sleep(0.5)
msg1 = sk.recv(1024)
print(msg1.decode("utf-8"))
msg2 = sk.recv(1024)
print(msg2.decode("utf-8"))

sk.close()
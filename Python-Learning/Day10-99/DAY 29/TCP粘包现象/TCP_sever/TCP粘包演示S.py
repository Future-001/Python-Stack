import struct
import socket

sk = socket.socket()
sk.bind(("127.0.0.1",9007))

sk.listen()

conn,addr = sk.accept()
conn.send('粘包了吗？|'.encode('utf-8'))
conn.send('确实粘了 '.encode('utf-8'))

conn.close()

sk.close()
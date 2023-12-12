import socket
import hashlib
import os

secret_key = b'calvin_sb'
sk = socket.socket()

sk.connect(("127.0.0.1",9009))
rand = sk.recv(16)

sha = hashlib.sha1(secret_key)
sha.update(rand)
ret = sha.hexdigest()

sk.send(ret.encode("utf-8"))

re = sk.recv(1024).decode("utf-8")
print(re)
import socket
import json

sk =socket.socket()

sk.bind(("127.0.0.1",9011))
sk.listen()

conn,_ = sk.accept()
print(sk.accept())

msg = conn.recv(1024).decode("utf-8")

print(msg)

msg = json.loads(msg)
print(msg)

with open(msg['filename'],mode='wb') as f:
    content = conn.recv(msg['filesize'])
    print("-->",len(content))
    f.write(content)

conn.close()

sk.close()
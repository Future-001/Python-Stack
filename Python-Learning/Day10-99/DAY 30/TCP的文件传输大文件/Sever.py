import socket
import json

sk =socket.socket()

sk.bind(("127.0.0.1",9010))
sk.listen()

conn,_ = sk.accept()

msg = conn.recv(1024).decode("utf-8")

print(msg)

msg = json.loads(msg)
print(msg)

with open(msg['filename'],mode='wb') as f:
    # content = conn.recv(msg['filesize'])
    # print("-->",len(content))
    # f.write(content)
    while msg['filesize']>0:
        content = conn.recv(1024)
        msg['filesize']-=len(content)  # 不能减去1024，收到的不一定是1024个字节
        f.write(content)

conn.close()

sk.close()
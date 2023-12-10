import socket
import json
import struct

sk =socket.socket()

sk.bind(("127.0.0.1",9010))
sk.listen()

conn,_ = sk.accept()

msg_len = conn.recv(4)
#收到了 mlen
dic_len = struct.unpack("i",msg_len)[0]
msg = conn.recv(dic_len).decode("utf-8")
msg = json.loads(msg)

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
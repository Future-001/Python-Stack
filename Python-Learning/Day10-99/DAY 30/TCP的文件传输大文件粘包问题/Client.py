import socket
import os
import json
import struct

sk = socket.socket()

sk.connect(("127.0.0.1",9010))

# 文件名\文件大小
# abs_path = r"D:\Code Files\Python\Python-Learning\Day10-99\DAY 30\传输的文件.txt"
abs_path = r"D:\毕设\Visdrone\VisDrone\VisDrone2019-DET-val.zip"
filename = os.path.basename(abs_path)

filesize = os.path.getsize(abs_path)

# 字符串一般不用拼接起来的，用json模块
dic = {"filename":filename,"filesize":filesize}

#避免粘包

str_dic = json.dumps(dic)

b_dic = str_dic.encode("utf-8")
mlen = struct.pack("i",len(b_dic))
sk.send(mlen)  # 先发字典的字节长度 ，然后再发字典
sk.send(b_dic)

# sk.send(str_dic.encode("utf-8"))    # 万一有粘包呢？可能就不太行了


with open(abs_path,mode='rb') as f:
    # content = f.read()  # 内容少，直接读了
    # sk.send(content)

    # 文件比较大的时候
    while filesize>0:
        content = f.read(1024)
        filesize-=1024
        sk.send(content)

sk.close()

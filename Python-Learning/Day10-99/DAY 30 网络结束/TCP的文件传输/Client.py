import socket
import os
import json

sk = socket.socket()

sk.connect(("127.0.0.1",9011))

# 文件名\文件大小
# abs_path = r"D:\Code Files\Python\Python-Learning\Day10-99\DAY 30\传输的文件.txt"
abs_path = r"D:\Code Files\Python\Python-Learning\Day10-99\DAY 30\流程图.png"
filename = os.path.basename(abs_path)

filesize = os.path.getsize(abs_path)

# 字符串一般不用拼接起来的，用json模块
dic = {"filename":filename,"filesize":filesize}

str_dic = json.dumps(dic)
sk.send(str_dic.encode("utf-8"))    # 万一有粘包呢？可能就不太行了

with open(abs_path,mode='rb') as f:
    content = f.read()  # 内容少，直接读了
    sk.send(content)

sk.close()

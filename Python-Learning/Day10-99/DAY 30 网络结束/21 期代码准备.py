# 代码准备
# 字符串操作以及打印 —— 实现上传下载的进度条功能

# def processBar(num, total):
#     rate = num / total
#     rate_num = int(rate * 100)
#     if rate_num == 100:
#         r = '\r%s>%d%%\n' % ('=' * rate_num, rate_num,)
#     else:
#         r = '\r%s>%d%%' % ('=' * rate_num, rate_num,)
#     sys.stdout.write(r)
#     sys.stdout.flush
#
#
# socketserver —— 实现ftp
# server端和client端的交互


# import socketserver
#
#
# class MyServer(socketserver.BaseRequestHandler):
#     def handle(self):
#         conn = self.request
#         conn.sendall(bytes('欢迎致电 10086，请输入1xxx,0转人工服务.', encoding='utf-8'))
#         Flag = True
#         while Flag:
#             data = conn.recv(1024).decode('utf-8')
#             if data == 'exit':
#                 Flag = False
#             elif data == '0':
#                 conn.sendall(bytes('通过可能会被录音.balabala一大推', encoding='utf-8'))
#             else:
#                 conn.sendall(bytes('请重新输入.', encoding='utf-8'))
#
#
# if __name__ == '__main__':
#     server = socketserver.ThreadingTCPServer(('127.0.0.1.txt', 8008), MyServer)
#     server.serve_forever()


# import socket
#
# ip_port = ('127.0.0.1.txt', 8008)
# sk = socket.socket()
# sk.connect(ip_port)
# sk.settimeout(5)
#
# while True:
#     data = sk.recv(1024).decode('utf-8')
#     print('receive:', data)
#     inp = input('please input:')
#     sk.sendall(bytes(inp, encoding='utf-8'))
#     if inp == 'exit':
#         break
#
# sk.close()

#
# struct模块 —— 自定制报头解决文件上传下载过程中的粘包问题
#
# 复制代码
# import json, struct
#
# # 假设通过客户端上传1T:1073741824000的文件a.txt
#
# # 为避免粘包,必须自定制报头
# header = {'file_size': 1073741824000, 'file_name': '/a/b/c/d/e/a.txt',
#           'md5': '8f6fbf8347faa4924a76856701edb0f3'}  # 1T数据,文件路径和md5值
#
# # 为了该报头能传送,需要序列化并且转为bytes
# head_bytes = bytes(json.dumps(header), encoding='utf-8')  # 序列化并转成bytes,用于传输
#
# # 为了让客户端知道报头的长度,用struck将报头长度这个数字转成固定长度:4个字节
# head_len_bytes = struct.pack('i', len(head_bytes))  # 这4个字节里只包含了一个数字,该数字是报头的长度
#
# # 客户端开始发送
# conn.send(head_len_bytes)  # 先发报头的长度,4个bytes
# conn.send(head_bytes)  # 再发报头的字节格式
# conn.sendall(文件内容)  # 然后发真实内容的字节格式
#
# # 服务端开始接收
# head_len_bytes = s.recv(4)  # 先收报头4个bytes,得到报头长度的字节格式
# x = struct.unpack('i', head_len_bytes)[0]  # 提取报头的长度
#
# head_bytes = s.recv(x)  # 按照报头长度x,收取报头的bytes格式
# header = json.loads(json.dumps(header))  # 提取报头
#
# # 最后根据报头的内容提取真实的数据,比如
# real_data_len = s.recv(header['file_size'])
# s.recv(real_data_len)
# 复制代码
#
# hashlib模块 —— 实现文件的一致性校验和用户密文登录
#
# os模块 —— 实现目录的切换及查看文件文件夹等功能
#
# 文件操作 —— 完成上传下载文件及断点续传等功能
#
# 面向对象编程思想 + 继承知识 —— 组织简化代码
from multiprocessing import Process
import socket
import struct

def talk(*args):
    conn=args[0]
    addr = args[1]
    while True:
        try:
            msg_l = struct.unpack("i",conn.recv(4))[0]  # 一定记得是第一个元素
            msg = conn.recv(msg_l).decode("utf-8")
            print(addr[1],f">>> {msg}")

            # content = input("server >>>")   # python规定只能在父进程中用input，子进程中使用会报错
            content = "响应服务"
            content = content.encode("utf-8")
            c_l = struct.pack("i",len(content))
            conn.send(c_l)
            conn.send(content)
        except ConnectionResetError:
            print(f"已与{addr}断开连接")
            conn.close()

if __name__ == "__main__":
    sk = socket.socket()
    sk.bind(("127.0.0.1",9101))
    sk.listen()
    while True:
        conn,addr = sk.accept()
        Process(target=talk,args=(conn,addr,)).start()
    sk.close()
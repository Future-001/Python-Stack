import socket
from multiprocessing import Process

def talk(conn):
    while True:
        try:
            msg = conn.recv(1024).decode("utf-8")
            ret = msg.upper().encode("utf-8")
            conn.send(ret)
        except ConnectionResetError:
            conn.close()

if __name__ =="__main__":
    sk = socket.socket()
    sk.bind(("127.0.0.1", 9090))
    sk.listen()
    while True:
        conn, addr = sk.accept()
        Process(target=talk,args=(conn,)).start()
    sk.close()


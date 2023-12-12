import time
import socketserver

class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        """
        登录，注册等功能，每个客户端都得执行一次。
        """
        conn = self.request
        print("看看它是什么: ",self.request)
        print(self.client_address)
        while True:
            try:
                content = conn.recv(1024).decode("utf-8")
                conn.send(content.upper().encode("utf-8"))
                time.sleep(0.3)
            except ConnectionResetError:
                break
server = socketserver.ThreadingTCPServer(("127.0.0.1",9012),Myserver)
server.serve_forever()
import socketserver

class MySever(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                data = self.request.recv(1024)
                print(data, self.client_address)
                if not data:
                    break
                self.request.sendall(data.upper())
            except Exception as e:
                break
if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(("127.0.0.1",9999),MySever)
    s.serve_forever()

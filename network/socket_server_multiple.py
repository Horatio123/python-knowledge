import socketserver


class EchoHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        print('get data: ' + data.decode())
        self.request.sendall(data)


if __name__ == "__main__":
    with socketserver.TCPServer(("localhost", 8888), EchoHandler) as server:
        print('run server')
        server.serve_forever()

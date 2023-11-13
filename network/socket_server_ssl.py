import ssl
import socket


def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"Received: {request.decode()}")
    client_socket.sendall("Hello from server!".encode())
    client_socket.close()


if __name__ == '__main__':

    # 服务器地址和端口号
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 8000

    # 创建socket对象并绑定地址和端口号
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

    # 对socket进行SSL包装
    ssl_server_socket = ssl.wrap_socket(server_socket, certfile='server.crt', keyfile='server.key', server_side=True)

    # 开始监听连接
    ssl_server_socket.listen(5)

    print(f"Listening on {SERVER_ADDRESS}:{SERVER_PORT}")

    while True:
        # 接受客户端连接请求
        client_socket, client_address = ssl_server_socket.accept()
        print(f"Accepted connection from {client_address}")
        # 处理客户端请求
        handle_client(client_socket)

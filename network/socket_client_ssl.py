import socket
import ssl


def main():
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 使用SSL包装socket对象
    # ssl_context = ssl.create_default_context()
    # ssl_context.check_hostname = True
    # ssl_context.verify_mode = ssl.CERT_REQUIRED
    # ssl_context.load_verify_locations(cafile="server.crt")
    # ssl_context.server_hostname = "127.0.0.1"
    ssl_context = ssl.create_default_context(cafile='server.crt')
    ssl_context.check_hostname = False

    ssl_context.verify_mode = ssl.CERT_REQUIRED
    ssl_sock = ssl_context.wrap_socket(s)

    # 连接服务器
    ssl_sock.connect(('localhost', 8000))

    # 发送数据
    ssl_sock.send(b'Hello, server!')

    # 接收响应
    data = ssl_sock.recv(1024)
    print(f'Received data: {data.decode()}')

    # 关闭连接
    ssl_sock.close()


if __name__ == '__main__':
    main()

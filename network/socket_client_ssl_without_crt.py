import socket
import ssl


if __name__ == '__main__':
    # 服务器地址和端口号
    SERVER_ADDRESS = '127.0.0.1'
    SERVER_PORT = 8000

    # 创建socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 对socket进行SSL包装
    ssl_socket = ssl.wrap_socket(client_socket, cert_reqs=ssl.CERT_NONE)

    # 连接服务器
    ssl_socket.connect((SERVER_ADDRESS, SERVER_PORT))

    # 发送数据
    data = 'Hello, server!'
    ssl_socket.write(data.encode())

    # 接收响应并解密
    response = ssl_socket.read()
    decrypted_response = response.decode()

    # 打印响应
    print(f"Received from server: {decrypted_response}")

    # 关闭socket
    ssl_socket.close()

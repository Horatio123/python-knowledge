import socket  # 导入socket库
from time import ctime
import json
import time

HOST = '127.0.0.1'
PORT = 9001
ADDR = (HOST, PORT)
BUFFSIZE = 1024  # 定义一次从socket缓冲区最多读入1024个字节
MAX_LISTEN = 5  # 表示最多能接受的等待连接的客户端的个数


def tcpServer():  # TCP服务
    # with socket.socket() as s:
    with socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM) as s:  # AF_INET表示socket网络层使用IP协议，SOCK_STREAM表示socket传输层使用tcp协议
        # 绑定服务器地址和端口
        s.bind(ADDR)
        # 启动服务监听 MAX_LISTEN
        s.listen(MAX_LISTEN)
        print('start listen')
        while True:
            # 等待客户端连接请求,获取connSock
            print('等待用户接入……')
            conn, addr = s.accept()
            print('警告，远端客户:{} 接入系统！！！'.format(addr))
            # with conn:
            while True:
                print('接收请求信息……')
                # 接收请求信息
                data = conn.recv(BUFFSIZE)  # 读取的数据一定是bytes类型，需要解码成字符串类型
                info = data.decode()
                # print('data=%s' % data)
                print(f'接收数据：{info}')

                # 发送请求数据
                conn.send(f'服务端接收到信息{info}'.encode())
                print('发送返回完毕！！！')

                if info == 'q':
                    break
            conn.close()


# 创建UDP服务
def udpServer():
    # 创建UPD服务端套接字
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # 绑定地址和端口
        s.bind(ADDR)
        # 等待接收信息
        while True:
            print('UDP服务启动，准备接收数据……')
            # 接收数据和客户端请求地址
            data, address = s.recvfrom(BUFFSIZE)

            if not data:
                break
            info = data.decode()
            print(f'接收请求信息：{info}')

            s.sendto(b'i am udp,i got it', address)

        s.close()


if __name__ == '__main__':

    while True:
        choice = input('input choice t-tcp or u-udp:')

        if choice != 't' and choice != 'u':
            print('please input t or u,ok?')
            continue

        if choice == 't':
            print('execute tcpsever')
            tcpServer()
        else:
            print('execute udpsever')
            udpServer()